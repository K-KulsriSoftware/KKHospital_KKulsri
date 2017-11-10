$('.btn.delete').click(function() {
    var $rows = $('tbody input:checked').parent().parent();
    $rows.each(function() {
        $(this).remove();
    });
    $(this).addClass('hide');
})