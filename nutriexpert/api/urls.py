from django.urls import path
from .views import MessageView

urlpatterns = [
    path('process-message/', MessageView.as_view(), name='process-message'),
]
