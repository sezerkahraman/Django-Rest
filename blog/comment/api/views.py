from rest_framework.generics import CreateAPIView,ListAPIView,DestroyAPIView,RetrieveUpdateAPIView

from comment.api.serializers import CommentSerializers,CommentListSerializers

from comment.models import Comment

from comment.api.permission import IsOwner
from comment.api.serializers import CommentDeleteUpdateSerializers
from rest_framework.mixins import DestroyModelMixin


class CommentCreateAPIView(CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializers
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class CommentListAPIView(ListAPIView):
    serializer_class = CommentListSerializers
    def get_queryset(self):
        return Comment.objects.filter(parent=None)


class CommentUpdateAPIView(RetrieveUpdateAPIView,DestroyModelMixin):
    queryset=Comment.objects.all()
    serializer_class=CommentDeleteUpdateSerializers
    lookup_field="pk"
    permission_classes=[IsOwner]

    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)

