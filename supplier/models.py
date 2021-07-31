from django.db import models

class oxygensuppliers(models.Model):
    groupname=models.CharField(max_length=40,default='')
    name_of_supplier=models.CharField(max_length=20,default='')
    district=models.CharField(max_length=40,default='')
    phone_number=models.IntegerField()

    def __str__(self):
        return self.groupname

