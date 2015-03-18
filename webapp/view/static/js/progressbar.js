var timedIncrease;

function conditionedIncrease() {
    var value = Number($('.progress-bar').attr('aria-valuenow'));
    if (value < 100) {
        increaseBar(35)
    } else {
        $('#button-next').css({opacity: 1});
        $('#button-progress').hide();
        $('#progress-bar').hide();
        $('#form-progress').hide();
        clearInterval(timedIncrease)
    }
}

function increaseBar(step) {
    var value = Number($('.progress-bar').attr('aria-valuenow'));
    var max = Number($('.progress-bar').attr('aria-valuemax'));

    value += step;
    if (value > max) {
        value = max
    }

    $('.progress-bar').css('width', value + '%').attr('aria-valuenow', value)
}