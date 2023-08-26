// Setting globals
const markerEls = document.querySelectorAll('.popup');

for (let markerEl of markerEls) {
  markerEl.addEventListener('click', hideEvent);
}

async function hideEvent(marker) {
  marker.classList.add('hidden');
  console.log(f`MARKER ${marker} CLICKED`);
}

function link_hub(id) {
  window.location.href = "/hub_info?hub=" + id;
}