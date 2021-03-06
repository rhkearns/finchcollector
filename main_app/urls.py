from django.urls import path
from . import views

urlpatterns = [
  path('', views.Home.as_view(), name='home'),
  path('about/', views.about, name='about'),
  path('finches/', views.finches_index, name="finches_index"),
  path('finches/<int:finch_id>/', views.finches_detail, name='finches_detail'),
  path('finches/create/', views.FinchCreate.as_view(), name='finches_create'),
  path('finches/<int:pk>/update/', views.FinchUpdate.as_view(), name="finches_update"),
  path('finches/<int:pk>/delete/', views.FinchDelete.as_view(), name='finches_delete'),
  path('finches/<int:finch_id>/add_sighting', views.add_sighting, name='add_sighting'),
  path('houses/create', views.HouseCreate.as_view(), name='houses_create'),
  path('houses/<int:pk>/', views.HouseDetail.as_view(), name='houses_detail'),
  path('houses/', views.HouseList.as_view(), name='houses_index'),
  path('houses/<int:pk>/update/', views.HouseUpdate.as_view(), name='houses_update'),
  path('houses/<int:pk>/delete/', views.HouseDelete.as_view(), name='houses_delete'),
  path('finches/<int:finch_id>/assoc_house/<int:house_id>/', views.assoc_house, name='assoc_house'),
  path('accounts/signup/', views.signup, name="signup"),
]