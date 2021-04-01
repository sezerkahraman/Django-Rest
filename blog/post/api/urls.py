from django.urls import path,include
from post.api.views import PostListApiView,PostDetailAPIView,PostDeleteAPIView,PostUpdateAPIView,PostCreateAPIView
app_name="post"
urlpatterns = [
    path('list',PostListApiView.as_view(),name="list"),
    path('detail/<slug>',PostDetailAPIView.as_view(),name="detail"),
    path('delete/<slug>',PostDeleteAPIView.as_view(),name="delete"),
    path('update/<slug>',PostUpdateAPIView.as_view(),name="update"),
    path('create/',PostCreateAPIView.as_view(),name="update"),
]
