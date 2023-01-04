from django.urls import path
from django.contrib.auth import views
from . import views

app_name = 'polls'
urlpatterns = [
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
    path("password_change/", views.PasswordChangeView.as_view(), name="password_change"),
    path("password_change/done/",views.PasswordChangeDoneView.as_view(),name="password_change_done",),
    path("password_reset/", views.PasswordResetView.as_view(), name="password_reset"),
    path("password_reset/done/",views.PasswordResetDoneView.as_view(),name="password_reset_done",),
    path("reset/<uidb64><token>/",views.PasswordResetConfirmView.as_view(),name="password_reset_confirm",),
    path("reset-done/",views.PasswordResetCompleteView.as_view(),name="password_reset_complete",)
    
   # path('', views.IndexView.as_view(), name='index'),
   # path('<int:pk>/', views.DetailView.as_view(), name='detail'),
   # path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
   # path('<int:question_id>/vote/', views.vote, name='vote'),
]
