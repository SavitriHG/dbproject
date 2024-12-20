from django.db import models

# Create your models here.
class User(models.Model):
	tuid = models.CharField(max_length=30)
	tuname = models.CharField(max_length=30)
	tuemail = models.EmailField(max_length=30)
	tucontact = models.CharField(max_length=30)

	class Meta:
		db_table = "user"

	