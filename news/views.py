from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.serializers import Serializer, CharField, IntegerField

from .models import Category, News


class NewsCreateSerializer(Serializer):
    title = CharField(max_length=255)
    category_id = IntegerField()


@api_view(['POST'])
def news_create(request):
    serializer = NewsCreateSerializer(data=request.POST)
    serializer.is_valid()

    category = Category.objects.get(id=serializer.validated_data['category_id'])

    news = News.objects.create(
        title=serializer.validated_data['title'],
        category=category,
    )

    return Response()





