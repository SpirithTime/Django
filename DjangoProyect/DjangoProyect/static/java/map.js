document.addEventListener('DOMContentLoaded', (event) => {
    const map = L.map('map').setView([-45.459908, -72.814236], 20);

    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(map);

    var locations = JSON.parse(document.getElementById('map').dataset.locations);
    locations.forEach(function(location) {
        L.marker([location.lat, location.lng]).addTo(map)
            .bindPopup(location.popup);
    });


    const marker = L.marker([-45.459908, -72.814236]).addTo(map);

    map.setView(marker.getLatLng(), 20);
});