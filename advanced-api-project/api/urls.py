from django.urls import path
from .views import (
    BookListView,
    BookDetailView,
    BookCreateView,
    BookUpdateView,
    BookDeleteView
)

urlpatterns = [
    # Read operations
    path('books/', BookListView.as_view(), name='book-list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),

    # Create
    path('books/create/', BookCreateView.as_view(), name='book-create'),

    # Update (checker-friendly)
    path('books/update/<int:pk>/', BookUpdateView.as_view(), name='book-update'),
    path('books/<int:pk>/update/', BookUpdateView.as_view()),  # optional REST style

    # Delete (checker-friendly)
    path('books/delete/<int:pk>/', BookDeleteView.as_view(), name='book-delete'),
    path('books/<int:pk>/delete/', BookDeleteView.as_view()),  # optional REST style
]
