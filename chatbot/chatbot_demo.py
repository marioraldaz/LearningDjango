import os
from dotenv import load_dotenv  # type: ignore
from langchain_openai import ChatOpenAI  # type: ignore
from typing import Annotated, List, Tuple, Union
from langchain.tools import BaseTool, StructuredTool, Tool  # type: ignore
from langchain_experimental.tools import PythonREPLTool  # type: ignore
from langchain_core.tools import tool  # type: ignore
import random
from langchain.agents import AgentExecutor, create_openai_tools_agent  # type: ignore
from langchain_core.messages import BaseMessage, HumanMessage  # type: ignore
from langchain_openai import ChatOpenAI  # type: ignore
from langchain_core.prompts import ( # type: ignore
    ChatPromptTemplate,
    FewShotPromptTemplate,
    MessagesPlaceholder,
    PromptTemplate,
    SystemMessagePromptTemplate,
)
from sqlalchemy import create_engine  # type: ignore
from langchain.output_parsers.openai_functions import JsonOutputFunctionsParser # type: ignore
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder # type: ignore
import operator
from typing import Annotated, Any, Dict, List, Optional, Sequence, TypedDict
import functools
from langchain.pydantic_v1 import BaseModel, Field  #type: ignore
from langchain.chains import create_sql_query_chain # # type: ignore
from langchain_community.utilities.sql_database import SQLDatabase  # type: ignore
from langchain.tools.retriever import create_retriever_tool #type:ignore
from langchain_community.document_loaders import WebBaseLoader, TextLoader #type:ignore
from langchain_text_splitters import RecursiveCharacterTextSplitter, CharacterTextSplitter #type:ignore
from langchain_openai import OpenAIEmbeddings #type:ignore
from langchain_community.vectorstores import FAISS #type:ignore
from sqlalchemy import Table, text #type: ignore
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder   # type: ignore
from langgraph.graph import StateGraph, END  # type: ignore
from langchain_core.runnables import ( # type: ignore
    ConfigurableField,
    RunnablePassthrough,
)
from django.conf import settings

# Now you can use BASE_DIR from settings
from langchain_core.utils.function_calling import convert_to_openai_function # type: ignore
from langchain_core.output_parsers import StrOutputParser # type: ignore
load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv('OPENAI_KEY')
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv('LANGSMITH_KEY')
os.environ["LANGCHAIN_PROJECT"] = "invoice charbot"

llm = ChatOpenAI(model="gpt-4o")


def create_agent(llm: ChatOpenAI, tools: list, system_prompt: str):
    # Each worker node will be given a name and some tools.
    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                system_prompt,
            ),
            MessagesPlaceholder(variable_name="messages"),
            MessagesPlaceholder(variable_name="agent_scratchpad"),
        ]
    )
    agent = create_openai_tools_agent(llm, tools, prompt)
    executor = AgentExecutor(agent=agent, tools=tools)
    return executor

# agent node
def agent_node(state, agent, name):
    result = agent.invoke(state)
    return {"messages": [HumanMessage(content=result["output"], name=name)]}

members = ["database_manager", "nutrition_expert"]
system_prompt = (
    "You are a supervisor tasked with managing a conversation between the"
    " following workers:  {members}. Given the following user request,"
    " respond with the worker to act next. Each worker will perform a"
    " task and respond with their results and status. Always call first the database_manager and then the nutrition_expert. You can only call each agent 2 times." 
)
# Our team supervisor is an LLM node. It just picks the next agent to process
# and decides when the work is completed
options = ["FINISH"] + members
# Using openai function calling can make output parsing easier for us
function_def = {
    "name": "route",
    "description": "Select the next role.",
    "parameters": {
        "title": "routeSchema",
        "type": "object",
        "properties": {
            "next": {
                "title": "Next",
                "anyOf": [
                    {"enum": options},
                ],
            }
        },
        "required": ["next"],
    },
}
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        MessagesPlaceholder(variable_name="messages"),
        (
            "system",
            "Given the conversation above, who should act next?"
            " Or should we FINISH? Select one of: {options}",
        ),
    ]
).partial(options=str(options), members=", ".join(members))


