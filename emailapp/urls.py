

from django.urls import path,include
from . import views
urlpatterns = [
    
    path('',views.index,name='index'),
    path('sendmail/',views.send_mail_to_all,name='mail'),
    
]