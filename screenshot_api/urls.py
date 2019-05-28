from django.urls import path

from . import views

urlpatterns = [
    path('screenshot/', views.FetchScreenshotView.as_view(), name='grab screenshot'),
    path('list/', views.ListScreenshotView.as_view(), name='list screenshots'),
]
