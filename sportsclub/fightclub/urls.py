from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('groups/', views.groups, name='groups'),
    path('groups/<int:group_id>', views.group, name='group'),
]