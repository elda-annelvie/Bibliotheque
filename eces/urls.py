from django.urls import path

from . import views

urlpatterns=[

	path('', views.AcceuilView.as_view(), name='accueil'),
	path('departements/', views.DepartementListView.as_view(), name='departement_list'),
	path('departements/<int:pk>/', views.DepartementDetailView.as_view(), name='departement_detail'),
	path('filieres/', views.FiliereListView.as_view(), name='filiere_list'),
	path('filieres/<int:pk>/', views.FiliereDetailView.as_view(), name='filiere_detail'),
	path('documents/', views.DocumentListView.as_view(), name='document_list'),
	path('documents/<int:pk>/', views.DocumentDetailView.as_view(), name='document_detail'),
    path('equipe/', views.EquipeView.as_view(), name='equipe_list'),
]
