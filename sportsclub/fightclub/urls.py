from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('groups/', views.groups, name='groups'),
    path('groups/<int:group_id>', views.group, name='group'),
    path('prices/', views.prices, name='prices'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/profile/', views.profile, name='profile'),

]