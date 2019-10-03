from rest_framework.response import Response
from snippets.models import Snippet
from snippets.api.serializers import SnippetSerializer
from rest_framework import viewsets
from rest_framework.decorators import action

# Auth in viewset
# from rest_framework.authentication import TokenAuthentication
# from rest_framework.permissions import IsAuthenticated


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

    # # Authentication in Viewset Base
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)


    # Custom Urls
    @action(methods=['GET'], detail=False)
    def newest(self, request):
        newest = self.get_queryset().order_by('created').last()
        serializer = self.get_serializer_class()(newest)
        return Response(serializer.data)
