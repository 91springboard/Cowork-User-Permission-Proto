from django.conf.urls import url

from . import views

urlpatterns = [
    url(
        r'^login/$',
        'django.contrib.auth.views.login',
        name='login',
        kwargs={'template_name': 'user_app/login.html'}
    ),
    url(
        r'^logout/$',
        'django.contrib.auth.views.logout',
        name='logout',
        kwargs={'next_page': '/'}
    ),
    url(r'^$', views.index, name='index'),
]
