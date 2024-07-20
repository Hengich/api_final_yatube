from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
#router.register('posts', PostViewSet, basename='posts')
#router.register(r'posts/(?P<id>\d+)/comments',
#                CommentViewSet, basename='comment')
#router.register('users', UserViewSet, basename='users')
#router.register(r'groups', GroupViewSet, basename='groups')
#router.register(r'follow', FollowViewSet, basename='follow')

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/', include('djoser.urls')),
    # JWT-эндпоинты, для управления JWT-токенами:
    path('v1/', include('djoser.urls.jwt')),
]
