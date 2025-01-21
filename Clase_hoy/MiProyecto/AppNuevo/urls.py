from django.urls import path
from .views import *

urlpatterns = [
    path('', AutorListView.as_view(), name='autor_list'),
    path('<int:pk>/', AutorDetailView.as_view(), name='autor_detail'),
    path('create/', AutorCreateView.as_view(), name='autor_create'),
    path('<int:pk>/update/', AutorUpdateView.as_view(), name='autor_update'),
    path('<int:pk>/delete/', AutorDeleteView.as_view(), name='autor_delete'),
]
