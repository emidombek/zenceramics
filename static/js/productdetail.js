document.addEventListener('DOMContentLoaded', function () {
  // Select all "View Details" buttons
  let viewDetailsButtons = document.querySelectorAll('.viewDetailsButton');

  // Iterate over each button and attach an event listener
  viewDetailsButtons.forEach(function (button) {
    button.addEventListener('click', function (event) {
      // Prevent the default action of the button
      event.preventDefault();

      // Retrieve the product ID from the button's data attribute
      let productId = this.dataset.productId;

      // Make an AJAX request to fetch product details based on the product ID
      fetch(`/products/product-details/${productId}/`)
        .then(response => {
          if (!response.ok) {
            throw new Error('Network response was not ok');
          }
          return response.json();
        })
        .then(data => {
          console.log('AJAX request successful. Response:', data);

          // Update the modal with fetched product details
          let modalProductName = document.getElementById('modalProductName');
          let modalProductImage = document.getElementById('modalProductImage');
          let modalProductDescription = document.getElementById('modalProductDescription');
          let modalProductPrice = document.getElementById('modalProductPrice');

          if (modalProductName && modalProductImage && modalProductDescription && modalProductPrice) {
            modalProductName.textContent = data.name;
            modalProductImage.src = data.image || '/path/to/default/image.jpg';
            modalProductDescription.textContent = data.description;
            modalProductPrice.textContent = `Price: $${data.price}`;

            // Show the modal
            $('#productDetailsModal').modal('show');
          } else {
            console.error('One or more modal elements not found.');
          }
        })
        .catch(error => {
          console.error('Fetch error:', error);
        });
    });
  });
});