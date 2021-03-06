from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

class Category(models.Model):
	"""docstring for Category"""
	name=models.CharField(max_length=128,unique=True)
	views=models.IntegerField(default=0)
	likes=models.IntegerField(default=0)
	slug=models.SlugField(default=' ')

	def save(self, *args, **kwargs):
		# Uncomment if you don't want the slug to change every time the name changes
        #if self.id is None:
             #self.slug = slugify(self.name)
		self.slug=slugify(self.name)
		super(Category,self).save(*args,**kwargs)    
	def __unicode__(self):
		return self.name

	class Meta:
		verbose_name_plural= "Categories"
		
		
class Page(models.Model):
	"""docstring for Page"""
	category=models.ForeignKey(Category, on_delete= models.CASCADE)
	title=models.CharField(max_length=128)
	url=models.URLField()
	views=models.IntegerField(default=0)
	slug =models.SlugField(default='')

	def save(self,*args,**kwargs):
		self.slug=slugify(self.title)
		super(Page,self).save(*args,**kwargs)

	def __unicode__(self):
		return self.title

	class Meta:
		verbose_name_plural= "Pages"

# Add a user profile
class UserProfile(models.Model):
	# Needed to UserProfile to User model instance
	user = models.OneToOneField(User)
	website = models.URLField(blank=True)
	picture = models.ImageField(upload_to = 'profile_images',blank=True)

	def __unicode__(self):
		return self.user.username


		
		

		