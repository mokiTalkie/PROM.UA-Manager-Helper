// Assigning jQuery objects to variables for convenience
const product = $('#gen-product');
const category = $('#gen-category');
const userInput = $('#user-input');
const tagOut = $('#tag-output');
const descOut = $("#description-output");
const copyTags = $('.copy-tags');
const copyDesc = $('.copy-desc');
const preloader = $('.preloader');
const repeatProductTag = $('#repeat-product-queries')
const repeatProductDesc = $('#repeat-product-description')
const repeatCategoryTag = $('#repeat-category-queries')
const repeatCategoryDesc = $('#repeat-category-description')

// When the document is ready
$(document).ready(function () {

  $(repeatProductTag).click(function (e) {
    e.preventDefault();
    $(preloader).show();

    $.ajax({
      type: 'POST',
      url: 'repeat',
      contentType: 'application/json',
      data: JSON.stringify({ 'input': userInput.val(), 'target': 'product_tags' }),
      success: function (response) {
        $(preloader).hide();
        tagOut.val(response.text)
      }
    });
  });
  $(repeatProductDesc).click(function (e) {
    e.preventDefault();
    $(preloader).show();

    $.ajax({
      type: 'POST',
      url: 'repeat',
      contentType: 'application/json',
      data: JSON.stringify({ 'input': userInput.val(), 'target': 'product_description' }),
      success: function (response) {
        $(preloader).hide();
        descOut.val(response.text)
      }
    });
  });
  $(repeatCategoryTag).click(function (e) {
    e.preventDefault();
    $(preloader).show();

    $.ajax({
      type: 'POST',
      url: 'repeat',
      contentType: 'application/json',
      data: JSON.stringify({ 'input': userInput.val(), 'target': 'category_tags' }),
      success: function (response) {
        $(preloader).hide();
        tagOut.val(response.text)
      }
    });
  });
  $(repeatCategoryDesc).click(function (e) {
    e.preventDefault();
    $(preloader).show();

    $.ajax({
      type: 'POST',
      url: 'repeat',
      contentType: 'application/json',
      data: JSON.stringify({ 'input': userInput.val(), 'target': 'category_description' }),
      success: function (response) {
        $(preloader).hide();
        descOut.val(response.text)
      }
    });
  });
  // When the 'product' button is clicked
  $(product).click(function (e) {
    e.preventDefault();
    $(preloader).show();
    // Send a POST request to the 'product' URL with the input value
    $.ajax({
      type: 'POST',
      url: 'product',
      contentType: 'application/json',
      data: JSON.stringify({ 'input': userInput.val() }),
      // On success, remove the 'disabled' and 'button-loading' classes from the button
      // Parse the response as a JSON object, and set the values of the tagOut and descOut variables
      success: function (response) {
        $(preloader).hide();
        tagOut.val(response.tags);
        descOut.val(response.description);
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
      contentType: 'application/json',
      data: JSON.stringify({ 'input': userInput.val() }),
      // On success, remove the 'disabled' and 'button-loading' classes from the button
      // On success, parse the response as a JSON object, and set the values of the tagOut and descOut variables
      success: function (response) {
        $(preloader).hide();
        tagOut.val(response.tags);
        descOut.val(response.description);
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
      $(btn).text("Скопійовано")
        .css("background-color", "#5a5a5a")
        .prop("disabled", true);

      // Reset the button text and styling after 2 seconds
      setTimeout(function () {
        $(btn).text("Копіювати")
          .css("background-color", "#5bc0de")
          .prop("disabled", false);
      }, 1000);
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
