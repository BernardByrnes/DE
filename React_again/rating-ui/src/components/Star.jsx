import React from "react";

const Star = ({ star, ratingClick, rating, hover, color }) => {
  return (
    <span
      onClick={() => ratingClick(star)}
      className="star"
      style={{ color: star <= (hover || rating) ? color : "#ccc" }}
    >
      {"\u2605"}
    </span>
  );
};

export default Star;
