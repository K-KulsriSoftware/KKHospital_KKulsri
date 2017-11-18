$('form').submit(function(e) {
    var $confirm_edit = $('input.confirm-edit');
    if(!$confirm_edit.prop('checked')) {
        e.preventDefault();
        alert('กรุณายืนยันการแก้ไขข้อมูล');
        return false;
    }
});