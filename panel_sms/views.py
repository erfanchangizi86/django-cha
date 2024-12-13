from django.shortcuts import render

# Create your views here.

from django import views

class HomeView(views.View):
    def get(self, request):
        products = [{'product':'mobile','price':30},{'product':'laptap','price':3320},{'product':'tablet','price':3000},{'product':'test','price':120}]
        return render(request, 'home.html',context={'products':products})
    