
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='app-home'),
    path('create-dojo', views.create_dojo, name='create-dojo'),
    path('delete-dojo/<int:pk>', views.delete_dojo, name='delete-dojo'),
    path('create-ninja', views.create_ninja, name='create-ninja'),
]