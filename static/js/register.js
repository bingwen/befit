var sendCode = function () {
    $.getJSON('/user/signin', {
        signin_code: 'get_code'
    }, function (result) {
        if (result['status'] == 'ok') {
            $('#error').html('');
        }
        else {
            $('#error').html('获取验证码错误');
        }
    });
    alert('已向您的手机发送验证码（并没有');
};

$('#send-code').click(sendCode);

// 裸代码可以作为一种核心注释：揭示「目的」的注释，aka「为何如此这般进行抽象」之注释。
//文字垂直居中，杭神法
//$('#send-code').css('line-height', $('#send-code').css('height'));
//// 让#mobile-box img在#mobile-box里垂直居中
//$('#mobile-box img').css('margin-top', ($('#mobile-box').height() - $('#mobile-box img').height()) / 2 + 'px');

/**
 * 文字垂直居中。
 * ……窝不知道适用范围。依赖jquery。2015-07-04 15:08:08*/
var textVerticalCentralize = function (container) {
    container.css('line-height', container.css('height'));
};

/**
 * 图片什么的垂直居中。
 * ……窝不知道适用范围。依赖jquery。2015-07-04 15:08:11*/
var elementVerticalCentralize = function (element, container) {
    element.css('margin-top', (container.height() - element.height()) / 2 + 'px');
};

textVerticalCentralize($('#send-code'));
elementVerticalCentralize($('#mobile-box img'), $('#mobile-box'));

