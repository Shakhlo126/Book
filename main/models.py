from django.db import models

# Create your models here.
class User(models.Model):
    phone_number = models.CharField(max_length=11, unique=True)
    password = models.CharField(max_length=11)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.phone_number

class Profile(models.Model):
    first_name = models.CharField(max_length=11)
    last_name = models.CharField(max_length=11)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=11, unique=True)
    image = models.ImageField(upload_to='profile_pics')
    birth_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name

class Category(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    name = models.CharField(max_length=11)
    image = models.ImageField(upload_to="images/")
    author = models.CharField(max_length=11)
    category = models.ManyToManyField(Category)
    page_count = models.CharField(max_length=11)
    short_description = models.CharField(max_length=11)
    price = models.CharField(max_length=110)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    client = models.ManyToManyField(User)
    phone_number = models.CharField(max_length=11, unique=True)
    address = models.CharField(max_length=11)
    note = models.TextField()
    product = models.ManyToManyField(Book)
    status = models.CharField(max_length=11)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.phone_number

class About(models.Model):
    title = models.CharField(max_length=11)
    description = models.TextField()
    image = models.ImageField(upload_to="images/")
    vd = models.CharField(max_length=11)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title