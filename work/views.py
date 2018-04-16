from django.shortcuts import render
from django.http import HttpResponse
from .models import Todos

def index(request):
	"""return HttpResponse("Hey der! Let's do some work")"""
	todos = Todos.objects.all()[:10]
	context = {
		'todos': todos
	}
	return render(request, 'index.html', context)

def details(request, id):
	todos = Todos.objects.get(id = id)

	context = {
		'todos' :todos
	}
	return render(request, 'details.html', context)

"""here Todos is the name  of the model we created"""
"""this id is same as the id we gave in urls.py"""

