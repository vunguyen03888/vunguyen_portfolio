from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import SlideIcon, Blog, Setting, ContactMessage, ContactForm, ProductView, CatalogProView
from django.contrib import messages
# Create your views here.

def index(request):
    if request.method == 'POST': # check post
        form = ContactForm(request.POST)
        if form.is_valid():
            data = ContactMessage() #create relation with model
            data.name = form.cleaned_data['name'] # get form input data
            data.email = form.cleaned_data['email']
            data.subject = form.cleaned_data['subject']
            data.messages = form.cleaned_data['messages']
            data.save()  #save data to table
            messages.success(request,"Thank you for your message.")
            return HttpResponseRedirect('#contact')
            # return HttpResponseRedirect('/')
    else:
        product1 = ProductView.objects.filter(category__pk=1).order_by('-update_at')[:3]
        product2 = ProductView.objects.filter(category__pk=2)
        product3 = ProductView.objects.filter(category__pk=3)
        setting = Setting.objects.all()
        form = ContactForm()
        blogs = Blog.objects.order_by('-update_at')[:3]
        slidericon = SlideIcon.objects.all()
        context = {
            'setting': setting,
            'form':form,
            'product1':product1,
            'product2':product2,
            'product3':product3,
            'blogs': blogs,
            'slidericon':slidericon,

        }
        return render(request,'home/index.html', context)

def blog(request):
    setting = Setting.objects.all()
    form = ContactForm()
    blogs = Blog.objects.all()
    context = {
        'setting': setting,
        'form': form,
        'blogs': blogs,
    }
    return render(request,'home/blog-grid.html', context)

def blog_single(request,id):
    setting = Setting.objects.all()
    form = ContactForm()
    blog = Blog.objects.get(pk=id)
    context = {
        'setting': setting,
        'form': form,
        'blog':blog,
    }
    return render(request, 'home/blog-single.html', context)