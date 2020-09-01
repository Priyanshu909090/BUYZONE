from django.db import models


# Create your models here.
class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=100, default="")
    product_description = models.CharField(max_length=1000, default="")
    product_price = models.IntegerField(default=0)
    actual_price = models.IntegerField(default=0)
    pub_date = models.DateField()
    category = models.CharField(max_length=50, default="")
    subcategory = models.CharField(max_length=80, default="")
    image = models.ImageField(upload_to='shop/images', default="")

    def __str__(self):
        return self.product_name


class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=70)
    email = models.CharField(max_length=50, default=" ")
    phone = models.CharField(max_length=60, default="")
    address = models.CharField(max_length=500, default=" ")
    textarea = models.CharField(max_length=1000)

    def __str__(self):
        return self.email


class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    items_json = models.CharField(max_length=10000, default="")
    name = models.CharField(max_length=111, default="")
    email = models.CharField(max_length=111, default="")
    address = models.CharField(max_length=111, default="")
    city = models.CharField(max_length=111, default="")
    state = models.CharField(max_length=111, default="")
    zip_code = models.CharField(max_length=111, default="")
    phone = models.CharField(max_length=111, default="")


class Women(models.Model):
    women_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=100, default="")
    product_description = models.CharField(max_length=1000, default="")
    product_price = models.IntegerField(default=0)
    actual_price = models.IntegerField(default=0)
    pub_date = models.DateField()
    category = models.CharField(max_length=50, default="")
    subcategory = models.CharField(max_length=80, default="")

    image = models.ImageField(upload_to='shop/images', default="")

    def __str__(self):
        return self.product_name


class Men(models.Model):
    men_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=100, default="")
    product_description = models.CharField(max_length=1000, default="")
    product_price = models.IntegerField(default=0)
    actual_price = models.IntegerField(default=0)
    pub_date = models.DateField()
    category = models.CharField(max_length=50, default="")
    subcategory = models.CharField(max_length=80, default="")

    image = models.ImageField(upload_to='shop/images', default="")

    def __str__(self):
        return self.product_name


class Kids(models.Model):
    kid_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=100, default="")
    product_description = models.CharField(max_length=1000, default="")
    product_price = models.IntegerField(default=0)
    actual_price = models.IntegerField(default=0)
    pub_date = models.DateField()
    category = models.CharField(max_length=50, default="")
    subcategory = models.CharField(max_length=80, default="")

    image = models.ImageField(upload_to='shop/images', default="")

    def __str__(self):
        return self.product_name


class Shoes(models.Model):
    shoes_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=100, default="")
    product_description = models.CharField(max_length=1000, default="")
    product_price = models.IntegerField(default=0)
    actual_price = models.IntegerField(default=0)
    pub_date = models.DateField()
    category = models.CharField(max_length=50, default="")
    subcategory = models.CharField(max_length=80, default="")

    image = models.ImageField(upload_to='shop/images', default="")

    def __str__(self):
        return self.product_name


class Watch(models.Model):
    wstch_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=100, default="")
    product_description = models.CharField(max_length=1000, default="")
    product_price = models.IntegerField(default=0)
    actual_price = models.IntegerField(default=0)
    pub_date = models.DateField()
    category = models.CharField(max_length=50, default="")
    subcategory = models.CharField(max_length=80, default="")

    image = models.ImageField(upload_to='shop/images', default="")

    def __str__(self):
        return self.product_name


class Other(models.Model):
    other_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=100, default="")
    product_description = models.CharField(max_length=1000, default="")
    product_price = models.IntegerField(default=0)
    actual_price = models.IntegerField(default=0)
    pub_date = models.DateField()
    category = models.CharField(max_length=50, default="")
    subcategory = models.CharField(max_length=80, default="")

    image = models.ImageField(upload_to='shop/images', default="")

    def __str__(self):
        return self.product_name
