from django.db import models

class Category(models.Model):
	"""docstring for Category"""
	name=models.CharField(max_length=128,unique=True)
	views=models.IntegerField(default=0)
	likes=models.IntegerField(default=0)
    
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

	def __unicode__(self):
		return self.title

	class Meta:
		verbose_name_plural= "Pages"

class PageAdmin(object):
	"""docstring for PageA"""
	def __init__(self, arg):
		super(PageA, self).__init__()
		self.arg = arg
		
		

		