const Rating = () => {
  const stars = Array.from({ length: 5 }, (_, i) => i + 1);

  const clicked = (index) => {
    console.log("clicked", index + 1);
  };

  const hovered = (direction) => console;

  return (
    <div className="rating-container">
      <h2>Rate Your Experience</h2>
      <div className="stars">
        {stars.map((star, index) => (
          <span
            onMouseEnter={() => hovered("enter")}
            onMouseLeave={() => hovered("leave")}
            onClick={() => clicked(index)}
            key={star}
            className="star"
          >
            {"\u2605"}
          </span>
        ))}
      </div>
    </div>
  );
};

export default Rating;
