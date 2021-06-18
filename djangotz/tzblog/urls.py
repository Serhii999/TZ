from django.urls import path
from tzblog.views import *
from django.contrib.auth import views as auth_views

# For pass reset used Django view classes
urlpatterns = [
    path('', PostsListView.as_view(), name='main'),
    path('accounts/login/', Login.as_view(), name='login'),
    path('register/', UserCreateView.as_view(), name='register'),
    path('logout/', Logout.as_view(), name='logout'),
    path('postcreate/', PostCreateView.as_view(), name='post_create'),
    path('mainpost/', MainPostListView.as_view(), name='main_post'),
    path('comment/create/', CreateCommentView.as_view(), name='create_comment'),
    path('myposts/', MyPostsListView.as_view(), name='my_posts'),
    path('post_update/<int:pk>', UpdatePostView.as_view(), name='post_update'),
    path('delete_post/<int:pk>', DeletePostView.as_view(), name='delete_post'),
    path('reset_password/', auth_views.PasswordResetView.as_view(), name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
