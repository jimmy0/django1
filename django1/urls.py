from django.contrib import admin
from django.urls import include, path

from . import view,testdb
 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', view.hello, name='index'),
    path('testdb', testdb.testdb),
    path('polls/', include('polls.urls')),
]
