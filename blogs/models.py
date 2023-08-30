from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Categories(models.Model):
    catagory = models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.catagory


class contact_usDB(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=90)
    phone=models.IntegerField() #maxlength not compulsary
    address=models.CharField(max_length=90)
    message=models.TextField() #maxlength not compulsary
    created_date=models.DateTimeField(auto_now_add=True)
    def __str__(self) -> str:
        return self.name


class blogs(models.Model):
    author_name=models.CharField(max_length=20)
    created_date=models.DateTimeField(auto_now_add=True)
    title=models.CharField(max_length=500)
    content = RichTextField()
    blog_image = models.FileField(upload_to="image/", max_length=500, null=True,default=None)
    catagory = models.ForeignKey(Categories, on_delete=models.CASCADE, null=True)
    show = models.BooleanField(default=False)
    def __str__(self):
        return self.title