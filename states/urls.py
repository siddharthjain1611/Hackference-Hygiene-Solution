from django.urls import path
from . import views

urlpatterns = [
    path('', views.state_list, name='state_list'),
    path('two-factor-theory', views.state_theory, name='state_theory'),
    path('state/<int:pk>/', views.state_detail, name='state_detail'),
    path('graphs', views.graphs, name='graphs'),
]