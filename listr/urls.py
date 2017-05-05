from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
<<<<<<< HEAD
    url(r'^', include('user.urls')),
=======
    url(r'^$', include('questions.urls')),
>>>>>>> 315d1413d97b266642d5b619070fe217511c04e1
    url(r'^admin/', admin.site.urls),
]
