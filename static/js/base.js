$(document).ready(function(){
    if($('.error center').html().replace(/(^\s*)|(\s*$)/g, "").length !=0){
        showError($('.error').html());
    }
});

var showError = function (errorString, bg_color) {
    if(bg_color) { $('.error').css('background-color', bg_color) }
    else { $('.error').css('background-color', '#B22222') }
    $('.error center').html(errorString)
    $('.error').slideDown(1000);
    setTimeout(function(){$('.error').slideUp(1000);},3000);
};