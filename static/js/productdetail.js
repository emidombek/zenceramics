function showProductDetails(button) {
  // Extract product details from data attributes
  const name = button.getAttribute('data-name');
  const image = button.getAttribute('data-image');
  const description = button.getAttribute('data-description');
  const price = button.getAttribute('data-price');

  // Populate modal with product details
  document.getElementById('modalProductName').textContent = name;
  document.getElementById('modalProductImage').src = image || '{% static "/images/placeholder.png" %}'; // Fallback image
  document.getElementById('modalProductDescription').textContent = description;
  document.getElementById('modalProductPrice').textContent = `Price: $${price}`;

  // Show the modal
  var productDetailsModal = new bootstrap.Modal(document.getElementById('productDetailsModal'), {});
  productDetailsModal.show();
}