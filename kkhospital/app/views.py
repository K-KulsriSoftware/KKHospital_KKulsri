from django.shortcuts import render
from django.http import HttpRequest, Http404, JsonResponse
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from datetime import datetime
from django.template.defaulttags import register
import json
# Create your views here.
from .API.API import API
api = API()


@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)

def check_logged_in(request):
    return 'user' in request.session and request.session['user'].get('is_authenticated')

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return redirect('/departments')

def departments(request):
    """Renders the about page."""
    if 'selected_package' in request.session:
        del request.session['selected_package']
    assert isinstance(request, HttpRequest)
    status, result = api.show_departments()
    return render(
        request,
        'app/departments.html',
        {
            'title': 'แผนกและแพ็คเกจ',
            'departments': result,
            'logged_user': request.session.get('user')
        }
    )

@login_required(login_url='/accounts/login')
def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title': 'About',
            'message': 'Your application description page.',
            'year': datetime.now().year,
            'logged_user': request.session.get('user')
        }
    )


def contact(request):
    if not check_logged_in(request):
        return redirect('/login/?next=/contact/')
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title': 'Contact',
            'message': 'Your contact page.',
            'year': datetime.now().year,
            'logged_user': request.session.get('user')
        }
    )

def doctor_detail(request):
    """Renders the about page."""
    if 'selected_package' not in request.session or 'selected_doctor' not in request.session:
        return redirect('/doctor-search')
    if request.method == 'POST':
        request.session['selected_date'] = json.loads(request.POST['date'])
        return redirect('/confirm/')
    assert isinstance(request, HttpRequest)
    status, doctor = api.show_doctor_detail(request.session['selected_doctor'])
    if status:
        status, package = api.show_special_package_info(
            request.session['selected_package'])
        working_times = {}
        for day in doctor['working_time']:
            if doctor['working_time'][day] != []:
                working_times[day] = []
                for time in doctor['working_time'][day]:
                    for i in range(int(time['start']), int(time['finish'])):
                        working_times[day].append(
                            {'start': i, 'finish': i + 1})
        print(working_times)
        return render(
            request,
            'app/doctor-detail.html',
            {
                'title': 'ข้อมูลแพทย์',
                'doctor': doctor,
                'selected_package': package,
                'working_time': working_times,
                'logged_user': request.session.get('user')
            }
        )
    else:
        raise Http404("No doctor found")

def member(request):
    """Renders the about page."""
    if not check_logged_in(request):
        return redirect('/login/?next=/member/')
    assert isinstance(request, HttpRequest)
    blood_abo = ['-', 'A', 'B', 'O', 'AB']
    blood_rh = ['', 'RH ลบ', 'RH บวก']
    status, member_detail = api.get_patients_detail(
        request.session['user']['username'])
    member_detail['blood_group_abo'] = blood_abo[member_detail['blood_group_abo']]
    member_detail['blood_group_rh'] = blood_rh[member_detail['blood_group_rh']]
    status, orders = api.get_patient_orders(
        request.session['user']['username'])
    return render(
        request,
        'app/member.html',
        {
            'title': 'ข้อมูลสมาชิก',
            'member_detail': member_detail,
            'orders': orders,
            'logged_user': request.session.get('user')
        }
    )


def edit_member_info(request):
    assert isinstance(request, HttpRequest)
    if request.method == 'POST':
        email = request.POST['email']
        status = request.POST['status']
        telephone_number = request.POST['telephone_number']
        emergency_phone = request.POST['emergency_phone']
        query_status, member_detail = api.get_patients_detail(
            request.session['user']['username'])

        # เอาค่า email, status ..... เอาไปใส่ใน field ของ dict member_detail แล้วเอา member_detail แต่ละ field ไปแทนใน paramenter ใน function ข้างล่าง
        member_detail['email'] = email
        member_detail['status'] = status
        member_detail['telephone_number'] = telephone_number
        member_detail['emergency_phone'] = emergency_phone
        query_status, result = api.update_patient_profile(member_detail['username'], member_detail['patient_name_title'], member_detail['patient_name'],
                                                          member_detail['patient_surname'], member_detail[
                                                              'patient_img'], member_detail['id_card_number'], member_detail['gender'],
                                                          member_detail['birthday'].year, member_detail[
                                                              'birthday'].month, member_detail['birthday'].day,
                                                          member_detail['blood_group_abo'], member_detail[
                                                              'blood_group_rh'], member_detail['race'], member_detail['nationallity'],
                                                          member_detail['religion'], member_detail['status'], member_detail[
                                                              'patient_address'], member_detail['occupy'], member_detail['telephone_number'],
                                                          member_detail['father_name'], member_detail[
                                                              'mother_name'], member_detail['emergency_name'],
                                                          member_detail['emergency_phone'], member_detail['emergency_address'], member_detail['email'], member_detail['congenital_disease'])
    blood_abo = ['-', 'A', 'B', 'O', 'AB']
    blood_rh = ['', 'RH ลบ', 'RH บวก']
    status, member_detail = api.get_patients_detail(
        request.session['user']['username'])
    member_detail['blood_group_abo'] = blood_abo[member_detail['blood_group_abo']]
    member_detail['blood_group_rh'] = blood_rh[member_detail['blood_group_rh']]
    return render(
        request,
        'app/edit-member.html',
        {
            'title': 'แก้ไขข้อมูลสมาชิก',
            'member_detail': member_detail,
            'logged_user': request.session.get('user')
        }
    )


