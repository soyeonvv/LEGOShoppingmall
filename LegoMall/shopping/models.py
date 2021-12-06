from django.db import models

# Create your models here.
class Manufacturer(models.Model):
    company = models.CharField(max_length=30)
    address = models.CharField(max_length=200)
    contact_numbers = models.CharField(max_length=15)
    country = models.CharField(max_length=30)

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)

class Post(models.Model):
    # 상품명
    product_name = models.CharField(max_length=50)
    # 간단한 설명
    hook_text = models.CharField(max_length=100, blank=True)
    # 상품 설명
    content = models.TextField()
    # 상품 이미지
    head_image = models.ImageField(upload_to='lego/images/', blank=True)
    # 가격
    price = models.IntegerField()
    # 연령
    age = models.IntegerField()
    # 부품수
    pcs = models.IntegerField()
    # 제조사
    Manufacturer = models.ForeignKey(Manufacturer, null=True, blank=True, on_delete=models.CASCADE)
