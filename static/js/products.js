$(document).ready(function() {
    // Event listener for the checkboxes
    $("#c-checkbox input[type='checkbox']").change(function() {
      // Get the selected categories
      var selectedCategories = [];
      $("#c-checkbox  input[type='checkbox']:checked").each(function() {
        selectedCategories.push($(this).val());
      });
  
      // Send an AJAX request to the server
      $.ajax({
        url: "products/",
        type: "POST",
        data: { categories: selectedCategories },
        success: function(response) {
          // Update the content with the updated content from the server
          $("#content").html(response);
        }
      });
    });
  });