from django.db import models
from django.conf import settings
from datetime import datetime, timedelta, timezone

# Create your models here.
class Problem(models.Model):
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_problems')
    problem_url = models.CharField(max_length=50)
    # constraint = models.TextField()
    problem_number = models.IntegerField()
    title = models.CharField(max_length=20)
    content = models.TextField()
    input = models.TextField(default='.')
    output = models.TextField(default='.')
    level = models.CharField(max_length=20)
    type = models.CharField(max_length=20, default='비밀')

    def __str__(self):
        return self.title

class Solution(models.Model):
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_solutions')
    hint = models.TextField(default='.')
    code = models.TextField()
    description = models.TextField(default='.')
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def created_string(self):
        time = datetime.now(tz=timezone.utc) - self.created_at
        if time < timedelta(minutes=1):
            return '방금 전'
        elif time < timedelta(hours=1):
            return str(int(time.seconds / 60)) + '분 전'
        elif time < timedelta(days=1):
            return str(int(time.seconds / 3600)) + '시간 전'
        elif time < timedelta(days=7):
            time = datetime.now(tz=timezone.utc).date() - self.registered_date.date()
            return str(time.days) + '일 전'
        else:
            return self.created_at.date
    
    # def __str__(self): ##Solution 모델에 title필드가 없다고 에러가 떠서 주석처리 해놓았습니다
    #         return self.title

class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='al_comments')
    solution = models.ForeignKey(Solution, on_delete=models.CASCADE)
    content = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)


    @property
    def created_string(self):
        time = datetime.now(tz=timezone.utc) - self.created_at
        if time < timedelta(minutes=1):
            return '방금 전'
        elif time < timedelta(hours=1):
            return str(int(time.seconds / 60)) + '분 전'
        elif time < timedelta(days=1):
            return str(int(time.seconds / 3600)) + '시간 전'
        elif time < timedelta(days=7):
            time = datetime.now(tz=timezone.utc).date() - self.registered_date.date()
            return str(time.days) + '일 전'
        else:
            return self.created_at.date
    
    # def __str__(self): ##Solution 모델에 title필드가 없다고 에러가 떠서 주석처리 해놓았습니다
    #         return self.title

class TestCase (models.Model):
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    input = models.TextField()
    output = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def created_string(self):
        time = datetime.now(tz=timezone.utc) - self.created_at
        if time < timedelta(minutes=1):
            return '방금 전'
        elif time < timedelta(hours=1):
            return str(int(time.seconds / 60)) + '분 전'
        elif time < timedelta(days=1):
            return str(int(time.seconds / 3600)) + '시간 전'
        elif time < timedelta(days=7):
            time = datetime.now(tz=timezone.utc).date() - self.registered_date.date()
            return str(time.days) + '일 전'
        else:
            return self.created_at.date
