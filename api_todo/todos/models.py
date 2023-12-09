from django.db import models

class TodoStatusChoices(models.TextChoices):
    TODO = '1', 'To Do'
    DONE = '2', 'Done'

class Todo (models.Model):
    title = models.CharField(max_length=120)
    description = models.CharField(max_length=240)
    created_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(auto_now=True, null=True)
    status = models.CharField(choices=TodoStatusChoices.choices, default=TodoStatusChoices.TODO, max_length=1)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'Todo'
        verbose_name_plural = 'Todos'
        
    def __str__(self):
        return self.title