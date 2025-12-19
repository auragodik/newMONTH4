from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from datetime import datetime
from .models import AboutYou
from .forms import BookSearchForm
from django.core.paginator import Paginator

def PassView(request):
    return render(request, 'base.html')

def newsPostView(request):
    posts = AboutYou.objects.all()
    return render(request, 'blog/news_list.html', {'posts': posts})

def PostDetailView(request, id):
    post = get_object_or_404(AboutYou, id=id)
    return render(request, 'blog/news_detail.html', {'post': post})

def WritersView(request):
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
    return HttpResponse("<h1>Цитаты</h1>" + "<br>".join(quotes))

def CurrentTimeView(request):
    return HttpResponse(f'Время - {datetime.now()}')



def book_list(request):
    books = AboutYou.objects.all().order_by('-id')
    form = BookSearchForm(request.GET or None)

    if form.is_valid():
        query = form.cleaned_data.get('query')
        if query:
            books = (
                AboutYou.objects.filter(title__icontains=query)
                | AboutYou.objects.filter(author__icontains=query)
            )

    paginator = Paginator(books, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'blog/book_list.html', {
        'page_obj': page_obj,
        'form': form
    })

def book_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        AboutYou.objects.create(title=title, author=author)
        return redirect('book_list')
    return render(request, 'blog/books_create.html')
