from django.urls import path

from . import views

app_name = 'store'

urlpatterns = [
    path('', views.product_all, name='product_all'),
    path('<slug:slug>/', views.product_detail, name='product_detail'),
    path('shop/<slug:category_slug>/', views.category_list, name='category_list'),
]




#  from django.contrib.sessions.models import Session
# s = Session.objects.get(pk='ogtpewcf3gc4qn4a24qsyhea1xq8dc0o')
