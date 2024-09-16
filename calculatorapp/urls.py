from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('submitquery',views.submitquery,name='submitquery')
   # path('',include('calculatorapp.urls'))
]

