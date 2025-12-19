from django.urls import path
from users.views import RegisterView, AuthLoginView, UserListView, AuthLogoutView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', AuthLoginView.as_view(), name='login'),
    path('logout/', AuthLogoutView.as_view(), name='logout'),
    path('users_list/', UserListView.as_view(), name='users_list'),
]
