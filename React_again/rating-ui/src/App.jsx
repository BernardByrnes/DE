import React from "react";
import Rating from "./components/Rating";

const App = () => {
  const name = "Ben";
  return (
    <div>
      <h1>Hello {name}</h1>
      <Rating />
    </div>
  );
};

export default App;
