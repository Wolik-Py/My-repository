from django.shortcuts import render
from .models import Article, Comment
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse

def index(request):
	latest_articles_list = Article.objects.order_by('release_date')[:5]
	return render(request, 'main/index.html', {'latest_articles_list' : latest_articles_list})


def detail(request, article_id):
	try:
		a = Article.objects.get( id = article_id )
	except:
		raise Http404('Статья не найдена')

	latest_comments_list = a.comment_set.order_by('release_date_comment')[:10]

	return render(request, "main/detail.html", {'article' : a, 'latest_comments_list' : latest_comments_list})

def leave_comment(request, article_id):
	try:
		a = Article.objects.get( id = article_id )
	except:
		raise Http404('Статья не найдена')

	a.comment_set.create(author_name = request.POST['name'], comment_text = request.POST['text'], release_date_comment = request.POST['date'])

	return HttpResponseRedirect( reverse('main:detail', args = (a.id,)))