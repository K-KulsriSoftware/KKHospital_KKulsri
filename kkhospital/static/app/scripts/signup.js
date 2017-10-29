$('form').submit(function(e) {
    if($('#id_password1').val() !== $('#id_password2').val()) {
        e.preventDefault();
        alert('รหัสผ่านไม่ตรงกัน')
    }
    if($('#id_password1').val().length < 8) {
        e.preventDefault();
        alert('รหัสผ่านต้องมีความยาวไม่น้อยกว่า 8 ตัวอักษร');
    }
});