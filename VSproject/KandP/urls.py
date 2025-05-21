from django.urls import path
from . import views

urlpatterns = [
    path('', views.buy_view, name='buy'),
    path('sell/', views.sell_view, name='sell'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
]


