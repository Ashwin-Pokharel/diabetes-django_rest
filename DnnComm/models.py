from django.db import models
from django.contrib.auth.models import User
import uuid

class ModelRequest(models.Model):
    request_id = models.UUIDField(primary_key=True , default=uuid.uuid4 , editable=False)
    user = models.ForeignKey(to=User , on_delete=models.CASCADE)
    patient_id = models.IntegerField(blank=True , verbose_name="patients id")
    pregnancies = models.PositiveSmallIntegerField(blank=False , verbose_name="number of pregnancies")
    glucose = models.IntegerField(blank=False , verbose_name="blood glucose")
    blood_pressure = models.IntegerField(blank=False , verbose_name="blood pressure")
    skin_thickness = models.IntegerField(blank=False , verbose_name="skin thickness")
    insulin = models.IntegerField(blank=False , verbose_name="insulin levels")
    bmi = models.FloatField(blank=False , verbose_name="body mass index")
    dpf = models.FloatField(blank=False , verbose_name="diabetes pedigree function")
    age = models.IntegerField(blank=False , verbose_name="age")
    raw_outcome = models.FloatField(blank=True , verbose_name="raw output from model")
    expected_class_outcome = models.IntegerField(blank=True , verbose_name="binary class predicted outcome")
    actual_outcome = models.IntegerField(blank=True , verbose_name="tested outcome")




# Create your models here.
