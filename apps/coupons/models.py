from django.db import models
from apps.companies.models import Company

class CurrentManager(models.Manager):
    def get_query_set(self):
        return super(CurrentManager, self).get_query_set().filter(expiration__gte=datetime.date.today())

class Coupon(models.Model):
    offer = models.CharField(max_length=100, help_text='Maximum 100 characters.')
    slug = models.SlugField(unique=True)
    description = models.TextField()
    productshot = models.ImageField(upload_to='static/productshot')	
    company = models.ForeignKey(Company)	
    expiration = models.DateTimeField()

    objects = models.Manager()
    current = CurrentManager()

    class Meta:
        verbose_name_plural = "Coupons"	
    
    def get_absolute_url(self):
        return "/%s/%s/" % (self.company.slug, self.slug)

    def __unicode__(self):
        return self.offer