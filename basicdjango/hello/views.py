from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def index(request):
  template=loader.get_template('index.html')

  #demo object like a database that send back to front 
  human = {
      'name': "bright",
      'age': 22 ,
      'food': ['water','soda','apple']

  }
  return HttpResponse(template.render(human,request))

