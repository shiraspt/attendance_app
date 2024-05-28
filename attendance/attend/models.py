from django.db import models

# Create your models here.
class User(models.Model):
    user_name = models.CharField(max_length = 50)
    user_pword = models.CharField(max_length = 50)
    shift_start = models.TimeField( default='')
    shift_end = models.TimeField( default='')
    
    class Meta:
        db_table = 'user_tb'



class Work(models.Model):
    user_name=models.CharField(max_length = 50)
    work_date = models.DateField( default='')
    start_time= models.TimeField( default="00:00:00.00000")
    # end_time = models.TimeField( default="00:00:00.00000")
    # longtime1=models.FloatField(default=00)
    # longtime2=models.FloatField(default=00)
    latetime1=models.FloatField(default=00)
    # latetime2=models.FloatField(default=00)
    status=models.CharField(max_length = 20,default="absend")
    user=models.ForeignKey(User,on_delete = models.CASCADE)
   

    class Meta:
        db_table = 'work_tb'


class Exit(models.Model):
    user_name=models.CharField(max_length = 50)
    work_date = models.DateField( default='')
    exit_time= models.TimeField(default="00:00:00.00000")
    # longtime2=models.FloatField(default=00)
    extratime=models.FloatField(default=00)
    status=models.CharField(max_length = 20,default="absend")
    user=models.ForeignKey(User,on_delete = models.CASCADE)
   

    class Meta:
        db_table = 'exit_tb'