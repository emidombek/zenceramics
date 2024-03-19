document.addEventListener('DOMContentLoaded', function () {
  // Attach event listener to all "View Details" links
  let viewDetailsLinks = document.querySelectorAll('.viewDetailsLink');
  viewDetailsLinks.forEach(function (link) {
    link.addEventListener('click', function (event) {
      event.preventDefault(); // Prevent the default action of following the link

      let productId = this.dataset.productId;

      // Make AJAX request to fetch product details
      fetch(`/product-details/${productId}/`)
        .then(response => {
          if (!response.ok) {
            throw new Error('Network response was not ok');
          }
          return response.json();
        })
        .then(data => {
          console.log('AJAX request successful. Response:', data);

          // Update modal with fetched product details
          document.getElementById('modalProductName').textContent = data.name;
          document.getElementById('modalProductImage').src = data.image || '/path/to/default/image.jpg';
          document.getElementById('modalProductDescription').textContent = data.description;
          document.getElementById('modalProductPrice').textContent = `Price: $${data.price}`;

          // Show the modal
          $('#productDetailsModal').modal('show');
        })
        .catch(error => {
          console.error('Fetch error:', error);
          // Here, you might want to inform the user that the request failed
        });
    });
  });
});