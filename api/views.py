import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from articles.models import Article
from articles.serializers import ArticleSerializer
from articles.models import Category
from articles.serializers import CategorySerializer
from publishers.models import Publisher
from articles.serializers import PublisherSerializer
from rest_framework import generics

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.


@csrf_exempt
@require_POST
def approved_article_log(request):
    """
    This endpoint is used to confirm when
    an article has been approved.

    :param request: Request object
    :type request: HTTPRequest

    :return: HTTP Status code 200 if the request is successful,

    otherwise returns a status code 400 with an error message.
    
    :rtype: HTTPResponse

    """
    try:

        #  if request.method == "POST":

        data = json.loads(request.body)

        print(
            f"APPROVED ARTICLE: "
            f"{data['title']}"
        )

        return JsonResponse(
            {
                "status": "received"
            },
            status=200
        )

    except json.JSONDecodeError:
        return JsonResponse(
            {"error": "Invalid JSON data"},
            status=400,
        )

    # return JsonResponse({
    #     "message": "Approved article endpoint"
    # })


class ApprovedArticleListAPIView(generics.ListAPIView):
    """View to list all approved articles via API."""
    serializer_class = ArticleSerializer

    def get_queryset(self):
        return Article.objects.filter(
            status="approved"
        ).order_by("-created_at")


class CategoryListAPIView(generics.ListAPIView):
    """View to list all categories via API."""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class PublisherListAPIView(generics.ListAPIView):
    """View to list all publishers via API."""
    queryset = Publisher.objects.filter(is_active=True)
    serializer_class = PublisherSerializer


class ProtectedAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({
            "message": f"Hello {request.user.username}"
        })
