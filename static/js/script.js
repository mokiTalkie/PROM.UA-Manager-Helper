const product = $('#gen-product');
const category = $('#gen-category');
const user_input = $('#user-input');
const tag_out = $('#tag-output')
const desc_out = $("#description-output")


$(product).click(function(e) {
  e.preventDefault();
  
  $.ajax({
    type: 'POST',
    url: 'product',
    data: { 'input': $(user_input).val() },
    dataType: 'text',
    success: function(response) {
      var JSONObj = JSON.parse(response)
      $(tag_out).val(JSONObj.tags)
      $(desc_out).val(JSONObj.description);
    }
  });
});
