from django.db import models
from django.forms import ModelForm, TextInput, Textarea
from django import forms

# Create your models here.
class Setting(models.Model):
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )
    title = models.CharField(max_length=150)
    keywords = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    company = models.CharField(max_length=50)
    address = models.CharField(blank=True,max_length=100)
    street = models.CharField(blank=True,max_length=100)
    phone = models.CharField(blank=True,max_length=15)
    fax = models.CharField(blank=True,max_length=15)
    email = models.CharField(blank=True,max_length=50)
    smtpserver = models.CharField(blank=True,max_length=50)
    smtpemail = models.CharField(blank=True,max_length=50)
    smtppassword = models.CharField(blank=True,max_length=10)
    smtpport = models.CharField(blank=True,max_length=5)
    icon = models.ImageField(blank=True,upload_to='images/')
    logo = models.ImageField(blank=True,upload_to='images/')
    facebook = models.URLField(blank=True,max_length=50)
    instagram = models.CharField(blank=True,max_length=50)
    twitter = models.CharField(blank=True,max_length=50)
    youtube = models.CharField(blank=True, max_length=50)
    aboutus = models.TextField(blank=True, null=True)
    # # contact = RichTextUploadingField(blank=True)
    color = models.CharField(max_length=20)
    myname = models.CharField(max_length=150)
    job = models.TextField()
    my_sapo = models.TextField()
    my_description = models.TextField()
    icon_me = models.ImageField(blank=True,upload_to='images/')
    status=models.CharField(max_length=10,choices=STATUS)
    create_at=models.DateTimeField()
    update_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class SlideIcon(models.Model):
    title = models.CharField(max_length=100)
    sapo = models.CharField(max_length=500)
    icon = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class ContactMessage(models.Model):
    STATUS = (
        ('New', 'New'),
        ('Read', 'Read'),
        ('Closed', 'Closed'),
    )
    name= models.CharField(blank=False,max_length=50, help_text="Some help text" )
    email= models.EmailField(blank=False,max_length=50)
    subject= models.CharField(blank=True,max_length=50)
    messages= models.TextField(blank=True,max_length=255)
    status=models.CharField(max_length=10,choices=STATUS,default='New')
    ip = models.CharField(blank=True, max_length=20)
    note = models.CharField(blank=True, max_length=100)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class ContactForm(ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject','messages']
        widgets = {
            'name'   : forms.TextInput(
                attrs={'title': 'Your name','class':'input','type':'text','name':'register-form-name','placeholder':'Name & Surname',}),
            'subject' : forms.TextInput(
                attrs={'class':'input','name':'register-form-name','placeholder':'Subject'}),
            'email'   : forms.TextInput(
                attrs={'class':'input','name':'register-form-name','placeholder':'Email Address'}),
            'messages' : forms.Textarea(
                attrs={'class':'input','name':'register-form-name','placeholder':'Your Message','rows':'8'}),
        }

class CatalogProView(models.Model):
    title = models.CharField(max_length=50)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title

class ProductView(models.Model):
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )
    category = models.ForeignKey(CatalogProView, on_delete=models.CASCADE)  # many to one relation with Category
    title = models.CharField(max_length=150)
    description = models.TextField(max_length=255)
    image = models.ImageField(upload_to='images/home', null=False)
    status = models.CharField(max_length=10, choices=STATUS, default='False')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Blog(models.Model):
    title = models.CharField(max_length=200)
    sapo = models.CharField(max_length=350)
    thumbnail = models.ImageField(upload_to='images/blog')
    note = models.CharField(max_length=100)
    status = models.BooleanField()
    contents = models.TextField(blank=True, null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title