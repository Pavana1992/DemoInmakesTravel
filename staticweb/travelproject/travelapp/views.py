from django.shortcuts import render
from . models import Place
from . models import Team

# Create your views here.
def home(request):
    obj = Place.objects.all()
    team = Team.objects.all()
    return render(request,'index.html', {'result':obj, 'result2':team})
