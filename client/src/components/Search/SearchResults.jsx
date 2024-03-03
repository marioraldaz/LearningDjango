import React from "react";

function SearchResults({ products }) {
  return (
    <div className="w-full flex items-center justify-center">
      <div className="grid grid-cols-auto-fit w-4/5">
      {products.map((product) => (
      <a href={`/Ingredient?id=${product.id}`} key={product.name}>
        <div
          className="m-2 bg-white h-[260px] w-[250px] border rounded-lg border-gray-300 text-black"
        >
          <h1 className="text-center mt-5">
            {product.name.toUpperCase()}
          </h1>
            <img
              className="bg-white m-auto w-1/2 mt-[40px] h-1/2 "
              src={`https://spoonacular.com/cdn/ingredients_100x100/${product.image}`}
              alt={product.name}
            />
        </div>
      </a>
      ))}
    </div>

      </div>
  );
}

export default SearchResults;
