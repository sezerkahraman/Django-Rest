from rest_framework.permissions import BasePermission

class IsOwner(BasePermission):
    def has_permission(self, request, view): #önce burası çalışır eğer burdaki işlemler tamamsa diğer tarafa geçer
                                             #Yani delete update gibi sayfa ekranlarını açar fakat butonu ortadan kaldırır çünkü bu adımı geçemez
        return request.user and request.user.is_authenticated

    message="You must the owner of this object." #eğer değilsede mesaj vericez bu objenin sahibi siz olmalısınız diye.

    def has_object_permission(self, request, view, obj):
        return obj.user==request.user
        # Burda look_up ile gittiğimiz url nin user'ı ile bizim gitmek istediğimiz user eşitmi onun sorgusunu yapıyoruz
        # Eğer ki böyle bir işlem varsa bu gözüksün
        #Yani yukardaki yazdığımız return sayesinde herhangi bir update delete vs gibi işlemleri gerçekleştirmek için kullanıcının
        # ya kendi yazdığı bir makale olacak yada o kullanıcı super user kullanıcı olacak