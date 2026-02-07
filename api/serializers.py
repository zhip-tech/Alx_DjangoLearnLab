from rest_framework import serializers
from datetime import datetime
from .models import Author, Book


class BookSerializer(serializers.ModelSerializer):
    """
    BookSerializer converts Book model instances to JSON
    and validates incoming data.

    Custom validation ensures the publication year
    is not set in the future.
    """

    class Meta:
        model = Book
        fields = '__all__'

    def validate_publication_year(self, value):
        """
        Prevents books from having a publication year
        greater than the current year.
        """
        current_year = datetime.now().year
        if value > current_year:
            raise serializers.ValidationError(
                "Publication year cannot be in the future."
            )
        return value


class AuthorSerializer(serializers.ModelSerializer):
    """
    AuthorSerializer serializes Author data and
    dynamically includes related books using
    a nested BookSerializer.
    """

    # Nested relationship: One author → many books
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']
