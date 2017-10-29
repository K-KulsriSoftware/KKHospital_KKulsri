from django.shortcuts import render
from django.http import HttpRequest
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from datetime import datetime
# Create your views here.
from .API.API import API
api = API()


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
