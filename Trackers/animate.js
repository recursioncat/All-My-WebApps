const trailer = document.querySelector(".shape");
box = document.querySelector(".fa"); 

box.addEventListener("mousemove", (e) => {
  const rect = box.getBoundingClientRect();
  const x = e.clientX - rect.left - trailer.offsetWidth / 2;
  const y = e.clientY - rect.top - trailer.offsetHeight / 2;

  console.log(x);
  console.log(y);

  const maxX = box.offsetWidth - trailer.offsetWidth;
  const maxY = box.offsetHeight - trailer.offsetHeight;

  const clampedX = Math.max(0, Math.min(x, maxX));
  const clampedY = Math.max(0, Math.min(y, maxY));

  const keyframes = {
    transform: `translate(${clampedX}px, ${clampedY}px)`,
  }

  const animation = trailer.animate(keyframes, {
    duration: 800,
    fill:'forwards'
  });

});

// Array of image file names
const images = [
  "images/All About the Real-Life Story Behind Oscar-Nominated War Movie '1917'.png",
  "images/Break Out The Hanky_ Tom's Got It Out For Your Tearducts.png",
  "images/Eternal sunshine of the spotless mind by Michel Gondry (2004).png",
  "images/Fight Club (1999) [935 1350] by Saajan.png",
  "images/f423aeba03eb285227672888dd1a71d1.png"
  // Add all your image file names here
];

// Function to select a random image
function getRandomImage() {
  const randomIndex = Math.floor(Math.random() * images.length);
  return images[randomIndex];
}

// Update the src attribute of the img tag with the selected image
document.addEventListener("DOMContentLoaded", () => {
  const mainPhoto = document.getElementById("mainPhoto");
  mainPhoto.src = getRandomImage();
});
