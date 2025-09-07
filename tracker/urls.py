from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/' , views.login_view , name="login_view"),
    path('register/' , views.register_view , name="register_view"),
    path('logout/' , views.logout_view , name="logout_view"),
    path('delete-transaction/<id>/', views.delete_transaction, name='delete_transaction')
]