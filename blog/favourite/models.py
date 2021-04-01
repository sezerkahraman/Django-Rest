from django.db import models

from django.db import models
from django.contrib.auth.models import User

from post.models import Post

class Favourite(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    post=models.ForeignKey(Post,on_delete=models.CASCADE)
    content=models.TextField()

    def __str__(self): ##admin sayfasından favouritenin içine girdiğimizde karşımıza gelen ismin user ismi olmasını sağlıyor.
        return self.user.username