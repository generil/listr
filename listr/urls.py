from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name=''),
    url(r'^login$', views.login, name=''),
    url(r'^signup$', views.signup, name=''),
    url(r'^questions/', include('questions.urls'))
]
