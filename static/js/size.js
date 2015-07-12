/**
 * Created by sonion on 15/5/21.
 */

//// TODO 适配不同平台时测试用
//$('#submit').on('click', function () {
//    alert('user-agent: ' + navigator.userAgent)
//});

//测试 点微信浏览器的返回 回到该页的时候 js 是否会跑一遍
alert('document.referrer: |'+document.referrer+'|');
//alert('user-agent: ' + navigator.userAgent);

var measureList = [
    {
        name: "身高",
        unit: "cm",
        min: 0,
        max: 190
    },
    {
        name: "胸围",
        unit: "cm",
        min: 0,
        max: 140
    },
    {
        name: "颈围",
        unit: "cm",
        min: 0,
        max: 50
    },
    {
        name: "臀围",
        unit: "cm",
        min: 0,
        max: 140
    },
    {
        name: "腰围",
        unit: "cm",
        min: 0,
        max: 140
    },
    {
        name: "大腿围",
        unit: "cm",
        min: 0,
        max: 70
    },
    {
        name: "上臂围",
        unit: "cm",
        min: 0,
        max: 40
    },
    {
        name: "臂长",
        unit: "cm",
        min: 0,
        max: 80
    },
    {
        name: "腿长",
        unit: "cm",
        min: 0,
        max: 120
    },
    {
        name: "肩宽",
        unit: "cm",
        min: 0,
        max: 60
    }
];

/** 逻辑初始化代码。应该在UI初始化之前。*/

// 尺子设置为 身高；min max val 在 changeItem() 中设置。
$('#slider-input').data('current-item-id', 0);

/** end of 逻辑初始化代码。*/


/**  UI 初始化代码 */

// 设完值，刷一下。
changeItem('神秘来源', 0);

// 让选项描述垂直居中
$('.option-description').css('line-height', $('.option-description').height() + 'px');

// 让选项按钮的宽度等于高度。不过现在（2015-06-21 00:28:49）写死了尺寸，所以不需要
//$('.option-touchable').width($('.option-touchable').height());

// 让选项按钮垂直居中。100px 是选项按钮写死的边长。
$('.option-touchable').css('margin-top', ($('.option').height() - 100) / 2 + 'px');

// 设置按钮初始背景图；设置小描述的值 TODO 怎样更函数式地使用jquery？
var _xs = [500, 500, 400, 400, 300, 300, 200, 200, 100, 100];
var _ys = [300, 100, 300, 100, 300, 100, 300, 100, 300, 100]; // + 100 if selected
for (var i = 0; i < 10; i++) {
    var currentItemId = $('#slider-input').data('current-item-id');
    var selected = 0;
    var button = $('.option-touchable[data-item-id=' + i + ']');
    button.css('background-position', _xs[i] + 'px ' + (_ys[i] + (i === currentItemId ? 100 : 0)) + 'px');
    var desc = $('.option-description[data-item-id=' + i + ']');
    desc.css('color', (i === currentItemId ? '#5A5A5A' : '#BEBEBE'));
    var optValBlank = $('.option-description[data-item-id=' + i + '] .option-value');
    var optVal = $('#form-of-data input[data-item-id=' + i + ']').val();
    optValBlank.html(optVal);
}

/** end of  UI 初始化代码 */


/** TODO call for bi-binding! AngularJS; can.js; etc. */
function onChangeSlider() {
    var val = $('#slider-input').val();
    var itemId = $('#slider-input').data('current-item-id');
    //实际存储区
    $('#form-of-data input[data-item-id=' + itemId + ']').val(val);
    //修改小数字
    $('.option-description[data-item-id=' + itemId + '] .option-value').html(val);
    //修改大数字
    $('#value-number').html(val);
}

/** 实时变化：从 onchange 改成 oninput 即可！via http://stackoverflow.com/questions/4911253/how-to-real-time-move-the-range-type-inputs-slider-using-javascript-without-ref */
$('#slider-input').on('input', function () {
    onChangeSlider();
});


//// closure...... binding time...(very late. --Douglas)
$('#minus-button').on('click', function () {
    //console.log('minus');
    var sliderInputDom = $('#slider-input');
    var val = parseInt(sliderInputDom.val()) - 1;
    sliderInputDom.val(val); // val() rocks! 不会越过 input 的 min 和 max 界限
    onChangeSlider(); // 级联地改变显示的值。
});
// a little not DRY
$('#plus-button').on('click', function () {
    //console.log('plus');
    var sliderInputDom = $('#slider-input');
    var val = parseInt(sliderInputDom.val()) + 1;
    sliderInputDom.val(val);
    onChangeSlider();
});

/** change measurement item
 * sourceItemId 参数实际已经无用。2015-07-07 17:09:11*/
function changeItem(sourceItemId, targetItemId) {
    console.log("change from", sourceItemId, "to", targetItemId);
    var sliderInputDom = $('#slider-input');
    var tarItem = measureList[targetItemId];
    var tarItemVal = $('#form-of-data input[data-item-id=' + targetItemId + ']').val();

    // 改尺子的属性
    sliderInputDom.attr('min', tarItem.min).attr('max', tarItem.max).val(tarItemVal).data('current-item-id', targetItemId);
    // 修改大描述
    var itemDisplay = tarItem.name + ' (' + tarItem.min + '-' + tarItem.max + ')';
    $('#current-item').html(itemDisplay);
    // 修改大数字的单位
    $('#value-unit').html(tarItem.unit);
    // 包含了：修改实际存储区、修改小数字、修改大数字
    onChangeSlider();
}

$('.option-touchable').on('click', function () {
    var src = $('#slider-input').data('current-item-id');
    var tar = $(this).data('item-id');
    changeItem(src, tar);
    refreshButton(src, 0);
    refreshButton(tar, 1);
    $('#slider-input').data('current-item-id', tar);
});

$('#submit').on('click', function () {
    $.post('/user/figure', {
        height: $("input[name='height']").val(),
        neck: $("input[name='neck']").val(),
        waist: $("input[name='waist']").val(),
        arm_length: $("input[name='arm_length']").val(),
        leg_length: $("input[name='leg_length']").val(),
        chest: $("input[name='chest']").val(),
        butt: $("input[name='butt']").val(),
        leg_width: $("input[name='leg_width']").val(),
        arm_width: $("input[name='arm_width']").val(),
        shoulder: $("input[name='shoulder']").val()
    }, function (result) {
        if (result['status'] == '200') {
            showError('保存成功', '#8FBC8F');
        }
        else {
            showError('保存出现问题，保存失败')
        }
    },"json");//getJSON
});

/** TODO 该叫 refreshButtonAndDescription 了
 * param:
 * itemId [0,9] int
 * selected [0,1] int
 * */
var refreshButton = function (itemId, selected) {
    var button = $('.option-touchable[data-item-id=' + itemId + ']');
    button.data('selected', selected);
    button.css('background-position', _xs[itemId] + 'px ' + (_ys[itemId] + button.data('selected') * 100) + 'px');
    var desc = $('.option-description[data-item-id=' + itemId + ']');
    console.log(desc);
    desc.css('color', ['#BEBEBE', '#5A5A5A'][selected]);
};

