(function () {
    var locations = window.FISHTECH_LOCATIONS || [];
    var fishCollectionUrl = window.FISHTECH_FISH_COLLECTION_URL || '/fish-collection';

    var defaultCenter = [39.5501, -105.7821]; // Colorado
    var map = L.map('map').setView(defaultCenter, 7);

    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        maxZoom: 18,
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(map);

    var nameEl = document.getElementById('location-name');
    var typeEl = document.getElementById('location-type');
    var descriptionEl = document.getElementById('location-description');
    var fishListEl = document.getElementById('location-fish-list');

    function clearFishList() {
        fishListEl.textContent = '';
    }

    function showFishListMessage(message) {
        clearFishList();
        var li = document.createElement('li');
        li.className = 'empty-state';
        li.textContent = message;
        fishListEl.appendChild(li);
    }

    function renderFishList(fish) {
        clearFishList();

        if (!fish || fish.length === 0) {
            showFishListMessage('No fish recorded for this location yet.');
            return;
        }

        fish.forEach(function (f) {
            var li = document.createElement('li');
            var link = document.createElement('a');
            link.href = fishCollectionUrl + '#fish-' + f.id;
            link.textContent = f.name;
            li.appendChild(link);
            fishListEl.appendChild(li);
        });
    }

    function selectLocation(location) {
        nameEl.textContent = location.name || 'Unknown';
        typeEl.textContent = location.type || 'Unknown';
        descriptionEl.textContent = location.description || '';

        showFishListMessage('Loading fish...');

        fetch('/api/waterbody/' + location.id + '/fish')
            .then(function (response) {
                if (!response.ok) {
                    throw new Error('Request failed');
                }
                return response.json();
            })
            .then(renderFishList)
            .catch(function () {
                showFishListMessage('Could not load fish for this location.');
            });
    }

    if (locations.length === 0) {
        showFishListMessage('No location found');
    } else {
        var bounds = [];

        locations.forEach(function (location) {
            if (location.lat == null || location.lng == null) {
                return;
            }

            var marker = L.marker([location.lat, location.lng]).addTo(map);
            marker.bindPopup(location.name || 'Water body');
            marker.on('click', function () {
                selectLocation(location);
            });

            bounds.push([location.lat, location.lng]);
        });

        if (bounds.length > 0) {
            map.fitBounds(bounds, { padding: [40, 40], maxZoom: 10 });
        }
    }
})();
