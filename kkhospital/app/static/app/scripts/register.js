$('form').submit(function(e) {
    if(!$('#confirm-form').prop('checked')) {
        e.preventDefault();
        alert('กรุณาทำเครื่องหมายหน้า "ข้าพเจ้ายินยอมเปิดเผยข้อมูลการตรวจรักษาของข้าพเจ้าให้แก่ คณะแพทย์ และพยาบาล"')
    }
});