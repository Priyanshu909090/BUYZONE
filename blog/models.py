from django.db import models


class BlogPost(models.Model):
    blogpost_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, default="")
    heading1 = models.CharField(max_length=1000, default="")
    content1 = models.CharField(max_length=11111, default="")
    head2 = models.CharField(max_length=1111, default="")

    con2 = models.CharField(max_length=11111, default="")
    head3 = models.CharField(max_length=1111, default="")
    con3 = models.CharField(max_length=11111, default="")
    head4 = models.CharField(max_length=1111, default="")
    con4 = models.CharField(max_length=11111, default="")

    pub_date = models.DateField()
    category = models.CharField(max_length=50, default="")
    subcategory = models.CharField(max_length=80, default="")
    thumbnail = models.ImageField(upload_to='blog/images', default="")
    image1 = models.ImageField(upload_to='blog/images', default="")
    image2 = models.ImageField(upload_to='blog/images', default="")

    def __str__(self):
        return self.title

# # Create your models here.
# class BlogPost(models.Model):
#     blogPost_id = models.AutoField(primary_key=True)
#     title = models.CharField(max_length=1111, default="")
#     heading1 = models.CharField(max_length=1111, default="")
#     content1 = models.CharField(max_length=10000, default="")
#     heading2 = models.CharField(max_length=1111, default="")
#     content2 = models.CharField(max_length=10000, default="")
#     heading3 = models.CharField(max_length=1111, default="")
#     content3 = models.CharField(max_length=10000, default="")
#     heading4 = models.CharField(max_length=1111, default="")
#     content4 = models.CharField(max_length=10000, default="")
#     summary = models.CharField(max_length=10000, default="")
#
#     pub_date = models.DateField()
#
#     thumbnail = models.ImageField(upload_to='blog/images', default="")
#     image1 = models.ImageField(upload_to='blog/images', default="")
#     image2 = models.ImageField(upload_to='blog/images', default="")
#
#     def __str__(self):
#         return self.title
