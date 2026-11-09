from django.urls import path
from . import views

urlpatterns = [
    path('', views.TacheListView.as_view(), name='tache-list'),
    path('<int:pk>/', views.TacheDetailView.as_view(), name='tache-detail'),
    path('ajouter/', views.TacheCreateView.as_view(), name='tache-create'),
    path('<int:pk>/modifier/', views.TacheUpdateView.as_view(), name='tache-update'),
    path('<int:pk>/supprimer/', views.TacheDeleteView.as_view(), name='tache-delete'),
]