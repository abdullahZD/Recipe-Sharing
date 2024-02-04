from django.urls import path
from .views import IngredientCreateView, register_user, user_login, user_logout
from. views import UserProfileRetrieveView, UserProfileUpdate ,  RecipeListView, RecipeCreateView, RecipeRetrieveView, \
RecipeUpdateView, RecipeDeleteView , \
FavoriteRecipeListView ,RatingsListView, RatingsRetrieveView



urlpatterns = [
    #Authentication urls
    path('register/', register_user, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    #Recipe
    #Recipe List
    path('recipe/', RecipeListView.as_view(), name='recipe-list'),
    #Create New Recipe
    path('recipe/create/', RecipeCreateView.as_view(), name='recipe-create'),
    #Retrive recipe with id
    path('recipe/<int:pk>/', RecipeRetrieveView.as_view(), name='recipe-detail'),
    #Update recipe
    path('recipe/<int:pk>/update/', RecipeUpdateView.as_view(), name='recipe-update'),
    #delete recipe
    path('recipe/<int:pk>/delete/', RecipeDeleteView.as_view(), name='recipe-delete'),
    #List the favorite recipe
    path('user/favorites/', FavoriteRecipeListView.as_view(), name='user-favorites'),
    #Add Ingreients
    path('Ingredient/create/', IngredientCreateView.as_view(), name='recipe-create'),
    #Ratings
    #list Ratings
    path('rating/', RatingsListView.as_view(), name='rating-list'),
    #Retrive Ratings id
    path('rating/<int:pk>/', RatingsRetrieveView.as_view(), name='rating-detail'),
    #User Profile
    #User Profile retrive by id
    path('profile/<int:pk>/', UserProfileRetrieveView.as_view(), name='profile-detail'),
    #User Profile Update 
    path('profile/<int:pk>/update/', UserProfileUpdate.as_view(), name='profile-update'),
    
]