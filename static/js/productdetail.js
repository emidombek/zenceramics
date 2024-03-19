document.addEventListener('DOMContentLoaded', function () {
  // This function will run when the DOM is fully loaded

  // Attach event listener to the "View Details" button
  var viewDetailsButton = document.getElementById('viewDetailsButton');
  if (viewDetailsButton) {
    viewDetailsButton.addEventListener('click', function () {
      showProductDetails(this);
    });
  }

  // Define the showProductDetails function
  function showProductDetails(button) {
    console.log('showProductDetails function called');

    // Retrieve the product details from the button's data attributes
    var productId = button.dataset.productId;
    var productName = button.dataset.name;
    var productImage = button.dataset.image;
    var productDescription = button.dataset.description;
    var productPrice = button.dataset.price;

    // Log the retrieved product details
    console.log('Product ID:', productId);
    console.log('Product Name:', productName);
    console.log('Product Image:', productImage);
    console.log('Product Description:', productDescription);
    console.log('Product Price:', productPrice);

    // Make AJAX request to fetch product details
    $.ajax({
      url: `/get-product-details/${productId}/`, // The URL to your Django view
      type: 'GET',
      dataType: 'json', // Expecting JSON data in response
      success: function (data) {
        console.log('AJAX request successful. Response:', data);

        // Update modal with fetched product details
        $('#modalProductName').text(data.name || productName);
        $('#modalProductImage').attr('src', data.image || productImage || '/path/to/default/image.jpg');
        $('#modalProductDescription').text(data.description || productDescription);
        $('#modalProductPrice').text(`Price: $${data.price || productPrice}`);

        // Show the modal
        $('#productDetailsModal').modal('show');
      },
      error: function (xhr, status, error) {
        console.error('Error fetching product details:', error);
        // Here, you might want to inform the user that the request failed
      }
    });
  }
});