from django.urls import path
from rest_framework import routers
from . import views

urlpatterns = [
    path('take-screenshot/', views.FetchScreenshotView.as_view(), name='take-screenshot'),
    path('list-screenshot/', views.ListScreenshotView.as_view(), name='list-screenshots'),
    path('media/<str:name>', views.MediaView.as_view(), name='serve-media'),
]

router = routers.SimpleRouter()
router.register(r'screenshot', views.ScreenshotViewSet)
urlpatterns += router.urls
