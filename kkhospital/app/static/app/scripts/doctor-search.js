$('li#auto').click(function () {
	$(this).addClass('active');
	$('li#manual').removeClass('active');
	$('div#manual-page').addClass('hide')
	$('div#auto-page').removeClass('hide')

	$.get('/doctor_auto_search_api/', function (data) {
		if (data && data.status && data.result.length > 0) {
			$('#auto-result').empty();
			var CSRFtoken = $('input[name=csrfmiddlewaretoken]').val();
			$(data.result).each(function () {
				$('#auto-result').append(`<div class="result-block">
		  <div class="div-img-circle"><img src="` + this.doctor_img + `" class="img-cir"/></div>
		  <div class="div-name"><span class="span-detail" title="` + this.doctor_name_title + this.doctor_name + ' ' + this.doctor_surname + `">` + this.doctor_name_title + this.doctor_name + ' ' + this.doctor_surname + `</span></div>
		  <span class="span-detail">` + this.department_name + `</span><br><form action="." method="POST">
		  <input type="hidden" name="csrfmiddlewaretoken" value="` + CSRFtoken + `">
		  <input type="hidden" name="doctor_id" value="` + this.doctor_id + `">
		  <button class="btn btn-default btn-res" type="submit">นัดหมายแพทย์</button></form>
		  </div>`);
			});
		} else {
			$('#result').append('<p>ไม่พบข้อมูล</p>');
		}
	})
})

$('li#manual').click(function () {
	$(this).addClass('active');
	$('li#auto').removeClass('active');
	$('div#auto-page').addClass('hide')
	$('div#manual-page').removeClass('hide')
});

$('.btn-summit').click(function () {
	if ($('.input-days input[type="checkbox"]:checked').length === 0 || $('.input-time input[type="checkbox"]:checked').length === 0 ||
		$('.input-gender input[type="checkbox"]:checked').length === 0) {
		alert('กรุณาทำเครื่องหมายในเงื่อนไขการค้นหาทุกส่วน (ยกเว้นชื่อและนามสกุลของแพทย์)');
		return;
	}
	$('#result').empty();
	var data = {};
	data.days = '';
	$('.input-days input[type="checkbox"]').each(function () {
		if ($(this).prop('checked')) {
			data.days += $(this).attr('id').substring(0, 3) + ','
		}
	});
	if (data.days === '') {
		delete data.days;
	} else {
		data.days = data.days.substring(0, data.days.length - 1);
	}
	data.time = '';
	$('.input-time input[type="checkbox"]').each(function () {
		if ($(this).prop('checked')) {
			data.time += $(this).closest('label').text().replace(/ /g, '').replace(/\n/g, '') + ',';
		}
	});
	if (data.time !== '' && (data.time.match(/,/g) || []).length > 1) {
		delete data.time;
	} else {
		data.time = data.time.replace(',', '');
	}
	data.doctor_firstname = $('.input-name input#in-firstname').val();
	if (data.doctor_firstname === '') {
		delete data.doctor_firstname;
	}
	data.doctor_surname = $('.input-name input#in-surname').val();
	if (data.doctor_surname === '') {
		delete data.doctor_surname;
	}
	data.gender = '';
	$('.input-gender input[type="checkbox"]').each(function () {
		if ($(this).prop('checked')) {
			data.gender += $(this).closest('label').text().replace(/ /g, '').replace(/\n/g, '') + ',';
		}
	});
	if (data.gender !== '' && (data.gender.match(/,/g) || []).length > 1) {
		delete data.gender;
	} else {
		data.gender = data.gender.replace(',', '');
	}
	console.log(data)
	$.get('/doctor_search_api', data, function (data) {
		if (data && data.status && data.result.length > 0) {
			var CSRFtoken = $('input[name=csrfmiddlewaretoken]').val();
			$(data.result).each(function () {
				$('#result').append(`<div class="result-block">
				<div class="div-img-circle"><img src="` + this.doctor_img + `" class="img-cir"/></div>
				<div class="div-name"><span class="span-detail" title="` + this.doctor_name_title + this.doctor_name + ' ' + this.doctor_surname + `">` + this.doctor_name_title + this.doctor_name + ' ' + this.doctor_surname + `</span></div>
				<span class="span-detail">` + this.department_name + `</span><br><form action="." method="POST">
				<input type="hidden" name="csrfmiddlewaretoken" value="` + CSRFtoken + `">
				<input type="hidden" name="doctor_id" value="` + this.doctor_id + `">
				<button class="btn btn-default btn-res" type="submit">นัดหมายแพทย์</button></form>
				</div>`);
			});
		} else {
			$('#result').append('<p>ไม่พบข้อมูล</p>');
		}
	});
})