from django.db import models

# DB 작성 필요


class Content(models.Model):
    pass


class Restaurant(models.Model):
    id = models.AutoField(primary_key=True)
    represent = models.CharField(max_length=200)
    mainkey = models.ForeignKey(Content, on_delete=models.CASCADE)


class Shopping(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    title = models.CharField(max_length=50)
    traffic = models.TextField()
    break_time = models.CharField(max_length=20)
    amenity = models.CharField(max_length=50)
    mainkey = models.ForeignKey(Content, on_delete=models.CASCADE)


class Festival(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=30)
    traffic = models.TextField()
    cost = models.CharField(max_length=30)
    amenity = models.CharField(max_length=50)
    mainkey = models.ForeignKey(Content, on_delete=models.CASCADE)


class Attraction(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    title = models.CharField(max_length=50)
    traffic = models.TextField()
    break_time = models.CharField(max_length=20)
    cost = models.CharField(max_length=30)
    amenity = models.CharField(max_length=50)
    mainkey = models.ForeignKey(Content, on_delete=models.CASCADE)


class User(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    inst_date = models.DateField(auto_now=True)
    updt_date = models.DateField(auto_now=True)
    mainkey = models.ForeignKey(Content, on_delete=models.CASCADE)


class Favorite(models.Model):
    pass


class Office(models.Model):
    id = models.AutoField(primary_key=True)
    call_number = models.CharField(max_length=30)
    time = models.CharField(max_length=30)
    latitude = models.CharField(max_length=20)
    longitude = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    address = models.TextField()
    foreign = models.CharField(max_length=50)
    introduction = models.TextField()

    pass


class gugun(models.Model):
    pass


# Create your models here.
