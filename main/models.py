from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Blog(models.Model):
    
    title = models.CharField(max_length=200) #짧은문자필드
    writer = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to="blog/", blank=True, null=True)
    tags = models.ImageField(upload_to="blog/", blank=True, null=True)

    
    def __str__(self) :
        return self.title
    
    def summary(self):
        return self.body[:20]
    

class Comment(models.Model):
    content = models.TextField()
    pub_date = models.DateTimeField()
    writer = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog,null=False,blank=False,on_delete=models.CASCADE)
    def __str__(self) :
        return self.blog.title+" : "+self.content[:20]
    

class Tag(models.Model):
    name=models.CharField(max_length=30, null=False, blank=False)
    
    def __str__(self):
        return self.name