def regular_packages(request):
    """Renders the about page."""
    if request.method == 'POST':
        request.session['selected_package'] = request.POST['package']
        return redirect('/doctor-search/')
    assert isinstance(request, HttpRequest)
    status, result = api.show_general_list()
    return render(
        request,
        'app/regular-package.html',
        {
            'title': 'ตรวจสุขภาพทั่วไป',
            'packages': result,
            'logged_user': request.session.get('user')
        }
    )


def special_packages(request, package_id):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    if request.method == 'POST':
        request.session['selected_package'] = request.POST['package']
        return redirect('/doctor-search/')
    status, result = api.show_special_package_info(package_id)
    print(result)
    return render(
        request,
        'app/special_packages.html',
        {
            'title': 'รายละเอียดแพ็คเกจ',
            'package': result,
            'package_id': package_id,
            'logged_user': request.session.get('user')
        }
    )


def search_for_doctor(request):
    """Renders the about page."""
    if 'selected_package' not in request.session:
        return redirect('/departments/')
    if request.method == 'POST':
        request.session['selected_doctor'] = request.POST['doctor_id']
        return redirect('/doctor-detail/')
    print(request.session['selected_package'])
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/doctor-search.html',
        {
            'title': 'ค้นหาแพทย์',
            'logged_user': request.session.get('user')
        }
    )


def doctor_search_api(request):
    package_id = request.session['selected_package']
    days = request.GET.get('days').split(
        ',') if request.GET.get('days') != None else None
    time = request.GET.get('time')
    print(time)
    doctor_firstname = request.GET.get('doctor_firstname')
    doctor_lastname = request.GET.get('doctor_surname')
    gender = request.GET.get('gender')
    status, result = api.find_doctors(
        package_id, days, time, doctor_firstname, doctor_lastname, gender)
    return JsonResponse({'status': status, 'result': result})


def doctor_auto_search_api(request):
    package_id = request.session['selected_package']
    status, result = api.auto_find_doctors(package_id)
    return JsonResponse({'status': status, 'result': result})


def doctor(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    if request.method == 'POST':
        request.session['selected_package'] = request.POST['package_id']
        request.session['selected_doctor'] = request.POST['doctor_id']
        return redirect('/doctor-detail/')
    status, result = api.show_doctor_in_department()
    print(result)
    return render(
        request,
        'app/doctor.html',
        {
            'title': 'แผนกและแพทย์',
            'departments': result,
            'logged_user': request.session.get('user')
        }
    )


def confirm(request):
    if not check_logged_in(request):
        return redirect('/login/?next=/confirm/')
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    if 'selected_package' not in request.session or 'selected_doctor' not in request.session or 'selected_date' not in request.session:
        return redirect('/doctor-detail/')
    if request.method == 'POST':
        status, result = api.create_order(request.session['selected_package'], request.session['selected_doctor'],
                                          request.session['user']['username'], '-', request.session['selected_date'])
        if status:
            return redirect('/')
    # print(request.session['selected_date'])
    status, package = api.show_special_package_info(
        request.session['selected_package'])
    status, doctor = api.show_doctor_detail(request.session['selected_doctor'])
    month = [
        'มกราคม',
        'กุมภาพันธ์',
        'มีนาคม',
        'เมษายน',
        'พฤษภาคม',
        'มิถุนายน',
        'กรกฎาคม',
        'สิงหาคม',
        'กันยายน',
        'ตุลาคม',
        'พฤศจิกายน',
        'ธันวาคม',
    ]
    return render(
        request,
        'app/confirm.html',
        {
            'title': 'ยืนยันแพ็คเกจ',
            'selected_package': package,
            'selected_doctor': doctor,
            'selected_date': request.session['selected_date']['date'],
            'selected_month': month[request.session['selected_date']['month'] - 1],
            'selected_year': request.session['selected_date']['year'],
            'selected_start_hr': request.session['selected_date']['start_hr'],
            'selected_finish_hr': request.session['selected_date']['finish_hr'],
            'logged_user': request.session.get('user')
        }
    )


@login_required(login_url='accounts/login')
def payment(request):
    """Renders the about page."""
    if not check_logged_in(request):
        return redirect('/login/?next=/payment/')
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/payment.html',
        {
            'title': 'ชำระค่าบริการ',
            'logged_user': request.session.get('user')
        }
    )


