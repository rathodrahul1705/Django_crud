from django.urls import path
from .import views

urlpatterns= [
	path('', views.index, name='index'),
	path('create', views.create, name='create'),
	path('read', views.read, name='read'),
	path('save', views.save, name='save'),
	path('edit/<str:id>/', views.edit, name='edit'),
	# path('update/<str:id>/', views.update, name='update'),
	path('update/<int:id>', views.update), 
	path('delete/<int:id>', views.delete), 

]