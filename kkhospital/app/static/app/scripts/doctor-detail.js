var month = [
    'มกราคม' ,
    'กุมภาพันธ์' ,
    'มีนาคม' ,
    'เมษายน' ,
    'พฤษภาคม' ,
    'มิถุนายน' ,
    'กรกฎาคม' ,
    'สิงหาคม' ,
    'กันยายน' ,
    'ตุลาคม' ,
    'พฤศจิกายน' ,
    'ธันวาคม' ,
]
var day = [
    'วันจันทร์',
    'วันอังคาร',
    'วันพุธ',
    'วันพฤหัสบดี',
    'วันศุกร์',
    'วันเสาร์',
    'วันอาทิตย์',
]

var timestamp = new Date().getTime()
while(new Date(timestamp).getUTCDay() > 1) {
    timestamp -= (1000 * 60 * 60 * 24)
}
var start_thisWeek = new Date(timestamp);
var start_nextWeek = new Date(timestamp + (1000 * 60 * 60 * 24 * 7));
var isThisWeek = true;
var isInit = false;

function checkReservation(hour, day, month, year) {
    return new Promise(resolve => {
        $.get('/check-reservation', {hour: hour, day: day, month: month, year: year}, function(data) {
            resolve(data.free);
        });
    })
}

function getDateForDay() {
    $('.schedule .panel-title').each(function() {
        var old_text = $(this).text().replace(/[\ \n]/g, '');
        old_text = old_text.substring(0, old_text.match(/[1234567890]/) ? old_text.match(/[1234567890]/).index : old_text.length);
        var date = isThisWeek ? start_thisWeek : start_nextWeek;
        date = new Date(date.getTime() + (1000 * 60 * 60 * 24 * day.indexOf(old_text)))
        $(this).text(old_text + ' ' + new Date(date).getDate() + ' ' + month[new Date(date).getMonth()] + ' ' + new Date(date).getFullYear());

        $(this).closest('.panel').find('ul.time li').each(function() {
            (function(today, $timeButton) {
                var hour = $timeButton.text().substring(0, $timeButton.text().indexOf(':'));
                checkReservation(hour, today.getDate(), today.getMonth() + 1, today.getFullYear()).then(function(status) {
                    if (status) {
                        $timeButton.removeClass('hide');
                    } else {
                        $timeButton.addClass('hide');
                    }
                })
            })(date, $(this));
        })
    });
}

getDateForDay();

$('ul.time li').click(function() {
    $('ul.time li').removeClass('selected');
    $(this).addClass('selected');
    $('p.appointment-time').text($(this).closest('.panel').find('.panel-title').text() + ', เวลา ' + $(this).text());
    $('div.appointment-detail').removeClass('hide');

    var date_text = $(this).closest('.panel').find('.panel-title').text().split(' ');
    var time_text = $(this).text().split(' - ');
    $('input[name="date"]').val('{"year": ' + date_text[3] + ', "month": ' + (month.indexOf(date_text[2]) + 1) + ', "date": ' + date_text[1]
        + ', "start_hr": ' + time_text[0].substring(0, time_text[0].indexOf(':')) + ', "finish_hr": ' + time_text[1].substring(0, time_text[1].indexOf(':'))
        + '}'
    );
});

$('.schedule-container .pager li').click(function() {
    $(this).addClass('disabled');
    if($(this).hasClass('previous')) {
        if(!isThisWeek) {
            $('ul.time li').removeClass('selected')
            $('div.appointment-detail').addClass('hide');
            $('.schedule-container .pager li.next').removeClass('disabled');
            isThisWeek = true;
            getDateForDay();
        }
    } else if($(this).hasClass('next')) {
        if(isThisWeek) {
            $('ul.time li').removeClass('selected')
            $('div.appointment-detail').addClass('hide');
            $('.schedule-container .pager li.previous').removeClass('disabled');
            isThisWeek = false;
            getDateForDay();
        }
    }
})