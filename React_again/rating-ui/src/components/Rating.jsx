import { useState } from "react";

const Rating = () => {
  const [rating, setRating] = useState(0);

  const stars = Array.from({ length: 5 }, (_, i) => i + 1);

  return (
    <div className="rating-container">
      <h2>Rate Your Experience</h2>
      <div className="stars">
        {stars.map((star) => (
          <span onClick={() => setRating(star)} key={star} className="star">
            {"\u2605"}
          </span>
        ))}
      </div>
    </div>
  );
};

export default Rating;
