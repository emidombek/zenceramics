document.querySelectorAll('.view-more-btn').forEach(button => {
  button.addEventListener('click', function () {
    const productId = this.getAttribute('data-product-id');
    fetch(`/product-details/${productId}/`) // Update the URL pattern as needed
      .then(response => response.json())
      .then(data => {
        // Populate the modal with the fetched data
        document.getElementById('modalProductName').textContent = data.name;
        document.getElementById('modalProductImage').src = data.image || '/path/to/default/image'; // Provide a fallback image path
        document.getElementById('modalProductDescription').textContent = data.description;
        document.getElementById('modalProductPrice').textContent = `Price: $${data.price}`;

        // Show the modal
        var productDetailsModal = new bootstrap.Modal(document.getElementById('productDetailsModal'), {});
        productDetailsModal.show();
      })
      .catch(error => console.error('Error fetching product details:', error));
  });
});