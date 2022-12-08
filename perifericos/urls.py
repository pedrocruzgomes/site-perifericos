from django.urls import path
from .views import HomeView, PerifericosView, TecladosView, CarrinhoView, Signup, Login, logout

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('carrinho', CarrinhoView.as_view(), name='carrinho'),
    path('signup', Signup.as_view(), name='signup'),
    path('login', Login.as_view(), name='login'),
    path('logout', logout, name='logout'),
    path('perifericos/', PerifericosView.as_view(), name='perifericos'),
    path('perifericos/teclados', TecladosView.as_view(), name='teclados'),
]