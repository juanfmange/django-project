from django.http import HttpResponse
from django.views.generic.base import View
from django.shortcuts import render

class HelloWorld(View):
    def get(self, request):
        data = {
            'name': 'juanito',
            'age': 26,
            'codes': ['python', 'go', 'js']
        }

        return render(request, 'hello_world.html', context=data)
