
from django.contrib import admin
from django.urls import path
from django.conf.urls import url 
from adoptions import views
urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$',views.home,name='home'),
    # url(r'^adoptions/(\d+)/',views.pet_detail,name='pet_detail'),
    path('adoptions/<int:id>/',views.pet_detail,name ='pet_detail'),
    path('display/', views.pet_submission),
]
