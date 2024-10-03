function renderImage(imageElementId, event) {
  const imageElement = document.getElementById(imageElementId);

  if (!imageElement || event.files.length != 1) return;

  let url = URL.createObjectURL(event.files[0]);
  imageElement.src = url;
}

function renderText(textElementId, event) {
  const textElement = document.getElementById(textElementId);
  textElement.innerHTML = event.value;
}
