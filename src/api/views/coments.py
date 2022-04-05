from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from api.serializers.comments_sz import ComentSerializers, ComentCreateSerializer
from project.models import Coment


class ComentListView(ListAPIView):
    queryset = Coment.objects.all()
    serializer_class = ComentSerializers


class ComentDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Coment.objects.all()
    serializer_class = ComentSerializers
    lookup_field = 'pk'
    lookup_url_kwarg = 'coment_id'


class ComentCreateView(CreateAPIView):
    serializer_class = ComentCreateSerializer