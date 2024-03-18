document.addEventListener('DOMContentLoaded', function () {
  document.querySelectorAll('.view-more-btn').forEach(button => {
    button.addEventListener('click', function () {
      const productId = this.getAttribute('data-product-id');
      fetch(`/product-details/${productId}/`)
        .then(response => {
          if (!response.ok) {
            throw new Error('Network response was not ok');
          }
          return response.json();
        })
        .then(data => {
          document.getElementById('modalProductName').textContent = data.name;
          document.getElementById('modalProductImage').src = data.image || '/path/to/fallback/image.png'; // Provide a fallback image path
          document.getElementById('modalProductDescription').textContent = data.description;
          document.getElementById('modalProductPrice').textContent = `Price: $${data.price}`;

          // Show the modal
          var productDetailsModal = new bootstrap.Modal(document.getElementById('productDetailsModal'));
          productDetailsModal.show();
        })
        .catch(error => console.error('Error:', error));
    });
  });
});