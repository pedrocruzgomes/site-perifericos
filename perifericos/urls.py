from django.urls import path
from .views import HomeView, TecladosView, CarrinhoView, Signup, Login, logout, PedidosView, MousesView
from .views import HeadsetsView, MousepadsView, MonitoresView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('carrinho', CarrinhoView.as_view(), name='carrinho'),
    path('signup', Signup.as_view(), name='signup'),
    path('login', Login.as_view(), name='login'),
    path('logout', logout, name='logout'),
    path('meus-pedidos', PedidosView.as_view(), name='pedidos'),
    path('perifericos/teclados', TecladosView.as_view(), name='teclados'),
    path('perifericos/mouses', MousesView.as_view(), name='mouses'),
    path('perifericos/headsets', HeadsetsView.as_view(), name='headsets'),
    path('perifericos/mousepads', MousepadsView.as_view(), name='mousepads'),
    path('perifericos/monitores', MonitoresView.as_view(), name='monitores'),
]