from elasticsearch_dsl import Q
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from applications.documents import ApplicationDocument
from applications.models import Application
from applications.tasks import process_application

from .serializers import ApplicationSerializer


class ApplicationViewSet(viewsets.ModelViewSet):
    """Вьюсет задач, выполянет все операции CRUD."""
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    document_class = ApplicationDocument

    def perform_create(self, serializer):
        application = serializer.save()
        process_application.delay(application.id)

    @action(detail=False, methods=('get',), url_path='search')
    def search(self, request):
        params = request.query_params.get('q', None)
        if params:
            query = Q(
                'multi_match',
                query=params,
                fields=('name', 'description'),
                fuzziness='auto'
            )
            search = self.document_class().search().query(query)
            response = search.to_queryset()
            serializer = self.serializer_class(response, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({'error': 'Параметр запроса не был предоставлен'},
                        status=status.HTTP_400_BAD_REQUEST)
