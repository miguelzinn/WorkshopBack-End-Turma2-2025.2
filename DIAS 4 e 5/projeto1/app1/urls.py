from django.urls import path
from .views import EnderecoCreateView, EnderecoListView, EnderecoDetailView, EnderecoDeleteView

urlpatterns = [
    path('', EnderecoCreateView.as_view(), name='create'),
    path('lista/', EnderecoListView.as_view(), name='list'),
    path('detalhe/<int:pk>/', EnderecoDetailView.as_view(), name='detail'),
    path('excluir/<int:pk>/', EnderecoDeleteView.as_view(), name='delete'),
]
