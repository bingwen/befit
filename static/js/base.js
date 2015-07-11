$(document).ready(function(){
    if($('.error center').html().replace(/(^\s*)|(\s*$)/g, "").length !=0){
        showError($('.error').html());
    }
});

var showError = function (errorString) {
    $('.error').html(errorString)
    $('.error').slideDown(1000);
    setTimeout(function(){$('.error').slideUp(1000);},3000);
};