var $rows = $('tbody tr');
$rows.click(function() {
    window.location = window.location + $(this).attr('goto');
});