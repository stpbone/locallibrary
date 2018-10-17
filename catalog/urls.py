# Create a file inside your catalog folder called urls.py, and add the following text to define the (empty) imported urlpatterns. 
# This is where we'll add our patterns as we build the application. 

from django.urls import path
from catalog import views


urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.BookListView.as_view(), name='books'),
    path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
]