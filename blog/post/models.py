from django.utils.text import slugify
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
class Post(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    title=models.CharField(max_length=120)
    content=models.TextField()
    draft=models.BooleanField(default=False)
    created=models.DateTimeField(editable=False) ##Eğer editable'i True yaparsak CreateAPIViewdan oluşturken oluşturma tarihini değiştirebiliriz
    modifield=models.DateTimeField()
    slug=models.SlugField(unique=True,max_length=150,editable=False) ##eğer slug'ı True yaparsak slug'ı CreateAPIViewdan değiştirebiliriz
    image=models.ImageField(upload_to="Resimler/post",null=True,blank=True)
    def __str__(self):
        return self.title
    def get_slug(self):
        slug=slugify(self.title.replace("ı","i"))
        unique=slug
        number=1
        while Post.objects.filter(slug=unique).exists():
            unique="{}-{}".format(slug,number)
            number+=1

        return unique

    def save(self, *args, **kwargs):
        if not self.id:
            self.created=timezone.now()
        self.modifield=timezone.now()
        self.slug=self.get_slug()
        return super(Post,self).save(*args,**kwargs)
# Create your models here.
