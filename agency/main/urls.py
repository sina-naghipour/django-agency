from django.urls import path
from . import views
urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('about/', views.About.as_view(), name='about'),
    path('blog/', views.Blog.as_view(), name='blog'),
    path('contact/', views.Contact.as_view(), name='contact'),
    path('services/', views.Services.as_view(), name='services'),
]