// ===============================================================================
// Control checkbox and delete button

function handleDeleteButton() {
    var $toolbar = $('.toolbar');
    if($('td input[type="checkbox"]:checked').length > 0) {
        $toolbar.find('.delete').removeClass('hide');
    } else {
        $toolbar.find('.delete').addClass('hide');
    }
}

$('th input[type="checkbox"]').click(function() {
    if($(this).prop('checked')) {
        $('input[type="checkbox"]').prop('checked', true);
    } else {
        $('input[type="checkbox"]').prop('checked', false);
    }
    handleDeleteButton();
});

$('td input[type="checkbox"]').click(function() {
    var $checkedInput = $('td input[type="checkbox"]:checked');
    if($checkedInput.length === $('td input[type="checkbox"]').length) {
        $('th input[type="checkbox"]').prop('checked', true);
    } else {
        $('th input[type="checkbox"]').prop('checked', false);
    }
    handleDeleteButton();
});

$('input[type="checkbox"]').click(function() {
    handleDeleteButton();
});

// ===============================================================================
