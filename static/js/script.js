// Assigning jQuery objects to variables for convenience
const product = $('#gen-product');
const category = $('#gen-category');
const userInput = $('#user-input');
const tagOut = $('#tag-output');
const descOut = $("#description-output");
const copyTags = $('.copy-tags');
const copyDesc = $('.copy-desc');
const preloader = $('.preloader');

$(preloader).hide();

// When the document is ready
$(document).ready(function () {
  // When the 'product' button is clicked
  $(product).click(function (e) {
    e.preventDefault();
    $(preloader).show();
    // Send a POST request to the 'product' URL with the input value
    $.ajax({
      type: 'POST',
      url: 'product',
      data: { 'input': userInput.val() },
      dataType: 'text',
      // On success, remove the 'disabled' and 'button-loading' classes from the button
      // Parse the response as a JSON object, and set the values of the tagOut and descOut variables
      success: function (response) {
        $(preloader).hide();
        const JSONObj = JSON.parse(response);
        tagOut.val(JSONObj.tags);
        descOut.val(JSONObj.description);
      }.bind(this)
    });
  });

  // When the 'category' button is clicked
  $(category).click(function (e) {
    e.preventDefault();
    $(preloader).show();
    // Send a POST request to the 'category' URL with the input value
    // Add 'disabled' and 'button-loading' classes to the button
    $.ajax({
      type: 'POST',
      url: 'category',
      data: { 'input': userInput.val() },
      dataType: 'text',
      // On success, remove the 'disabled' and 'button-loading' classes from the button
      // On success, parse the response as a JSON object, and set the values of the tagOut and descOut variables
      success: function (response) {
        $(preloader).hide();
        const JSONObj = JSON.parse(response);
        tagOut.val(JSONObj.tags);
        descOut.val(JSONObj.description);
      }
    });
  });

  // Define a function to copy text to the clipboard
  function copyText(btn, text) {
    // If the text is not empty, create a temporary textarea, set its value to the text,
    // select the contents of the textarea, copy the contents to the clipboard,
    // and update the button text and styling
    if (text !== '') {
      const $temp = $("<textarea>");
      $("body").append($temp);
      $temp.val(text).select();
      document.execCommand("copy");
      $temp.remove();
      $(btn).text("Copied")
        .css("background-color", "#28a745")
        .prop("disabled", true);
        
      // Reset the button text and styling after 2 seconds
      setTimeout(function () {
        $(btn).text("Copy")
          .css("background-color", "#4e5d6c")
          .prop("disabled", false);
      }, 2000);
    } else {
      // If the text is empty, show an alert message
      alert("Область із вихідним текстом порожня.");
    }
  }

  // When the 'copy tags' button is clicked, call the copyText function with the tagOut value and the button element
  $(copyTags).click(function () {
    copyText(this, tagOut.val());
  });

  // When the 'copy description' button is clicked, call the copyText function with the descOut value and the button element
  $(copyDesc).click(() => {
    copyText(copyDesc, descOut.val());
  });
});
