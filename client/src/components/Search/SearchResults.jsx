import React from "react";

function SearchResults({ products }) {
  return (
    <div className="flex flex-wrap w-full">
      {products.map((product) => (
        <div
          key={product.name}
          className="m-2 bg-neutral-900 h-[260px] w-[300px] border rounded-lg border-gray-300 text-black"
        >
          <h1 className="text-white text-center mt-5">
            {product.name.toUpperCase()}
          </h1>
          <a href={`/Ingredient?id=${product.id}`}>
            <img
              className="bg-white m-auto w-1/2 mt-[40px] h-1/2 "
              src={`https://spoonacular.com/cdn/ingredients_100x100/${product.image}`}
              alt={product.name}
            />
          </a>
        </div>
      ))}
    </div>
  );
}

export default SearchResults;
