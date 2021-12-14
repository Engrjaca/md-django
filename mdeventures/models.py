from django.db import models

# Create your models here.


class Tasks(models.Model):
    report = models.CharField(max_length=20, blank=True, null=True)  
    merchant = models.CharField(max_length=20, blank=True, null=True) 
    frequency = models.CharField(max_length=20, blank=True, null=True)
    d1 = models.IntegerField(null=True, blank=True)
    path = models.CharField(max_length=100, blank=True, null=True)

    def __int__(self):
        return self.id

class Logs(models.Model):
    task_id = models.ForeignKey(Tasks, on_delete=models.CASCADE, null=True, blank=True)
    type = models.CharField(max_length=20, blank=True, null=True) 
    status = models.CharField(max_length=20, blank=True, null=True)  
    remarks = models.TextField(max_length=250, blank=True, null=True)  
    start_time = models.DateTimeField(blank=True, null=True) 
    end_time = models.DateTimeField(blank=True, null=True) 
   
    def __str__(self):
        return self.status