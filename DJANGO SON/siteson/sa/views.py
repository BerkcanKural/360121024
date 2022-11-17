from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def index(request):
  template = loader.get_template('index.html')
  return HttpResponse(template.render())

def details(request):
  template = loader.get_template('details.html')
  return HttpResponse(template.render())

def shop(request):
  template = loader.get_template('shop.html')
  return HttpResponse(template.render())

def cart(request):
  template = loader.get_template('cart.html')
  return HttpResponse(template.render())
  
def contact(request):
  template = loader.get_template('contact.html')
  return HttpResponse(template.render())