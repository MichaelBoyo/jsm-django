from django.db import models
from django.utils import timezone


class Category(models.Model):
    category_name = models.CharField(max_length=100)

    def __str__(self):
        return str(self.category_name)


class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    todos = models.ForeignKey('Todo', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.username


class Expense(models.Model):
    amount = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField("date created", default=timezone.now)

    def __str__(self):
        return str(self.category)


class Income(models.Model):
    amount = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField("date created", default=timezone.now)

    def __str__(self):
        return str(self.category)


class Todo(models.Model):
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.TextField(blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_completed = models.DateTimeField(null=True, blank=True)
    important = models.BooleanField(default=False)
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.task


class Notes(models.Model):
    body = models.TextField(blank=True)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.body