supervisor_chain = (
    prompt
    | llm.bind_functions(functions=[function_def], function_call="route")
    | JsonOutputFunctionsParser()
)



# The agent state is the input to each node in the graph
class AgentState(TypedDict):
    # The annotation tells the graph that new messages will always
    # be added to the current states
    messages: Annotated[Sequence[BaseMessage], operator.add]
    # The 'next' field indicates where to route to next
    next: str


embeddings = OpenAIEmbeddings()


db = FAISS.load_local("nutrition_vector_database", embeddings,allow_dangerous_deserialization=True) #Load db

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SQL_lite_uri = f"sqlite:///{os.path.join(BASE_DIR, 'db.sqlite3')}"

SQL_db = SQLDatabase.from_uri(SQL_lite_uri)

@tool("execute_sql_query", return_direct=False)
def execute_sql_query(sql_query):
    """Executes the SQL query in the database"""
    print("Executing query: ",sql_query)
    try:
        # Assuming you have already defined the engine variable
        engine = create_engine(SQL_lite_uri)
        # Connect to the database
        connection = engine.connect()
        # Execute the SQL query
        result = connection.execute(text(sql_query))
        formatted = ""
        # Process the result if needed
        for row in result:
            formatted += str(row)
        return formatted
    except Exception as e:
        print("Error executing", e)
    finally:
        # Close the connection
        connection.close()
        
db = FAISS.load_local("database_info_vector_database", embeddings,allow_dangerous_deserialization=True) #Load db

        
retriever = db.as_retriever()

database_retriever_tool = create_retriever_tool(retriever,"database_retriever_tool",
                    "Retrieves information about tables in the database.")

retriever = db.as_retriever()

retrieve_nutrition_info = create_retriever_tool(retriever,"nutrition_retriever_tool",
                    "Retrieves information about nutrition.")



nutrition_expert = create_agent(llm, [retrieve_nutrition_info ],"You are a nutrition expert. You need to provide advice for the user. You need to find what fits the user better. Only answer the user question." )
nutrition_expert_node = functools.partial(agent_node, agent=nutrition_expert, name="nutrition_expert")

database_manager = create_agent(llm, [execute_sql_query, database_retriever_tool],"You are a database manager, you need to get information from the database by executing the right SQL query. The information needs to be related to the UserProfile with this id: "+"1")
database_manager_node = functools.partial(agent_node, agent=database_manager, name="database_manager")

workflow = StateGraph(AgentState)

# Add nodes for fuel anomaly expert and fuel database expert
workflow.add_node("nutrition_expert", nutrition_expert_node)
workflow.add_node("database_manager", database_manager_node)

# Add supervisor node and conditional edges
workflow.add_node("supervisor", supervisor_chain)

# Add edges for each member
for member in members:
    workflow.add_edge(member, "supervisor")

# Update conditional map to include all relevant nodes
conditional_map = {k: k for k in members}
conditional_map["FINISH"] = END
conditional_map["database_manager"] = "database_manager"
conditional_map["nutrition_expert"] = "nutrition_expert"

# Add conditional edges based on the conditional map
workflow.add_conditional_edges("supervisor", lambda x: x["next"], conditional_map)

# Finally, add entrypoint
workflow.set_entry_point("supervisor")

# Compile the graph
graph = workflow.compile()

config = {"recursion_limit": 20}
for s in graph.stream(
    {
        "messages": [
            HumanMessage(content="Am I lacking any vitamin?")
        ]
    }, config=config
):
    if "__end__" not in s:
        print(s)
        print("----")

    """
    I need a recipe that is low in carbs and high in protein
    Am I lacking any vitamin?
    """