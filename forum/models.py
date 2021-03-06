from django.db import models

# Create your models here.
from django.db import models
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
# from django.contrib.auth.models import User
# Create your models here.
#from users.models import User
User = get_user_model()


class Forum(models.Model):
    user = models.ForeignKey(User,related_name='forum', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(null=False, blank=False, unique=False, default=0)

    def __str__(self):
        return self.title


class Comment(models.Model):
    user = models.ForeignKey(User, related_name='comment',on_delete=models.CASCADE)
    forum = models.ForeignKey(Forum,related_name='comment', on_delete=models.CASCADE)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)    
    likes = models.IntegerField(null=False, blank=False, unique=False,default=0)

    def __str__(self):
        return self.forum.title