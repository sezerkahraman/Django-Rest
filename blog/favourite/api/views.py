from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from favourite.models import Favourite

from favourite.api.serializers import FavouriteListCreateAPISerializer

from favourite.models import Favourite

from favourite.api.serializers import FavaouriteUpdateDestroyAPISerializer

from favourite.api.permission import IsOwner


class FavouriteListCreateAPIView(ListCreateAPIView):
    queryset = Favourite.objects.all()
    serializer_class = FavouriteListCreateAPISerializer

    def get_queryset(self): ##Çünkü listelenen bilgiler oturum açmış kişinin kendi bilgileri olması lazım.
        return Favourite.objects.filter(user=self.request.user)

    def perform_create(self, serializer): ##Bir kayıt işlemi yaptığımızda kendi adımıza kaydetmemizi sağlar
        serializer.save(user=self.request.user)

class FavouriteAPIView(RetrieveUpdateDestroyAPIView):
        queryset = Favourite.objects.all()
        serializer_class =FavaouriteUpdateDestroyAPISerializer
        lookup_field = "pk"
        permission_classes = [IsOwner]


