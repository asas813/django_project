from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) # 글 작성자
    title = models.CharField(max_length=200) # 제목
    text = models.TextField() # 내용
    created_date = models.DateTimeField(default=timezone.now) # 생성시각
    published_date = models.DateTimeField(blank=True, null=True) # 발행시각

    def publish(self): # publish() 메서드
        self.published_date = timezone.now() # 현재시각을 가져옴
        self.save() # 저장

    def __str__(self):
        return self.title