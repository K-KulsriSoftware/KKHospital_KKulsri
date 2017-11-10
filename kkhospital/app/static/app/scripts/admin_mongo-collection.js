var $rows = $('tbody tr');
$rows.each(function(index) {
    var $firstCol = $($(this).find('td').get(1));
    var $link = $('<a href=' + $(this).attr('goto') + '>' + $firstCol.text() + '</a>');
    $firstCol.empty();
    $firstCol.append($link);
});