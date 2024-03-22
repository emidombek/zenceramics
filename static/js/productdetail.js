document.addEventListener('DOMContentLoaded', function () {
  // Attach event listeners to "View Details" buttons as soon as the DOM is fully loaded
  attachEventListeners();
});

function attachEventListeners() {
  // Select all "View Details" buttons on the page
  let viewDetailsButtons = document.querySelectorAll('.viewDetailsButton');

  // Iterate over each button and attach an event listener
  viewDetailsButtons.forEach(function (button) {
    button.addEventListener('click', function (event) {
      // Prevent the default action
      event.preventDefault();

      // Retrieve the product ID from the button's data attribute
      let productId = this.dataset.productId;

      // Fetch and display the product details modal using the retrieved product ID
      fetchProductDetails(productId);
    });
  });
}

function fetchProductDetails(productId) {
  fetch(`/products/product-details/${productId}/`)
    .then(response => {
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      return response.json();
    })
    .then(data => {
      console.log('AJAX request successful. Response:', data);

      // Update and show the modal with the fetched product details
      updateAndShowModal(data);
    })
    .catch(error => {
      console.error('Fetch error:', error);
    });
}

function updateAndShowModal(data) {
  let modalProductName = document.getElementById('modalProductName');
  let modalProductImage = document.getElementById('modalProductImage');
  let modalProductDescription = document.getElementById('modalProductDescription');
  let modalProductPrice = document.getElementById('modalProductPrice');

  if (modalProductName && modalProductImage && modalProductDescription && modalProductPrice) {
    modalProductName.textContent = data.name;
    modalProductImage.src = data.image || '/path/to/default/image.jpg';
    modalProductDescription.textContent = data.description;
    modalProductPrice.textContent = `Price: $${data.price}`;

    // Assuming you're using Bootstrap for the modal
    $('#productDetailsModal').modal('show');
  } else {
    console.error('One or more modal elements not found.');
  }
}