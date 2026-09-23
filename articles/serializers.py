from rest_framework import serializers
from .models import Article
from articles.models import Category
from publishers.models import Publisher


class ArticleSerializer(serializers.ModelSerializer):
    """
    Serializer for approved article data exposed through the REST API.

    Converts Article model instances into JSON-friendly representations.
    Related author, publisher, and category objects are represented using
    their string values rather than primary keys.

    :var author: String representation of the article author.
    :vartype author: StringRelatedField

    :var publisher: String representation of the publisher.
    :vartype publisher: StringRelatedField

    :var category: String representation of the category.
    :vartype category: StringRelatedField
    """
    author = serializers.StringRelatedField()
    publisher = serializers.StringRelatedField()
    category = serializers.StringRelatedField()

    class Meta:
        """
        Metadata configuration for the ArticleSerializer.

        :var model: The Article model serialized by this serializer.
        :vartype model: Article

        :var fields: Model fields included in the serialized output.
        :vartype fields: list[str]
        """
        model = Article
        fields = [
            "id",
            "title",
            "content",
            "author",
            "publisher",
            "category",
            "status",
            "created_at",
        ]


class CategorySerializer(serializers.ModelSerializer):
    """Serializer for the Category model."""
    class Meta:
        model = Category
        fields = "__all__"


class PublisherSerializer(serializers.ModelSerializer):
    """Serializer for the Publisher model."""
    class Meta:
        model = Publisher
        fields = [
            "id",
            "name",
            "description",
            "website",
        ]
