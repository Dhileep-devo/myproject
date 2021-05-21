from rest_framework.serializers import ModelSerializer
from myapp.models import FeedFile
class FeedFileSerializer(ModelSerializer):
    class Meta:
        model=FeedFile
        fields='__all__'