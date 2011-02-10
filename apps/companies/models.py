from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=300)
    slug = models.SlugField(unique=True)
    street = models.CharField(max_length=500, help_text='Street Address')
    city = models.CharField(max_length=100, help_text='City')
    state = models.CharField(max_length=100, help_text='2 Letter Abbreviation')	
    zipcode = models.IntegerField(help_text='Zipcode')	
    logo = models.ImageField(upload_to='static/logo')	

    class Meta:
        verbose_name_plural = "Companies"	

    def __unicode__(self):
        return self.name	