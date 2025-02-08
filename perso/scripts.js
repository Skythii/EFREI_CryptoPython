// Initialiser la carte
const map = L.map('carte').setView([48.8566, 2.3522], 5);  // Par défaut, centré sur Paris avec un zoom de 5

// Ajouter un fond de carte (tuiles)
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
  attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

// Liste des destinations (tu peux ajouter plus de destinations avec leurs informations)
const destinations = [
  {
    nom: "Paris",
    description: "La capitale de la France, célèbre pour la Tour Eiffel et ses musées.",
    latitude: 48.8566,
    longitude: 2.3522,
    image: "https://via.placeholder.com/400x300?text=Paris"
  },
  {
    nom: "Londres",
    description: "La capitale du Royaume-Uni, connue pour le Big Ben et Buckingham Palace.",
    latitude: 51.5074,
    longitude: -0.1278,
    image: "https://via.placeholder.com/400x300?text=Londres"
  },
  {
    nom: "Tokyo",
    description: "Capitale du Japon, une ville moderne mêlant tradition et technologie.",
    latitude: 35.6762,
    longitude: 139.6503,
    image: "https://via.placeholder.com/400x300?text=Tokyo"
  }
];

// Fonction pour afficher les infos d'une destination
function afficherInfos(destination) {
  document.getElementById("titreDestination").textContent = destination.nom;
  document.getElementById("descriptionDestination").textContent = destination.description;
  document.getElementById("imageDestination").src = destination.image;
}

// Placer les épingles sur la carte et lier chaque destination à son info
destinations.forEach(destination => {
  const marker = L.marker([destination.latitude, destination.longitude]).addTo(map);
  
  marker.on('click', function() {
    afficherInfos(destination);
  });
});
