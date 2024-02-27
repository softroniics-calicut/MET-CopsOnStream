from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class CustomUser(AbstractUser):
    #common fields for both regular users and police
    phone=models.IntegerField(null=True,blank=True)
    address=models.CharField(max_length=50,null=True,blank=True)
    pic=models.FileField()

    rank=models.CharField(max_length=50,blank=True,null=True)
    badge_number=models.IntegerField(blank=True,null=True)
    age=models.IntegerField(blank=True,null=True)
    service_years=models.IntegerField(blank=True,null=True)
    # position=models.CharField(max_length=50)
    user_type=models.CharField(max_length=20)
    entry_choices=(('approved','approved'),
                   ('pending','pending'),
                   ('rejected','rejected')
    )
    entry=models.CharField(choices=entry_choices,max_length=50,default='pending',null=True,blank=True)



    def __str__(self):
        return self.username

class Case(models.Model):
    type_choices=(
        ('murder','murder'),
        ('kidnapping','kidnapping'),
        ('damaging property','damaging property'),
        ('rape','rape'),
        ('physical or mental abuse','physical or mental abuse'),
        ('theft','theft'),
        ('others','others')

    )
    type=models.CharField(choices=type_choices,max_length=50,blank=True)
    date=models.DateField()
    place=models.CharField(max_length=50)
    # culprit=models.CharField(max_length=50, null=True, blank=True)
    victim=models.CharField(max_length=50, null=True, blank=True)
    describe=models.CharField(max_length=255, null=True, blank=True)
    user=models.ForeignKey(CustomUser,related_name='my_user',on_delete=models.CASCADE)
    police=models.ForeignKey(CustomUser,related_name='assigned_police',on_delete=models.CASCADE,blank=True,null=True)
    status_choices=(('Pending','Pending'),
                    ('Case_ongoing','Case_ongoing'),
                    ('Case_Incomplete','Case_incomplete'),
                    ('Case_solved/closed','Case_solved/closed')
    )
    status=models.CharField(choices=status_choices,max_length=50,null=True,blank=True)
    feedback = models.CharField(max_length=200, null=True, blank=True)
    # def __str__(self):
    #     return self.type



class Notification(models.Model):
    notification=models.CharField(max_length=300)









