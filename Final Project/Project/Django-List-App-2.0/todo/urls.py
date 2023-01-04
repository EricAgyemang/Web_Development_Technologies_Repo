from django.urls import path, include
from django.views.generic import TemplateView
from todo.views import Register

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.addTodo, name='add'),
    path('complete/<todo_id>/', views.completeTodo, name='complete'),
    path('deletecomplete/', views.deleteCompleted, name='deletecomplete'),
    path('deleteall/', views.deleteAll, name='deleteall'),
    path('accounts/',include('django.contrib.auth.urls')),
    # path('register/success/',TemplateView.as_view(template_name="registration/success.html"), name = 'register-success'),
    path('register/', Register.as_view(), name = 'register'),  
]