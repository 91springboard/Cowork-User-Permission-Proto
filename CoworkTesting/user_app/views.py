from django.shortcuts import render

# Create your views here.
from django.contrib.auth import get_user_model


# @login_required(login_url='login/')
def index(request):
    users = []
    if request.user.is_authenticated():
        users = get_user_model().objects.all()
    context = {'users': users, 'username': request.user.username or None}
    return render(request, 'user_app/index.html', context)
