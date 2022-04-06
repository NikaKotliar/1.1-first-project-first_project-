from django.shortcuts import render

from articles.models import Article


def articles_list(request):
    template = 'articles/news.html'
    object_list = Article.objects.all()
    for article in object_list:
        print(article.image)
        print(article.title)
        print(article.text)
        a = article.article_info.all()
        for i in a:
            print(i.tag_pos)
    context = {
        'object_list': object_list
    }

    return render(request, template, context)
