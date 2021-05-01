from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime,date
from ckeditor.fields import RichTextField
# Create your models here.

class Category(models.Model):

    name = models.CharField(max_length=255)


    def __str__(self):
        return self.name

# action after clicking post or any button
    def get_absolute_url(self):
        # return reverse('blog_details',args=(str(self.id)) )
        # or
        return reverse('Blog')


class Post(models.Model):
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=255)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    # body=models.TextField()
    Blog_cover_image= models.ImageField(blank=True,null=True, upload_to="images/")
    Blog_post_image_1= models.ImageField(blank=True,null=True, upload_to="images/")
    Blog_post_image_2= models.ImageField(blank=True,null=True, upload_to="images/")
    Blog_post_image_3= models.ImageField(blank=True,null=True, upload_to="images/")
    Blog_post_image_4= models.ImageField(blank=True,null=True, upload_to="images/")
    Blog_post_image_5= models.ImageField(blank=True,null=True, upload_to="images/")
    Blog_post_image_6= models.ImageField(blank=True,null=True, upload_to="images/")
    body=RichTextField(blank=True,null=True)
    post_date=models.DateField(auto_now_add=True)
    category = models.CharField(max_length=255,default='Travel')
    snippet = models.CharField(max_length=255)

    def __str__(self):
        return self.title + ' | ' + str(self.author)

# action after clicking post or any button
    def get_absolute_url(self):
        # return reverse('blog_details',args=(str(self.id)) )

        # or
        return reverse('Blog')



class PotographyPost(models.Model):
    portrait_image = models.ImageField(blank=True,null=True, upload_to="images/")
    landscape_image = models.ImageField(blank=True,null=True, upload_to="images/")
    food_image = models.ImageField(blank=True,null=True, upload_to="images/")

    def get_absolute_url(self):
        # return reverse('blog_details',args=(str(self.id)) )

        # or
        return reverse('photography')
    # def __str__(self):
    #     return self.title + ' | ' + str(self.author)



class Signup(models.Model):
    email= models.EmailField()
    timestamp= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
