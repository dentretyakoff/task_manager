from django_elasticsearch_dsl import Document
from django_elasticsearch_dsl.registries import registry

from .models import Application


@registry.register_document
class ApplicationDocument(Document):
    class Index:
        name = 'applications'

    class Django:
        model = Application
        fields = (
            'name',
            'description',
        )
