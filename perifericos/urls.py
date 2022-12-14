from django.urls import path
from .views import HomeView, TecladosView, Signup, Login, logout, MousesView
from .views import HeadsetsView, MousepadsView, MonitoresView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('signup', Signup.as_view(), name='signup'),
    path('login', Login.as_view(), name='login'),
    path('logout', logout, name='logout'),
    path('perifericos/teclados', TecladosView.as_view(), name='teclados'),
    path('perifericos/mouses', MousesView.as_view(), name='mouses'),
    path('perifericos/headsets', HeadsetsView.as_view(), name='headsets'),
    path('perifericos/mousepads', MousepadsView.as_view(), name='mousepads'),
    path('perifericos/monitores', MonitoresView.as_view(), name='monitores'),
]