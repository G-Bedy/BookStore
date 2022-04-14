from django.urls import path

from . import views

app_name = 'store'

urlpatterns = [
    path('', views.product_all, name='product_all'),
    path('<slug:slug>/', views.product_detail, name='product_detail'),
    path('shop/<slug:category_slug>/', views.category_list, name='category_list'),
]




#  from django.contrib.sessions.models import Session
# s = Session.objects.get(pk='knq0mxb6aavb3blzkfum1hebsb1oxxmx')
# s.get_decoded()