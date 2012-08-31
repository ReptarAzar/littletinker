from django import forms
from captcha.fields import ReCaptchaField


class ContactForm(forms.Form):
	name = forms.CharField(widget=forms.TextInput(attrs={'class':'dark', 'onfocus':"this.value=''", 'id':'element_0', 'value':'Name', 'size':'80', 'class':'validate[required]'}))
	email = forms.EmailField(widget=forms.TextInput(attrs={'class':'dark', 'onfocus':"this.value=''", 'id':'element_1', 'value':'Email', 'size':'80', 'class':'validate[required]'}))
	message = forms.CharField(widget=forms.Textarea(attrs={'class':'dark', 'onfocus':"this.value=''", 'id':'element_2', 'cols':'80', 'rows':'6', 'class':'validate[required]'}))
	captcha = ReCaptchaField(attrs={'theme' : 'clean'})
