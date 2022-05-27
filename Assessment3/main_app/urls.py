from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('create', views.add_widget, name='create'),
    path('delete/<int:pk>', views.DeleteWidget.as_view(), name='delete')
]
