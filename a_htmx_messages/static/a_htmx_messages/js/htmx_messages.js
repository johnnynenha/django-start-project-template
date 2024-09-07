document.addEventListener("alpine:init", () => {
  Alpine.data("htmx_messages", () => ({
    black_button: ["text-bg-warning", "text-bg-light"],
    toast_options: {
      delay: 3000,
    },
    register(element) {
      let toastClassList = Array.from(element.classList);

      if (
        this.black_button.filter((item) => toastClassList.includes(item))
          .length > 0
      ) {
        element
          .querySelector("button.btn-close")
          .classList.remove("btn-close-white");
      }

      const toast = new bootstrap.Toast(element, this.toast_options);

      element.addEventListener("hidden.bs.toast", () => {
        toast.dispose();
        element.remove();
      });

      toast.show();
    },
  }));
});
