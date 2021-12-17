from django.db import models
from django.contrib.auth.models import User
from markdownx.models import MarkdownxField
from markdownx.utils import markdown

# Create your models here.
class Manufacturer(models.Model):
    company = models.CharField(max_length=30, unique=True)
    address = models.CharField(max_length=200)
    contact_numbers = models.CharField(max_length=15)
    country = models.CharField(max_length=30)

    def __str__(self):
        return self.company

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/shopping/category/{self.slug}/'

class Post(models.Model):
    # 상품명
    product_name = models.CharField(max_length=50)
    # 간단한 설명
    hook_text = models.CharField(max_length=100, blank=True)
    # 상품 설명
    content = MarkdownxField()
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
    # 카테고리
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)
    # 작성자
    author = models.ForeignKey(User,null=True,on_delete=models.SET_NULL)

    def __str__(self):
        return f'[{self.pk}]{self.product_name} - {self.Manufacturer}'

    def get_absolute_url(self):
        return f'/shopping/{self.pk}/'

    def get_content_markdown(self):
        return markdown(self.content)
