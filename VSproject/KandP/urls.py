from django.urls import path
from . import views

urlpatterns = [
    path('', views.buy_view, name='buy'),
    path('sell/', views.sell_view, name='sell'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    path('product/<int:pk>/delete/', views.delete_product, name='delete_product'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]   