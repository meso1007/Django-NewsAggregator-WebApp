let nextDom = document.getElementById("next");
let prevDom = document.getElementById("prev");
let carouseDom = document.querySelector(".carousel");
let listItemDom = document.querySelector(".carousel .list");
let thumbnailDom = document.querySelector(".carousel .thumbnail");
let startX;

nextDom.onclick = () => {
  showSlider("next");
};
prevDom.onclick = () => {
  showSlider("prev");
};

// for mobile

carouseDom.addEventListener("touchstart", (event) => {
  startX = event.touches[0].clientX;
});

carouseDom.addEventListener("touchmove", (event) => {
  event.preventDefault();
});

carouseDom.addEventListener("touchend", (event) => {
  let endX = event.changedTouches[0].clientX;
  handleSwipe(startX, endX);
});

function handleSwipe(startX, endX) {
  let swipeDistance = startX - endX;

  if (swipeDistance > 50) {
    nextDom.click();
  } else if (swipeDistance < -50) {
    prevDom.click();
  }
}

// for keyboard
document.addEventListener("keydown", (event) => {
  if (event.key === "ArrowRight") {
    nextDom.click();
  } else if (event.key === "ArrowLeft") {
    prevDom.click();
  }
});

// auto changing
let timeRunning = 3000;
let timeAutoNext = 7000;
let runTimeOut;
let runAutoRun = setTimeout(() => {
  nextDom.click();
}, timeAutoNext);

function showSlider(type) {
  let itemSlider = document.querySelectorAll(".carousel .list .item");
  let itemThumbnail = document.querySelectorAll(".carousel .thumbnail .item");

  if (type === "next") {
    listItemDom.appendChild(itemSlider[0]);
    thumbnailDom.appendChild(itemThumbnail[0]);
    carouseDom.classList.add("next");
  } else {
    let positionLastItem = itemSlider.length - 1;
    listItemDom.prepend(itemSlider[positionLastItem]);
    thumbnailDom.prepend(itemThumbnail[positionLastItem]);
    carouseDom.classList.add("prev");
  }

  clearTimeout(runTimeOut);
  runTimeOut = setTimeout(() => {
    carouseDom.classList.remove("next");
    carouseDom.classList.remove("prev");
  }, timeRunning);

  clearTimeout(runAutoRun);
  runAutoRun = setTimeout(() => {
    nextDom.click();
  }, timeAutoNext);
}
document.addEventListener("DOMContentLoaded", function () {
  console.log("DOMContentLoaded event fired"); // ここで確認
  const timeContainer = document.getElementById("current-time");

  if (!timeContainer) {
    console.error("Element with id 'current-time' not found");
    return;
  }

  function updateTime() {
    function updateTime() {
      const now = new Date();

      // Get the date components
      const year = now.getFullYear();
      const month = (now.getMonth() + 1).toString().padStart(2, "0"); // Months are zero-based
      const day = now.getDate().toString().padStart(2, "0");

      // Get the time components
      const hours = now.getHours().toString().padStart(2, "0");
      const minutes = now.getMinutes().toString().padStart(2, "0");
      const seconds = now.getSeconds().toString().padStart(2, "0");

      // Combine date and time
      const formattedDate = `${year}-${month}-${day}`;
      const formattedTime = `${hours}:${minutes}:${seconds}`;

      // Set the date and time inside the container
      const timeContainer = document.getElementById("current-time");
      timeContainer.textContent = `${formattedDate} ${formattedTime}`;
      console.log("hi");
    }

    // Call updateTime once initially
    updateTime();

    // Update time every second
    setInterval(updateTime, 1000);
  }

  // Call updateTime once initially
  updateTime();

  // Update time every second
  setInterval(updateTime, 1000);
});
