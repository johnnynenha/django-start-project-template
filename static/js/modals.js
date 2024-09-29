document.addEventListener("alpine:init", () => {
  Alpine.data("modal", () => ({
    modal: null,
    init() {
      this.modal = bootstrap.Modal.getOrCreateInstance(this.$el);

      this.$el.addEventListener("hidden.bs.modal", () => {
        this.modal.dispose();
        this.modal = null;
        this.$el.remove();
      });

      this.modal.show();
    },
  }));
});
