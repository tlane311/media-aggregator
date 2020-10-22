from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="popular-page"),
    path('community/<str:community_id>/', views.individual_community, name="individual-community"),
    path('community/<str:community_id>/<str:post_id>/', views.individual_post, name="individual-post"),
    path('user/<str:user_id>', views.user, name="user"),
    path('user/', views.error, name="error"),
    path('community/', views.community, name="communities_redirect"),
    path('communities', views.communities, name="communities")
]