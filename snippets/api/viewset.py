from rest_framework.response import Response
from snippets.models import Snippet
from snippets.api.serializers import SnippetSerializer
from rest_framework import viewsets
from rest_framework.decorators import action


# class SnippetViewSet(viewsets.ViewSet):
#
#     def list(self, request):
#         queryset = Snippet.objects.all()
#         serializer = SnippetSerializer(queryset, many=True)
#         return Response(serializer.data)


class SnippetViewSet(viewsets.ModelViewSet):

    # List, Retrieve, Update, Delete

    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    # Custom Urls
    @action(methods=['GET'], detail=False)
    def newest(self, request):
        newest = self.get_queryset().order_by('created').last()
        serializer = self.get_serializer_class()(newest)
        return Response(serializer.data)
