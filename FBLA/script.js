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

const photoContainer = document.getElementById("carouselStacked");
photoContainer.replaceChildren();

const frames = [];
let changingPhotos = false;
let firstChange = true;

// Make three frames, each containing two overlapping images.
for (let i = 0; i < 3; i++) {
    const frame = document.createElement("div");
    frame.className = "carousel-item photo-frame";

    const layers = [];

    for (let j = 0; j < 2; j++) {
        const image = document.createElement("img");
        image.alt = "FBLA chapter photo";
        image.className = "d-block w-100 rounded-5";

        frame.appendChild(image);
        layers.push(image);
    }

    photoContainer.appendChild(frame);
    frames.push({ layers, visibleLayer: 0 });
}

async function changePhotos() {
    if (changingPhotos) return;
    changingPhotos = true;

    try {
        // Avoid immediately repeating the pictures currently showing.
        const currentSources = frames.map(
            (frame) => frame.layers[frame.visibleLayer].getAttribute("src")
        );

        const available = photos.filter(
            (filename) => !currentSources.includes(filename)
        );

        // Load the incoming pictures on the hidden layers.
        const incoming = frames.map((frame) => {
            const index = Math.floor(Math.random() * available.length);
            const filename = available.splice(index, 1)[0];
            const nextLayer = firstChange ? 0 : 1 - frame.visibleLayer;
            const image = frame.layers[nextLayer];

            image.src = filename;
            return { frame, nextLayer, image };
        });

        await Promise.all(incoming.map(({ image }) => image.decode()));

        // Let the browser paint the hidden layers before fading.
        await new Promise((resolve) => {
            requestAnimationFrame(() => requestAnimationFrame(resolve));
        });

        // Change each column at a random time, so the order is random too.
        await Promise.all(
            incoming.map(async ({ frame, nextLayer, image }) => {
                const delay = firstChange ? 0 : Math.random() * 3000;

                await new Promise((resolve) => setTimeout(resolve, delay));

                frame.layers[frame.visibleLayer].classList.remove("is-visible");
                image.classList.add("is-visible");
                frame.visibleLayer = nextLayer;

                await new Promise((resolve) => setTimeout(resolve, 1200));
            })
        );

        firstChange = false;
    } catch (error) {
        console.error("Could not load the next photos:", error);
    } finally {
        changingPhotos = false;
    }
}

// Buttons choose another random set without sliding.
document.querySelectorAll("#carouselMultiple .btn-icon")
    .forEach((button) => {
        button.removeAttribute("data-bs-slide");
        button.removeAttribute("data-bs-target");
        button.addEventListener("click", changePhotos);
    });

changePhotos();
setInterval(changePhotos, 5000);

// Chapter calendar
const calendar = new FullCalendar.Calendar(document.getElementById("calendar"), {
    initialView: "dayGridMonth",
    initialDate: "2026-10-01",
    height: "auto",
    fixedWeekCount: false,
    eventDisplay: "block",
    displayEventTime: false,
    headerToolbar: { left: "prev,next", center: "title", right: "today" },
    eventTimeFormat: { hour: "numeric", minute: "2-digit", meridiem: "short" },
    events: [
        { title: "Chapter Meeting", start: "2026-10-16T12:15:00", extendedProps: { location: "Class Connect" } },
        { title: "Chapter Meeting", start: "2026-10-23T12:15:00", extendedProps: { location: "Class Connect" } },
        { title: "Chapter Meeting", start: "2026-10-30T12:15:00", extendedProps: { location: "Class Connect" } }
    ],
    eventDidMount: (info) => {
        const time = info.event.start.toLocaleTimeString([], { hour: "numeric", minute: "2-digit" });
        info.el.title = `${info.event.title} at ${time} - ${info.event.extendedProps.location}`;
    }
});
calendar.render();