if (user !== 'AnonymousUser' && group === '') {
    $.get('/check-user-information', {username: user}, function(data) {
        if (!data.hasInfo) {
            $('#get-info-popup').css('top', '0px');
        }
    });
}