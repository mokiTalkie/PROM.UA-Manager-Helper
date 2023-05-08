const product = $('#gen-product');
const category = $('#gen-category');
const userInput = $('#user-input');
const tagOut = $('#tag-output');
const descOut = $("#description-output");
const copyTags = $('.copy-tags');
const copyDesc = $('.copy-desc');

$(document).ready(function () {
  $(product).click(function (e) {
    e.preventDefault();
    $(this).addClass('disabled button-loading');
    $.ajax({
      type: 'POST',
      url: 'product',
      data: { 'input': userInput.val() },
      dataType: 'text',
      success: function (response) {
        $(this).removeClass('button-loading disabled');
        const JSONObj = JSON.parse(response);
        tagOut.val(JSONObj.tags);
        descOut.val(JSONObj.description);
      }.bind(this)
    });
  });

  $(category).click(function (e) {
    e.preventDefault();
    $.ajax({
      type: 'POST',
      url: 'category',
      data: { 'input': userInput.val() },
      dataType: 'text',
      success: function (response) {
        const JSONObj = JSON.parse(response);
        tagOut.val(JSONObj.tags);
        descOut.val(JSONObj.description);
      }
    });
  });

  function copyText(btn, text) {
    if (text !== '') {
      const $temp = $("<textarea>");
      $("body").append($temp);
      $temp.val(text).select();
      document.execCommand("copy");
      $temp.remove();
      $(btn).text("Copied")
        .css("background-color", "#28a745")
        .prop("disabled", true);
        
      setTimeout(function () {
        $(btn).text("Copy")
          .css("background-color", "#4e5d6c")
          .prop("disabled", false);
      }, 2000);
    } else {
      alert("Область із вихідним текстом порожня.");
    }
  }

  $(copyTags).click(function () {
    copyText(this, tagOut.val());
  });

  $(copyDesc).click(() => {
    copyText(copyDesc, descOut.val());
  });
});
