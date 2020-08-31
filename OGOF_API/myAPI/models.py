from django.db import models
from django.core.validators import RegexValidator
from django_countries.fields import CountryField


# Create your models here.
class DeveloperContacts(models.Model):
	name = models.CharField(max_length = 50)
	phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
	phone_contact = models.CharField(validators=[phone_regex], max_length=17, blank=False, null=True)
	email =models.EmailField()
	country = CountryField()
	BACKEND_DEVELOPER = 'backend_developer'
	FRONTEND_DEVLOPER = 'frontend_developer'
	FULLSTACK_DEVELOPER = 'fullstack_developer'
	developer_type =[
	(BACKEND_DEVELOPER,'backend_developer'),
	(FRONTEND_DEVLOPER, 'frontend_developer'),
	(FULLSTACK_DEVELOPER, 'fullstack_developer'),
	]
	developer_category=models.CharField(max_length=250, choices=developer_type, default=FRONTEND_DEVLOPER,)

	def __str__(self):
		return self.name

