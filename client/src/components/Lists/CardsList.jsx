import React from "react";

export function CardsList({ products }) {
  if (!products) {
    return <h1>Loading....</h1>;
  }
  return (
    <>
      {products.map((product) => (
        <a
          href={
            product.name ? `/Ingredient/${product.id}` : `/Recipe/${product.id}`
          }
          key={product.id}
        >
          <div className="m-2 bg-white h-[360px] w-[350px] border rounded-lg border-gray-300 text-black">
            <h1 className="text-center mt-5 mb-[30px]">
              {product.name?.toUpperCase()}
              {product.title?.toUpperCase()}
            </h1>
            <img
              className="bg-white m-auto self-end"
              src={
                product.name
                  ? `https://spoonacular.com/cdn/ingredients_100x100/${product.image}`
                  : `${product.image}`
              }
              alt={product.name}
            />
          </div>
        </a>
      ))}
    </>
  );
}
