from django.db import models
from django.core.validators import MinValueValidator

landusechoices = (('Residential', 'Residential'), ('Commercial', 'Commercial'), ('Recreational', 'Recreational'), ('Industrial', 'Industrial'), ('Mixeduse', 'Mixeduse'))
position_choices = (('Inspector','Inspector'),('Recommending Officer','Recommending Officer'),('Charting Officer', 'Charting Officer'),('Approving Officer', 'Approving Officer'), ('Others', 'Others'), ('Corp Member','Corp Member'))
sex_choices = (('Male', 'Male'), ('Female','Female'))

class application(models.Model):
    sn = models.IntegerField(default=0)
    date_of_registration = models.DateField(default='01/01/2017')
    applicant = models.CharField(max_length=250)
    location = models.CharField(max_length=250)
    registration_plan_number = models.CharField(max_length=20)
    type_of_use = models.CharField(choices=landusechoices, max_length=15)
    no_of_floors = models.IntegerField()
    amount = models.IntegerField()
    treasury_receipt_number = models.CharField(max_length=25)
    inspector = models.ForeignKey('staff', related_name='staff_inspector', on_delete=models.SET_NULL, null=True)
    recommending_officer = models.ForeignKey('staff', related_name='staff_recommending_officer', on_delete=models.SET_NULL, null=True)
    charting_officer = models.ForeignKey('staff', related_name='staff_charting_officer', on_delete=models.SET_NULL, null=True)
    approving_officer = models.ForeignKey('staff', related_name='staff_approving_officer', on_delete=models.SET_NULL, null=True)
    luc_no = models.CharField(max_length=10)



class staff(models.Model):
    name = models.CharField(max_length=25)
    position = models.CharField(choices= position_choices, default='Others', max_length=100)
    sex = models.CharField(choices=sex_choices, max_length=6)
    profile_photo = models.FileField(upload_to='profile_photo', default='profile_photo')


    def __str__(self):
        return self.name









