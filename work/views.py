from django.shortcuts import render,redirect
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

def add(request):
	if(request.method == 'POST'):
		title = request.POST['title']
		text = request.POST['text']
		todo = Todos(title=title, text=text)
		todo.save()
		print("in add")
		return redirect('/work')
	else:
		return render(request, 'add.html')

def delete(request, id):
	if(request.method == 'POST'):
		#print("in delete")
		Todos.objects.filter(id = id).delete()
		
		return redirect('/work')
	return render(request,'delete.html', {"id": id})
		#todos.delete()	
    
	#return redirect('/work')
	#else:
		#return HttpResponse("Could not delete the post")

"""here Todos is the name  of the model we created"""
"""this id is same as the id we gave in urls.py"""

