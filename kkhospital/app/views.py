from django.shortcuts import render
from django.http import HttpRequest, Http404, JsonResponse
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from datetime import datetime
from django.template.defaulttags import register
from html_json_forms import parse_json_form
from bson.objectid import ObjectId
import json
# Create your views here.
from .API.API import API
api = API()

blood_abo = ['-', 'A', 'B', 'O', 'AB']
blood_rh = ['', 'RH-', 'RH+']

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)

def check_logged_in(request):
    return 'user' in request.session and request.session['user'].get('is_authenticated')

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return redirect('/departments')

def check_user_information(request):
    return JsonResponse({'hasInfo': api.get_patient_id(request.GET.get('username'))[0]})

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
        # print(working_times)
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

def doctor_profile(request):
    """Renders the about page."""
    doctor_id = api.get_doctor_id(request.user.username)[1]
    status, doctor = api.show_doctor_detail(doctor_id)
    status, orders = api.get_doctor_orders(request.user.username)
    return render(
        request,
        'app/doctor-profile.html',
        {
            'title': 'ข้อมูลแพทย์',
            'doctor': doctor,
            'orders': orders,
        }
    )

@login_required(login_url='/accounts/login')
def member(request):
    global blood_abo, blood_rh
    assert isinstance(request, HttpRequest)
    if not api.get_patient_id(request.user.username)[0]:
        return redirect('/register')
    status, patient_id = api.get_patient_id(request.user.username)
    status, member_detail = api.get_patient_detail(patient_id)
    member_detail['blood_group_abo'] = blood_abo[member_detail['blood_group_abo']]
    member_detail['blood_group_rh'] = blood_rh[member_detail['blood_group_rh']]
    status, orders = api.get_patient_orders(request.user.username)
    return render(
        request,
        'app/member.html',
        {
            'title': 'ข้อมูลสมาชิก',
            'member_detail': member_detail,
            'orders': orders,
            'logged_user': request.user.username
        }
    )

@login_required(login_url='/accounts/login')
def treat(request, order_id):
    global blood_abo, blood_rh
    if request.method == 'POST':
        status, result = api.insert_note(order_id, request.POST.get('treating-detail'))
        if status:
            return redirect('/doctor-profile')
    assert isinstance(request, HttpRequest)
    order_detail = api.get_order_detail(order_id)[1]
    status, patient_detail = api.get_patient_detail(order_detail['patient_id'])
    patient_detail['blood_group_abo'] = blood_abo[patient_detail['blood_group_abo']]
    patient_detail['blood_group_rh'] = blood_rh[patient_detail['blood_group_rh']]
    # member_detail['blood_group_abo'] = blood_abo[member_detail['blood_group_abo']]
    # member_detail['blood_group_rh'] = blood_rh[member_detail['blood_group_rh']]
    return render(
        request,
        'app/member-profile.html',
        {
            'title': 'การรักษา',
            'member_detail': patient_detail,
            'note': order_detail['note']
        }
    )

