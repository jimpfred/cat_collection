from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render
from .models import Cat

# Create your views here.
def home(request):
    return render(request, 'home.html')
def about(request):
    return render(request, 'about.html')
def cats_index(request):
    cats = Cat.objects.all()  #db call
    return render(request, 'cats/index.html', {'cats': cats })

def cats_detail(request, cat_id):
    cat = Cat.objects.get(id=cat_id)
    return render(request, 'cats/detail.html', {'cat': cat})

class CatCreate(CreateView):
    model = Cat
    fields = '__all__'

class CatUpdate(UpdateView):
    model = Cat
    fields = ['breed', 'description', 'age']

class CatDelete(DeleteView):
    model = Cat
    success_url = '/cats/' # once cat deleted dont go to detail pagr, override to detail