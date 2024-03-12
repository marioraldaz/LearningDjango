import React, {useState} from 'react'

export function RecipeNutrition({nutrition}) {

    const [flavonoids, setFlavonoids] = useState(false);
  return (
    <div>
      <div className="">
            <h3>Carbs Percentage: {nutrition.percentCarbs} </h3>
            <h3>Fat Percentage: {nutrition.percentFat}</h3>
            <h3>Protein Percentage: {nutrition.percentProtein}</h3>
      </div>
      {flavonoids &&
      <div className="">
        {flavonoids.map((elem)=>{
            <div key={elem.name} className="">
                <span>{elem.name}</span>
                <span>{elem.amount}</span>
                <span>{elem.unit}</span>     
            </div> 
        })}
      </div>
      <div className=""
      }
    </div>
  )
}

