from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True) #객체가 생성된 시간 저장

    def __str__(self): #admin페이지에서 title로 확인가능
        return self.title
