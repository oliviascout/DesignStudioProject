
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import *
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
    gameid = game.id
    reviews = Review.objects.filter(game_id=gameid)

    new_review = None
    if request.method == 'POST':
        review_form = ReviewForm(data=request.POST)
        if review_form.is_valid():
            #create review but dont save to database yet
            new_review = review_form.save(commit=False)
            #assign current game to review
            new_review.game = game
            #save review to database
            new_review.save()
    else:
        review_form = ReviewForm()

    return render(request, 'gamepage.html',{'game_items': game, 'reviews': reviews, 'new_review': new_review,
                                               'review_form':review_form})

'''

def game_detail(request, slug):
    game = Game.objects.get(slug=slug)
    return render(request, 'gamepage.html',{'game_items': game})

def review_detail(request, slug):
    template_name = 'gamepage.html'
    game = get_object_or_404(Game, slug=slug)
    reviews = game.reviews
    #reviews = game.reviews.filter(heart=True)
    new_review = None
    if request.method == 'POST':
        review_form = ReviewForm(data=request.POST)
        if review_form.is_valid():
            #create review but dont save to database yet
            new_review = review_form.save(commit=False)
            #assign current game to review
            new_review.game = game
            #save review to database
            new_review.save()
    else:
        review_form = ReviewForm()
    return render(request, template_name, {'game': game,
                                               'reviews': reviews,
                                               'new_review': new_review,
                                               'review_form':review_form})



'''



