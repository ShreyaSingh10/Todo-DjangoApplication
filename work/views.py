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
