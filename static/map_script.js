// Setting globals
const markerEls = document.querySelectorAll('.marker');

for (let deleteButton of deleteButtonsEl) {
  deleteButton.addEventListener('click', hideEvent);
}