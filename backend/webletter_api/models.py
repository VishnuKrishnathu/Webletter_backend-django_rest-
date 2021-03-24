from django.db import models

# Create your models here.

def profilePictureUpload(instance, filename):
    directory = instance.firstname + str(instance.id)
    return '/'.join(['pp',directory, filename])

def postsPictureUpload(instance, filename):
    directory = instance.posts.firstname + str(instance.posts.id)
    return '/'.join(['pp', directory, filename])


class BlogUsers(models.Model):
    firstname = models.CharField(max_length = 30)
    lastname = models.CharField(max_length = 30)
    phonenumber = models.BigIntegerField(null=True)
    emailid = models.EmailField(max_length= 200, null = True)
    profilepicture = models.ImageField(upload_to = profilePictureUpload, null= True, blank=True)

    def __str__(self):
        return self.firstname    

class Posts(models.Model):
    posts = models.ForeignKey('BlogUsers',null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length = 80)
    theme_image = models.ImageField(upload_to= postsPictureUpload, null = True, blank=True)
    article = models.TextField()

    def __str__(self):
        return self.title