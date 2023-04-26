from django.db import models
from django.contrib.auth.models import User

class User_name(models.Model):
    firstname = models.CharField(null=False, max_length=255)
    secondname = models.CharField(null=False, max_length=255, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=False, related_name='user_names')

    class Meta:
        verbose_name = 'User_name'
        verbose_name_plural = 'User_names'


class User_birth(models.Model):
    date_of_birth = models.DateField(null=True)
    place_of_birth = models.CharField(null=False, max_length=255)
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    updated_at = models.DateTimeField(auto_now=True)
    user_name = models.ForeignKey(User_name, on_delete=models.CASCADE, null=False, related_name='user_births')

    class Meta:
        verbose_name = 'User_birth'
        verbose_name_plural = 'User_births'


class User_info(models.Model):
    specialization = models.CharField(null=False, max_length=255)
    orga_of_education =  models.CharField(null=False, max_length=255)
    year_of_graduation = models.IntegerField(null=False, default=False)
    user_name = models.ForeignKey(User_name, on_delete=models.CASCADE, null=False, related_name='user_infos')

    class Meta:
        verbose_name = 'User_info'
        verbose_name_plural = 'User_infos'

class User_work(models.Model):
    address = models.CharField(null=False, max_length=255)
    organization = models.CharField(null=False, max_length=255)
    user_name = models.OneToOneField(User_name, on_delete=models.CASCADE, null=False, related_name='user_works')


    class Meta:
        verbose_name = 'User_work'
        verbose_name_plural = 'User_works'

class Practice(models.Model):
    experience = models.IntegerField(null=False, default=False)
    user_name = models.OneToOneField(User_name, on_delete=models.CASCADE, null=False, related_name='practices')

    class Meta:
        verbose_name = 'Practice'
        verbose_name_plural = 'Practices'
    
class Criminal(models.Model):
    criminal_record = models.CharField(null=False, max_length=255)
    user_name = models.OneToOneField(User_name, on_delete=models.CASCADE, null=False, related_name='criminals')

    class Meta:
        verbose_name = 'Criminal'
        verbose_name_plural = 'Criminals'

class Medicine(models.Model):
    medicine_number = models.IntegerField(null=False)
    medicine_date = models.DateField(null=True)
    user_name = models.OneToOneField(User_name, on_delete=models.CASCADE, null=False, related_name='medicines')

    class Meta:
        verbose_name = 'Medicine'
        verbose_name_plural = 'Medicines'

class Master(models.Model):
    master_degree = models.CharField(max_length=100, blank=True, null=True)

    user_name = models.OneToOneField(User_name, on_delete=models.CASCADE, null=False, related_name='masters')

    class Meta:
        verbose_name = 'Master'
        verbose_name_plural ='Masters'

class Doctor(models.Model):
    doctor_profile = models.CharField(max_length=100, blank=True, null=False)
    user_name = models.OneToOneField(User_name, on_delete=models.CASCADE, null=False, related_name='doctors')

    class Meta:
        verbose_name = 'Doctor'
        verbose_name_plural ='Doctors'

class Phd(models.Model):
    phd_record = models.CharField(null=False, max_length=255)
    user_name = models.OneToOneField(User_name, on_delete=models.CASCADE, null=False, related_name='phdes')

    class Meta:
        verbose_name = 'Phd'
        verbose_name_plural = 'Phds'

class Professor(models.Model):
     docent_professor = models.CharField(null=False, max_length=255)
     user_name = models.OneToOneField(User_name, on_delete=models.CASCADE, null=False, related_name='professors')

     class Meta:
        verbose_name = 'Professor'
        verbose_name_plural = 'Professors'

class Sport(models.Model):
    sport_degree = models.CharField(null=False, max_length=255)
    user_name = models.OneToOneField(User_name, on_delete=models.CASCADE, null=False, related_name='sports')

    class Meta:
        verbose_name = 'Sport'
        verbose_name_plural = 'Sports'

class Subject (models.Model):
   subject_of_teaching = models.CharField(null=False, max_length=255)
   user_name = models.OneToOneField(User_name, on_delete=models.CASCADE, null=False, related_name='subjects')
   
   class Meta:
        verbose_name = 'Subject'
        verbose_name_plural = 'Subjects'

class Employee (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=False)
    STATUS_CHOICES = [
        ('PR', 'Преподаватель'),
        ('DE', 'Декан'),

    ]
    status = models.CharField(
        max_length=2,
        choices=STATUS_CHOICES,
        default='ST',
    )

    class Meta:
        permissions = [('is_dean', 'Декан')]

    def is_dean(self):
        return self.status == 'DE'