@staff_member_required(login_url='accounts/login')
def admin_mongo(request):
    assert isinstance(request, HttpRequest)
    status, result = api.get_all_collections_name()
    result.sort()
    return render(
        request,
        'app/admin-mongo.html',
        {
            'title': 'mongoDB Admin',
            'header_title': 'mongoDB Admin',
            'collections': result,
            'DATABASE': True,
            'logo_link': '/admin-mongo',
            'logged_user': request.session.get('user')
        }
    )


@staff_member_required(login_url='accounts/login')
def admin_mongo_collection(request, collection_name):
    assert isinstance(request, HttpRequest)
    status, result = {
        'buildings': api.get_all_buildings_name(),
        'departments': api.get_all_departments_name(),
        'doctors': api.get_all_doctors_name(),
        'orders': api.get_all_orders(),
        'patients': api.get_all_patients_name(),
        'users': api.get_all_users_name(),
        'packages': api.get_all_packages_name()
    }.get(collection_name)
    return render(
        request,
        'app/admin-mongo.html',
        {
            'title': 'mongoDB Admin',
            'header_title': 'mongoDB Admin',
            'collection_name': collection_name,
            'data': result,
            'COLLECTION': True,
            'toolbar': True,
            'logo_link': '/admin-mongo',
            'logged_user': request.session.get('user')
        }
    )


def login(request):
    assert isinstance(request, HttpRequest)
    if request.method == 'POST':
        status, username = api.verify_password(
            request.POST['username'], request.POST['password'])
        if status:
            status, result = api.check_already_used_this_username(
                request.POST['username'])
            if not status:
                request.session['just_regis'] = True
            request.session['user'] = {
                'username': request.POST['username'], 'is_authenticated': True}
            return redirect(request.POST['next'])

        else:
            return render(
                request,
                'app/login.html',
                {
                    'title': 'Log in',
                    'error': True
                }
            )
    if 'user' in request.session:  # mind add
        if request.session['user'].get('is_authenticated'):  # mind one tab
            return redirect('/')  # mind one tab
    next_page = '/'
    if 'next' in request.GET:
        next_page = request.GET['next']
    return render(
        request,
        'app/login.html',
        {
            'title': 'Log in',
            'next': next_page
        }
    )


def logout(request):
    assert isinstance(request, HttpRequest)
    request.session['user'] = {'is_authenticated': False}
    print(request.session['user'])
    return redirect('/')


def register(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    if not request.session.get('just_regis'):
        raise Http404("Page not found")
    if request.method == 'POST':
        patient_name_title = request.POST['patient_name_title']
        patient_name = request.POST['patient_name']
        patient_surname = request.POST['patient_surname']
        # patient_img = request.POST['patient_img']
        id_card_number = request.POST['id_card_number']
        gender = request.POST['gender'] == 'ชาย'
        birthday_year = int(request.POST['birthday_year'])
        birthday_month = int(request.POST['birthday_month'])
        birthday_day = int(request.POST['birthday_day'])
        blood_abo = ['-', 'A', 'B', 'O', 'AB']
        blood_rh = ['', '-', '+']
        blood_group_abo = blood_abo.index(
            request.POST['blood_group_abo']) if request.POST['blood_group_abo'] in blood_abo else 0
        blood_group_rh = blood_rh.index(
            request.POST['blood_group_rh']) if request.POST['blood_group_rh'] in blood_rh else 0
        race = request.POST['race']
        nationallity = request.POST['nationallity']
        Religion = request.POST['religion']
        Status = int(request.POST['Status'])
        pateint_address = request.POST['pateint_address']
        occupy = request.POST['occupy']
        telphone_number = request.POST['telphone_number']
        father_name = request.POST['father_name']
        mother_name = request.POST['mother_name']
        emergency_name = request.POST['emergency_name']
        emergency_phone = request.POST['emergency_phone']
        emergency_addr = request.POST['emergency_addr']
        email = request.POST['email']
        congenital_disease = request.POST['congenital_disease'].split(',')
        # เติมให้ครบ

        status, result = api.update_patient_profile(request.session['user']['username'], patient_name_title, patient_name, patient_surname, '',
                                                    id_card_number, gender, birthday_year, birthday_month, birthday_day,
                                                    blood_group_abo, blood_group_rh, race, nationallity, Religion, Status,
                                                    pateint_address, occupy, telphone_number, father_name, mother_name, emergency_name,
                                                    emergency_phone, emergency_addr, email, congenital_disease)
        if status:
            del request.session['just_regis']
            print(request.session['user'])
            return redirect('/')
        else:
            return render(
                request,
                'app/register.html',
                {
                    'title': 'สมัครสมาชิก',
                    'logged_user': request.session.get('user')
                }
            )
    else:
        return render(
            request,
            'app/register.html',
            {
                'title': 'สมัครสมาชิก',
                'logged_user': request.session.get('user')
            }
        )
