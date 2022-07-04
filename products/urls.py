from django.urls import path
from . import views

urlpatterns=[
    path('',views.ProductsView.as_view()),
    path('<int:id>/', views.ProductDetailView.as_view()),
    path('rate/<int:id>/' , views.RateView.as_view()),
]