@login_required(login_url='/accounts/login')
def edit_member_info(request):
    assert isinstance(request, HttpRequest)
    if request.method == 'POST':
        email = request.POST['email']
        # status = request.POST['status']
        telephone_number = request.POST['telephone_number']
        emergency_phone = request.POST['emergency_phone']
        status, patient_id = api.get_patient_id(request.user.username)
        status, member_detail = api.get_patient_detail(patient_id)

        # เอาค่า email, status ..... เอาไปใส่ใน field ของ dict member_detail แล้วเอา member_detail แต่ละ field ไปแทนใน paramenter ใน function ข้างล่าง
        member_detail['email'] = email
        # member_detail['status'] = status
        member_detail['telephone_number'] = telephone_number
        member_detail['emergency_phone'] = emergency_phone
        member_detail['birthday'] = {'day': member_detail['birthday'].day, 'month': member_detail['birthday'].month, 'year': member_detail['birthday'].year}
        query_status, result = api.update_patient(patient_id, member_detail)
        if query_status:
            return redirect('..')
    blood_abo = ['-', 'A', 'B', 'O', 'AB']
    blood_rh = ['', 'RH ลบ', 'RH บวก']
    status, patient_id = api.get_patient_id(request.user.username)
    status, member_detail = api.get_patient_detail(patient_id)
    member_detail['gender'] = 'ชาย' if member_detail['gender'] else 'หญิง'
    member_detail['blood_group_abo'] = blood_abo[member_detail['blood_group_abo']]
    member_detail['blood_group_rh'] = blood_rh[member_detail['blood_group_rh']]
    member_detail['congenital_disease'] = ', '.join(member_detail['congenital_disease'])
    return render(
        request,
        'app/edit-member.html',
        {
            'title': 'แก้ไขข้อมูลสมาชิก',
            'member_detail': member_detail,
            'logged_user': request.user.username
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
    # print(result)
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
    # print(request.session['selected_package'])
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
    # print(time)
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
    # print(result)
    return render(
        request,
        'app/doctor.html',
        {
            'title': 'แผนกและแพทย์',
            'departments': result,
            'logged_user': request.session.get('user')
        }
    )

@login_required(login_url='/accounts/login')
def confirm(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    if 'selected_package' not in request.session or 'selected_doctor' not in request.session or 'selected_date' not in request.session:
        return redirect('/doctor-detail/')
    if request.method == 'POST':
        status, result = api.create_order(request.session['selected_package'], request.session['selected_doctor'],
                                          request.user.username, '-', request.session['selected_date'])
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
            'logged_user': request.user.username
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

def check_user_group(group_name, user):
    groups = user.groups.all()
    print(groups)
    return len(groups) > 0 and groups[0].name == group_name


@login_required(login_url='/accounts/login')
def admin_mongo(request):
    if not check_user_group('staff', request.user):
        raise PermissionDenied
    assert isinstance(request, HttpRequest)
    status, result = api.get_all_collections_name()
    result.sort()
    return render(
        request,
        'app/admin_mongo.html',
        {
            'title': 'mongoDB Admin',
            'header_title': 'mongoDB Admin',
            'collections': result,
            'DATABASE': True,
            'logo_link': '/admin-mongo',
            'logged_user': request.session.get('user'),
            'only_logout': True
        }
    )

def decode_data(data):
    for k, v in data.items():
        if type(v) == type({}):
            pass
        elif type(v) == type([]):
            pass
        else:
            data[k] = api.decode_thai_value(k, v)[1]


@login_required(login_url='/accounts/login')
def admin_mongo_collection(request, collection_name):
    if not check_user_group('staff', request.user):
        raise PermissionDenied
    assert isinstance(request, HttpRequest)
    permissions = {}
    permissions['insert'] = 1 if api.get_collection_permission(collection_name, 'insert')[0] else 0
    permissions['delete'] = 1 if api.get_collection_permission(collection_name, 'delete')[0] else 0
    permissions['update'] = 1 if api.get_collection_permission(collection_name, 'update')[0] else 0
    # print(collection_name)
    # print(permissions)
    status, data = api.admin_get_all_documents(collection_name)
    result = []
    for doc in data:
        tmp = {}
        for k, v in doc.items():
            if k == '_id':
                k = 'object_id'
            tmp[k] = v
        decode_data(tmp)
        result.append(tmp)
    return render(
        request,
        'app/admin_mongo.html',
        {
            'title': 'mongoDB Admin',
            'header_title': 'mongoDB Admin',
            'collection_name': collection_name,
            'permissions': permissions,
            'data': result,
            'COLLECTION': True,
            'toolbar': True,
            'logo_link': '/admin-mongo',
            'logged_user': request.session.get('user'),
            'only_logout': True
        }
    )

def clean_field(org, res, name=''):
    for field in org:
        tmp = field['field_name']
        if name != '':
            tmp = '[' + tmp + ']'
        if field['field_type'] == 'dict':
            clean_field(field['dict'], res, name + tmp)
        elif field['field_type'] == 'list' and field['value'] == 'dict':
            clean_field(field['dict'], res, name + tmp + '[0]')
        else:
            this_field = {'field_name': name + tmp, 'field_type': field['field_type']}
            if 'value' in field:
                this_field['value'] = field['value']
            res.append(this_field)

@login_required(login_url='/accounts/login')
def admin_mongo_add(request, collection_name):
    if not check_user_group('staff', request.user):
        raise PermissionDenied
    if request.method == 'POST':
        tmp = dict(request.POST)
        for key in tmp:
            tmp[key] = tmp[key][0]
        del tmp['csrfmiddlewaretoken']
        # return JsonResponse(parse_json_form(tmp))
        # print(parse_json_form(tmp))
        status, result = api.admin_insert_document(collection_name, parse_json_form(tmp))
        if status:
            return redirect('..')
        else:
            return redirect('.')
    status, fields = api.get_collection_pattern(collection_name)
    found_id = False
    for i in range(len(fields)):
        if fields[i]['field_name'] == '_id':
            found_id = True
            index = i
            break
    if found_id:
        del fields[index]
    # print(fields)
    return render(
        request,
        'app/admin_mongo-add.html',
        {
            'title': 'mongoDB Admin',
            'header_title': 'mongoDB Admin',
            'collection_name': collection_name,
            'fields': json.dumps(fields),
            'logo_link': '/admin-mongo',
            'only_logout': True
        }
    )

def clean_datatype(data):
    for k, v in data.items():
        if type(v) == type(datetime.now()) or type(v) == type(ObjectId()):
            data[k] = str(v)
        elif type(v) == type({}):
            clean_datatype(data[k])
        elif type(v) == type([]):
            for i in range(len(v)):
                if type(v) == type(datetime.now()) or type(v) == type(ObjectId()):
                    data[k] = str(v)
                elif type(v) == type({}):
                    clean_datatype(v[i])

def fill_field(fields, data):
    for field in fields:
        if data == None or data.get(field['field_name']) == None:
            if field['field_type'] == 'dict':
                fill_field(field['dict'], None)
            else:
                data[field['field_name']] = None
        elif field['field_type'] == 'date':
            tmp = data[field['field_name']].split('-')
            data[field['field_name']] = {
                'year': tmp[0],
                'month': tmp[1],
                'day': tmp[2]
            }

@login_required(login_url='/accounts/login')
def admin_mongo_edit(request, collection_name, object_id):
    if not check_user_group('staff', request.user):
        raise PermissionDenied
    if request.method == 'POST':
        tmp = dict(request.POST)
        for key in tmp:
            tmp[key] = tmp[key][0]
        del tmp['csrfmiddlewaretoken']
        # return JsonResponse(parse_json_form(tmp))
        data = parse_json_form(tmp)
        status, fields = api.get_collection_pattern(collection_name)
        fill_field(fields, data)
        status, result = api.admin_update_document(collection_name, object_id, data)
        if status:
            return redirect('..')
        else:
            return redirect('.')
    status, fields = api.get_collection_pattern(collection_name)
    status, data = api.admin_get_detail(collection_name, object_id)
    clean_datatype(data)
    found_id = False
    for i in range(len(fields)):
        if fields[i]['field_name'] == '_id':
            found_id = True
            index = i
            break
    if found_id:
        del fields[index]
    return render(
        request,
        'app/admin_mongo-add.html',
        {
            'title': 'mongoDB Admin',
            'header_title': 'mongoDB Admin',
            'collection_name': collection_name,
            'fields': json.dumps(fields).replace('"', '\\"').replace("'", "\\'"),
            'data': json.dumps(data).replace('"', '\\"').replace("'", "\\'"),
            'logo_link': '/admin-mongo',
            'only_logout': True
        }
    )

@login_required(login_url='/accounts/login')
def admin_mongo_delete(request, collection_name, object_id):
    if not check_user_group('staff', request.user):
        raise PermissionDenied
    if request.method == 'POST':
        status, result = api.admin_delete_document(collection_name, object_id)
        respose = {'ok': 1 if status else 0}
        return JsonResponse(respose)
    else:
        pass

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

def register(request):
    """Renders the about page."""
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
        blood_group_abo = int(request.POST['blood_group_abo'])
        race = request.POST['race']
        nationallity = request.POST['nationallity']
        religion = request.POST['religion']
        Status = int(request.POST['status'])
        patient_address = request.POST['patient_address']
        occupy = request.POST['occupy']
        telephone_number = request.POST['telephone_number']
        father_name = request.POST['father_name']
        mother_name = request.POST['mother_name']
        emergency_name = request.POST['emergency_name']
        emergency_phone = request.POST['emergency_phone']
        emergency_addr = request.POST['emergency_addr']
        email = request.POST['email']
        congenital_disease = request.POST['congenital_disease'].split(',')
        # เติมให้ครบ

        status, result = api.register(request.user.username, patient_name_title, patient_name, patient_surname, '',
                                                    id_card_number, gender, birthday_year, birthday_month, birthday_day,
                                                    blood_group_abo, 0, race, nationallity, religion, Status,
                                                    patient_address, occupy, telephone_number, father_name, mother_name, emergency_name,
                                                    emergency_phone, emergency_addr, email, congenital_disease, True)
        if status:
            return redirect('/')
        else:
            return render(
                request,
                'app/register.html',
                {
                    'title': 'ข้อมูลผู้ป่วย',
                    'logged_user': request.user.username,
                    'REGISTER_PAGE': True
                }
            )
    else:
        return render(
            request,
            'app/register.html',
            {
                'title': 'ข้อมูลผู้ป่วย',
                'logged_user': request.user.username,
                'REGISTER_PAGE': True
            }
        )
