from django.shortcuts import render

from base_module.models import Genre, Article

def base(request):
	genres = Genre.objects.all()
	article_preview = Article.objects.order_by('-last_update').all()

	context = {
		'genres': genres,
		'article_preview': article_preview
	}

	return render(request, 'base.html', context = context)

def article(request, pk):
	genres = Genre.objects.all()
	game = Article.objects.get(pk = pk)

	context = {
		'genres': genres,
		'game': game
	}

	return render(request, 'article.html', context = context)