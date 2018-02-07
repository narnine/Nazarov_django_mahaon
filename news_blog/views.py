from django.shortcuts import render
from django.http import HttpResponse
from .models import Article
from django.http import HttpResponseNotFound

# Create your views here.
def index(request):
    articles = Article.objects.all()
    return render(request, 'news_blog/news_list.html', {'articles': articles})

def get_article(request, article_id):
   try:
       article = Article.objects.get(id=article_id)
       author = Author.objects.filter(article__pk=article_id)
   except (Article.DoesNotExist, Author.DoesNotExist) as error:
       return HttpResponseNotFound(error)
   return render(request, 'news_blog/news_article.html',
                 {'article': article,
                  'author': author
                  }
                 )

articles = [
   {
       'id': 1,
       'title': 'First news',
       'text': 'This is the worst first article'
   },
   {
       'id': 2,
       'title': 'Second news',
       'text': 'This is the amazing second article'
   }]
