if (permissions.update) {
    var $rows = $('tbody tr');
    $rows.each(function(index) {
        var $firstCol = $($(this).find('td').get(1));
        var $link = $('<a href=edit/' + $(this).attr('_id') + '>' + $firstCol.text() + '</a>');
        $firstCol.empty();
        $firstCol.append($link);
    });
}

if (!permissions.delete) {
    $('th:first-child').remove();
    $('td:first-child').remove();
}