$('input[type="checkbox"]:first').click(function() {
    if($(this).prop('checked')) {
        $('input[type="checkbox"]').prop('checked', true);
    } else {
        $('input[type="checkbox"]').prop('checked', false);
    }
})

$('input[type="checkbox"]').click(function() {
    if($('input[type="checkbox"]').length > 0) {
        // $('button')
    }
})