import React from "react";

function SearchResults({ products }) {
  return (
    <div className="flex flex-wrap w-full">
      {products.map((product) => (
      <a href={`/Ingredient?id=${product.id}`} key={product.name}>
        <div
          className="m-2 bg-neutral-900 h-[260px] w-[300px] border rounded-lg border-gray-300 text-black"
        >
          <h1 className="text-white text-center mt-5">
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
  );
}

export default SearchResults;
