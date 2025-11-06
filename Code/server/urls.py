from django.urls import path
from .views import *

urlpatterns = [

    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path("chat-history/", ChatHistoryCreateView.as_view(), name="chat-history"),
    path("category/", CategoryCreateView.as_view(), name="category-create"),
    path("chat-history/user/", UserChatHistoryView.as_view(), name="user-chat-history"),
    path("category/user/<str:category_name>/", UserCategoryFilterView.as_view(), name="user-category-filter")


]