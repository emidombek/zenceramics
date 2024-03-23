$(function () {
  // Attach event listeners to "View Details" buttons as soon as the DOM is fully loaded
  $('.viewDetailsButton').each(function () {
    $(this).on('click', function (event) {
      // Prevent the default action
      event.preventDefault();

      // Retrieve the product ID from the button's data attribute
      let productId = $(this).data('productId');

      // Fetch and display the product details modal using the retrieved product ID
      fetchProductDetails(productId);
    });
  });
});

function fetchProductDetails(productId) {
  $.ajax({
    url: `/products/product-details/${productId}/`,
    type: 'GET',
    success: function (data) {
      console.log('AJAX request successful. Response:', data);
      updateAndShowModal(data);
    },
    error: function (jqXHR, textStatus, errorThrown) {
      console.error('Fetch error:', textStatus, errorThrown);
    }
  });
}

function updateAndShowModal(data) {
  // Update modal content
  $('#modalProductName').text(data.name);
  $('#modalProductImage').attr('src', data.image || '/path/to/default/image.jpg');
  $('#modalProductDescription').text(data.description);
  $('#modalProductPrice').text(`Price: $${data.price}`);

  // Show the modal using Bootstrap's modal method
  $('#productDetailsModal').modal('show');
}