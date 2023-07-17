from django.urls import path
from . import views

# https://docs.djangoproject.com/en/3.0/topics/http/urls/
app_name = 'cats'
urlpatterns = [
    path('', views.MainView.as_view(), name='all'),
    path('main/create/', views.AutoCreate.as_view(), name='cat_create'),
    path('main/<int:pk>/update/', views.AutoUpdate.as_view(), name='cat_update'),
    path('main/<int:pk>/delete/', views.AutoDelete.as_view(), name='cat_delete'),
    path('lookup/', views.MakeView.as_view(), name='breed_list'),
    path('lookup/create/', views.MakeCreate.as_view(), name='breed_create'),
    path('lookup/<int:pk>/update/', views.MakeUpdate.as_view(), name='breed_update'),
    path('lookup/<int:pk>/delete/', views.MakeDelete.as_view(), name='breed_delete'),
]
