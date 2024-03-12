import React from "react";

export function SearchResults({ products }) {
  console.log(products);
  return (
    <div className="flex flex-wrap justify-center items-center mt-[100px] p-[10px]">
      {products.map((product) => (
      <a href={product.name ? `/Ingredient?id=${product.id}` : `/Recipe?id=${product.id}`} key={product.name}>
        <div
          className="m-2 bg-white h-[360px] w-[350px] border rounded-lg border-gray-300 text-black"
        >
          <h1 className="text-center mt-5 mb-[30px]">
            {product.name?.toUpperCase()}
            {product.title?.toUpperCase()}
          </h1>
            <img
              className="bg-white m-auto self-end"
              src={product.name ? `https://spoonacular.com/cdn/ingredients_100x100/${product.image}` : `${product.image}`}
              alt={product.name}
            />
        </div>
      </a>
      ))}

      </div>
  );
}
