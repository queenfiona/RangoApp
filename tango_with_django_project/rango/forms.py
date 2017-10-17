from django import forms
from rango.models import Category,Page

class CategoryForm(forms.ModelForm):
	name=forms.CharField(max_length=128,help_text="Please enter the category name.")
	views=forms.IntegerField(widget=forms.HiddenInput(),initial=0)
	likes=forms.IntegerField(widget=forms.HiddenInput(),initial=0)
	slug=forms.CharField(widget=forms.HiddenInput(),required=False)

	def clean(self):
		cleaned_data=super(CategoryForm,self).clean()
		name=cleaned_data.get('name')
		if name:
			raise forms.ValidationError("The name exist,enter different one.")
		elif name == ' ':
			raise forms.ValidationError(" Cannot submit an empty field ,enter a category")
		else:
			raise forms.ValidationError("Category does not exist")

		return cleaned_data

	class Meta:
		# Provide an association between the ModelForm and a model
		model=Category
		fields=('name',)

class PageForm(forms.ModelForm):
	title=forms.CharField(max_length=128,help_text="Please enter the title of the page.")
	url=forms.URLField(max_length=200,help_text="Please enter the url of the page.")
	views=forms.IntegerField(widget=forms.HiddenInput(),initial=0,required=False)
	slug=forms.CharField(widget=forms.HiddenInput(),required=False)

	def clean(self):
		cleaned_data=self.cleaned_data
		url=cleaned_data.get('url')
		# If url is not empty and doesn't start with 'http://', prepend 'http://'.
		if url and not url.startswith('http://'):
			url = ('http://') + url
			cleaned_data['url']=url
		return cleaned_data


	class Meta:
		model=Page
		exclude=('category',)

