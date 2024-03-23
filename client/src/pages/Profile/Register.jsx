import { useState } from "react";
import { register } from "../../api/users.api";
export function Register() {
  const [error, setError] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    const formData = new FormData(e.target);
    const newUser = Object.fromEntries(formData.entries());
    try {
      const res = await register(newUser);
      if (res.status === 201) {
        setError(NULL);
      }
    } catch (error) {
      let errorsEntries = [];
      error.response
        ? (errorsEntries = Object.entries(error.response.data))
        : "";
      let errorMessage = "";
      errorsEntries.forEach((error) => {
        errorMessage += `${error[0]}: ${error[1]}\n`;
      });
      setError(errorMessage);
    }
  };
  return (
    <div className="flex items-center justify-center mt-[40px]">
      <form
        onSubmit={handleSubmit}
        className="w-[500px] bg-neutral-800 p-[50px] h-full rounded-2xl text-black"
      >
        <h1 className="text-4xl text-center text-white"> Register </h1>
        {error && <h1 className="text-red-600 mt-8">{error}</h1>}
        <div className="mt-10 flex justify-center items-center flex-col">
          <label
            htmlFor="username"
            className="block  text-green-600 font-semibold"
          >
            Username:
          </label>
          <input
            type="text"
            id="username"
            name="username"
            className="text-center mt-1 block w-full rounded border-gray-300 shadow-sm focus:border-blue-500 focus:ring focus:ring-blue-500 focus:ring-opacity-50"
            required
          />
        </div>

        <div className="mt-10 flex justify-center items-center flex-col">
          <label
            htmlFor="password"
            className="block text-green-600 font-semibold"
          >
            Password:
          </label>
          <input
            type="password"
            id="password"
            name="password"
            className="mt-1 text-center block w-full rounded border-gray-300 shadow-sm focus:border-blue-500 focus:ring focus:ring-blue-500 focus:ring-opacity-50"
            required
          />
        </div>

        <div className="mt-10 flex justify-center items-center flex-col">
          <label
            htmlFor="repeatPassword"
            className="block text-green-600 font-semibold"
          >
            Repeat Password:
          </label>
          <input
            type="password"
            id="repeatPassword"
            name="repeatPassword"
            className="mt-1 text-center block w-full rounded border-gray-300 shadow-sm focus:border-blue-500 focus:ring focus:ring-blue-500 focus:ring-opacity-50"
            required
          />
        </div>
        <div className="mt-10 flex justify-center items-center flex-col">
          <label
            htmlFor="gender"
            className="block text-green-600 font-semibold mb-2"
          >
            Gender:
          </label>
          <select id="gender" name="gender">
            <option value="Male">Male</option>
            <option value="Female">Female</option>
          </select>
        </div>
        <div className="m-10 flex justify-center items-center flex-col">
          <label
            htmlFor="email"
            className="block text-green-600 font-semibold mb-2"
          >
            Email:
          </label>
          <input
            type="email"
            id="email"
            name="email"
            placeholder="Enter your email"
            required
          />
        </div>
        <div className="m-10 flex justify-center items-center flex-col">
          <label
            htmlFor="date_of_birth"
            className="block text-green-600 font-semibold mb-2"
          >
            Birthdate:
          </label>
          <input type="date" id="date_of_birth" name="date_of_birth" required />
        </div>

        <div className="m-10 text-white flex justify-center items-center flex-col">
          <button
            type="submit"
            className="text-white block bg-green-700 p-[30px] pt-[10px] pb-[10px] rounded-lg mb-[20px]"
          >
            Register
          </button>
          You Already Have An Account?
          <a
            href="/Login"
            className="mt-[10px] w-[100px] text-center text-white block bg-green-700 pt-[10px] pb-[10px] rounded-lg"
          >
            {" "}
            Log In
          </a>
        </div>
      </form>
    </div>
  );
}
