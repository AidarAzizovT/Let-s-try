from django.http import HttpResponse
from django.shortcuts import render
from .models import Article, Comment
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
latest_articles_list = Article.objects.order_by('pub_date')
def index(request):
    return HttpResponse("Here will be great website on June")

def test(request):
    return HttpResponse("Test page")

def main_page(request):
    return render(request, 'articles/list.html', {'latest_articles_list' : latest_articles_list})

def figma (request):
    return render(request, 'WebSiteWithFigma/index.html')

def detail(request, article_id):
    try:
        a = Article.objects.get(id = article_id)
    except:
        raise Http404("Page not found")
    latest_comments_list = a.comment_set.order_by('-id')[:10]
    return render(request, 'articles/detail.html', {'article': a, 'latest_comments_list':latest_comments_list })

def leave_comment(request, article_id):
    try:
        a = Article.objects.get(id = article_id)
    except:
        raise Http404("Page not found")

    a.comment_set.create(comment_author = request.POST['Name'], comment_text = request.POST['Text'])
    return HttpResponseRedirect(reverse('articles:detail', args=(a.id,)))