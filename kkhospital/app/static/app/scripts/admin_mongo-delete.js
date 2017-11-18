$('.btn.delete').click(function() {
    if (!confirm('ยืนยันการลบข้อมูล')) {
        return;
    }
    var $rows = $('tbody input:checked').parent().parent();
    var csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
    $rows.each(function() {
        (function($row) {
            $.post('delete/' + $row.attr('_id'), {csrfmiddlewaretoken: csrfToken}, function(data) {
                if (!data.ok) {
                    alert('ไม่สามารถลบ ' + $row.attr('_id') + ' ได้ กรุณาลองใหม่อีกครั้ง');
                } else {
                    $row.remove();
                }
            })
        })($(this));
    });
    $(this).addClass('hide');
})