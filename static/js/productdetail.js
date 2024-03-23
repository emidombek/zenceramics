document.addEventListener('DOMContentLoaded', function () {
  console.log('DOM fully loaded and parsed');
  bindViewDetailsButtons();
});

function bindViewDetailsButtons() {
  const buttons = document.querySelectorAll('.viewDetailsButton');
  console.log(`Found ${buttons.length} '.viewDetailsButton' elements`);

  buttons.forEach(button => {
    button.addEventListener('click', function (event) {
      event.preventDefault(); // Prevent the default action

      // Retrieve product details from data attributes
      let productId = this.getAttribute('data-product-id');
      let productName = this.getAttribute('data-name');
      let productImage = this.getAttribute('data-image');
      let productDescription = this.getAttribute('data-description');
      let productPrice = this.getAttribute('data-price');

      // Log each attribute to ensure they are correctly retrieved
      console.log('Button clicked. Product Details:', {
        ProductID: productId,
        ProductName: productName,
        ProductImage: productImage,
        ProductDescription: productDescription,
        ProductPrice: productPrice
      });

      // Populate and show the modal
      populateAndShowModal(productId, productName, productImage, productDescription, productPrice);
    });
  });
} // This closing brace matches the opening brace of the function bindViewDetailsButtons

function populateAndShowModal(productId, name, image, description, price) {
  console.log('Initializing modal for Product ID:', productId);

  const modalElement = document.getElementById('productDetailsModal');
  if (modalElement) {
    console.log('Modal element found:', modalElement);
    const modalOptions = {
      backdrop: 'static',
      keyboard: true,
      focus: true
    };

    document.getElementById('modalProductName').textContent = name;
    document.getElementById('modalProductImage').src = image || '/path/to/default/image.jpg';
    document.getElementById('modalProductDescription').textContent = description;
    document.getElementById('modalProductPrice').textContent = `Price: $${price}`;

    const addToCartButton = document.getElementById('modalAddToCartButton');
    addToCartButton.href = `cart/add/<int:product_id>/`;

    const productDetailsModal = new bootstrap.Modal(modalElement, modalOptions);
    productDetailsModal.show();
  } else {
    console.log('Error: Modal element not found');
  }
}