
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Game
from .models import Review
from .forms import ReviewForm
from django.views import generic
# Create your views here.
@login_required
def index(request):
    game_items = Game.objects.all()

    return render(request, 'index.html', {'game_items': game_items})


#class gameDetail(generic.DetailView):
 #   model = Game
  #  template_name = 'gamepage.html'

def game_detail(request, slug):
    game = Game.objects.get(slug=slug)

    return render(request, 'gamepage.html',{'game_items': game})