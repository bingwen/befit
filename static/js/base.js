$(document).ready(function(){
    if($('.error').html() != ''){
        showError($('.error').html());
    }
});

var showError = function (errorString) {
    $('.error').html(errorString)
    $('.error').slideDown(1000);
    setTimeout(function(){$('.error').slideUp(1000);},3000);
};