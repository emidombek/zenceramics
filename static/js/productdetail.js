function showProductDetails(button) {
  // Extract product details from data attributes
  const name = button.getAttribute('data-name');
  console.log('Name:', name); // Check if the name is correctly retrieved

  const image = button.getAttribute('data-image');
  console.log('Image:', image); // Check if the image URL is correctly retrieved

  const description = button.getAttribute('data-description');
  console.log('Description:', description); // Check if the description is correctly retrieved

  const price = button.getAttribute('data-price');
  console.log('Price:', price); // Check if the price is correctly retrieved

  // Check if elements exist before attempting to set their properties
  console.log('modalProductName element:', document.getElementById('modalProductName'));
  console.log('modalProductImage element:', document.getElementById('modalProductImage'));
  console.log('modalProductDescription element:', document.getElementById('modalProductDescription'));
  console.log('modalProductPrice element:', document.getElementById('modalProductPrice'));

  // Populate modal with product details
  if (document.getElementById('modalProductName')) {
    document.getElementById('modalProductName').textContent = name;
  } else {
    console.error('modalProductName element not found');
  }

  if (document.getElementById('modalProductImage')) {
    document.getElementById('modalProductImage').src = image || '{% static "/images/placeholder.png" %}'; // Fallback image
  } else {
    console.error('modalProductImage element not found');
  }

  if (document.getElementById('modalProductDescription')) {
    document.getElementById('modalProductDescription').textContent = description;
  } else {
    console.error('modalProductDescription element not found');
  }

  if (document.getElementById('modalProductPrice')) {
    document.getElementById('modalProductPrice').textContent = `Price: $${price}`;
  } else {
    console.error('modalProductPrice element not found');
  }

  // Show the modal
  var productDetailsModal = new bootstrap.Modal(document.getElementById('productDetailsModal'), {});
  productDetailsModal.show();
}