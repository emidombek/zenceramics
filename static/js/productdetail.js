document.addEventListener('DOMContentLoaded', function () {
  // This ensures the script runs after the entire page is loaded.
  bindViewDetailsButtons();
});

function bindViewDetailsButtons() {
  document.querySelectorAll('.viewDetailsButton').forEach(function (button) {
    button.addEventListener('click', function (event) {
      event.preventDefault(); // Prevent the default action

      // Retrieve product details from data attributes
      let productId = this.getAttribute('data-product-id');
      let productName = this.getAttribute('data-name');
      let productImage = this.getAttribute('data-image');
      let productDescription = this.getAttribute('data-description');
      let productPrice = this.getAttribute('data-price');

      // Populate and show the modal
      populateAndShowModal(productId, productName, productImage, productDescription, productPrice);
    });
  });
}

function populateAndShowModal(productId, name, image, description, price) {
  // Populate modal content
  document.getElementById('modalProductName').textContent = name;
  document.getElementById('modalProductImage').src = image || '/path/to/default/image.jpg';
  document.getElementById('modalProductDescription').textContent = description;
  document.getElementById('modalProductPrice').textContent = `Price: $${price}`;

  // Show the modal using Bootstrap 5's native JavaScript API with explicit options
  const modalElement = document.getElementById('productDetailsModal');
  const modalOptions = {
    backdrop: 'static',
    keyboard: true,
    focus: true
  };
  const productDetailsModal = new bootstrap.Modal(modalElement, modalOptions);
  productDetailsModal.show();
}