from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Blog(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=300)
    content=models.TextField()
    
    def __str__(self):
        return self.title + ' by ' + self.user.username

    
class Reviews(models.Model):
    blog=models.ForeignKey(Blog,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    comment=models.CharField(max_length=700)
    
    def __str__(self):
        return self.user.username + ' commented on ' + self.blog.title
    
    
    