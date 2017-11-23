$('a#logout').click(function() {
    if (confirm('ยืนยันการออกจากระบบ')) {
        $('form#logout').submit();
    }
});