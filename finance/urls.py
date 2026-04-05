
from django.urls import path
from .views import RecordListCreateView
urlpatterns = [path('', RecordListCreateView.as_view())]
