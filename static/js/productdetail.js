document.addEventListener('DOMContentLoaded', function () {
  // Attach event listener to all "View Details" buttons
  let viewDetailsButtons = document.querySelectorAll('.viewDetailsButton');
  viewDetailsButtons.forEach(function (button) {
    button.addEventListener('click', function () {
      // Prevent the default action of the button
      event.preventDefault();

      // Retrieve the product ID from the button's data attribute
      let productId = this.dataset.productId;

      // Make AJAX request to fetch product details
      fetch(`/products/product-details/${productId}/`)
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