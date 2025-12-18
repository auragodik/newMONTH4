from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from datetime import datetime
from .models import AboutYou

def PassView(request):
    if request.method == 'GET':
        return render(request, 'base.html')

def newsPostView(request):
    posts = AboutYou.objects.all()
    return render(request, 'blog/news_list.html', {'posts': posts})


def PostDetailView(request, id):
    post = get_object_or_404(AboutYou, id=id)
    return render(request, 'blog/news_detail.html', {'post': post})


def WritersView(request):
    if request.method == 'GET':
        return HttpResponse(
            "Лев Толстой, Уильям Шекспир, Джордж Оруэлл, Марк Твэн, "
            "Джейн Остин, Эрнест Хеммингуэй, Агата Кристи, А. С. Пушкин, "
            "Чынгыз Айтматов, Федор Достоевский"
        )


def QuotesView(request):
    quotes = [
        "Фёдор Достоевский - «Красота спасёт мир.»",
        "Лев Толстой - «Все думают изменить мир, но никто не думает изменить себя.»",
        "Чингиз Айтматов - «Самое трудное для человека — быть каждый день человеком.»",
        "Джордж Оруэлл - «Свобода — это свобода говорить, что дважды два — четыре.»",
        "Эрнест Хемингуэй - «Смысл жизни — найти свой дар. Цель жизни — отдать его.»",
    ]
    html = "<h1>5 цитат великих писателей</h1><ul>"
    for q in quotes:
        html += f"<li>{q}</li>"
    html += '</ul>'
    return HttpResponse(html)


def CurrentTimeView(request):
    current_time = datetime.now()
    if request.method == 'GET':
        return HttpResponse(f'Время - {current_time}')



def book_list(request):
    books = AboutYou.objects.all()
    return render(request, 'blog/book_list.html', {'books': books})


def book_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')

        AboutYou.objects.create(title=title, author=author)

        return redirect('book_list')

    return render(request, 'blog/books_create.html')
