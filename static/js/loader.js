(function () {
  const loader = document.getElementById("loader");

  window.addEventListener("load", () => {
    loader.classList.add("opacity-0");
    loader.classList.add("invisible");

    loader.addEventListener("transitionend", () => {
      document.body.removeChild(loader);
    });
  });
})();
