const photos = [
    "assets/Graduation2026_1.jpg",
    "assets/Graduation2026_2.jpg",
    "assets/FOF2024_1.jpg",
    "assets/FOF2024_2.jpg",
    "assets/NLC2025_2.jpg",
    "assets/NLC2025_3.jpg",
    "assets/NLC2025_4.jpg",
    "assets/NLC2025_5.jpg",
    "assets/NLC2025_6.jpg",
    "assets/NLC2025_7.jpg",
    "assets/NLC2025_8.jpg",
    "assets/NLC2025_9.jpg",
    "assets/Regionals2026_1.jpg",
    "assets/Regionals2026_2.jpg",
    "assets/Regionals2026_3.jpg",
    "assets/Regionals2026_4.jpg",
    "assets/Regionals2026_5.jpg",
    "assets/Regionals2026_6.jpg",
    "assets/Regionals2026_7.jpg",
    "assets/Regionals2026_8.jpg",
    "assets/State2025_1.jpg",
    "assets/State2025_3.jpg",
    "assets/State2025_4.jpg",
    "assets/State2025_5.jpg"
]

const photoContainer =document.getElementById("carouselStacked");

// Remove the three existing placeholders.
photoContainer.replaceChildren();
photos.forEach((filename, index) => {
    const slide =document.createElement("div");
    slide.className = "carousel-item";

    if (index === 0) {
        slide.classList.add("active");
    }

    const image = document.createElement("img");
    image.src = filename;
    image.alt = "FBLA chapter photl";
    image.className = "d-block w-100 rounded-5";

    slide.appendChild(image);
    photoContainer.appendChild(slide);
});