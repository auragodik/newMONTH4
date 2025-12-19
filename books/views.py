from django.views import View
from django.views.generic import ListView, DetailView
from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime
from .models import AboutYou
from .forms import BookSearchForm
from django.core.paginator import Paginator
from django.db.models import Q

class PassView(View):
    def get(self, request):
        return render(request, 'base.html')


class NewsPostView(ListView):
    model = AboutYou
    template_name = 'blog/news_list.html'
    context_object_name = 'posts'


class PostDetailView(DetailView):
    model = AboutYou
    template_name = 'blog/news_detail.html'
    pk_url_kwarg = 'id'
    context_object_name = 'post'


class WritersView(View):
    def get(self, request):
        return HttpResponse(
            "Лев Толстой, Уильям Шекспир, Джордж Оруэлл, Марк Твэн, "
            "Джейн Остин, Эрнест Хеммингуэй, Агата Кристи, А. С. Пушкин, "
            "Чынгыз Айтматов, Федор Достоевский"
        )


class QuotesView(View):
    def get(self, request):
        quotes = [
            "Фёдор Достоевский - «Красота спасёт мир.»",
            "Лев Толстой - «Все думают изменить мир, но никто не думает изменить себя.»",
            "Чингиз Айтматов - «Самое трудное для человека — быть каждый день человеком.»",
            "Джордж Оруэлл - «Свобода — это свобода говорить, что дважды два — четыре.»",
            "Эрнест Хемингуэй - «Смысл жизни — найти свой дар. Цель жизни — отдать его.»",
        ]
        return HttpResponse("<h1>Цитаты</h1>" + "<br>".join(quotes))


class CurrentTimeView(View):
    def get(self, request):
        return HttpResponse(f'Время - {datetime.now()}')


class BookListView(View):
    def get(self, request):
        books = AboutYou.objects.all().order_by('-id')
        form = BookSearchForm(request.GET or None)
        if form.is_valid():
            query = form.cleaned_data.get('query')
            if query:
                books = AboutYou.objects.filter(
                    Q(title__icontains=query) | Q(author__icontains=query)
                )

        paginator = Paginator(books, 2)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        return render(request, 'blog/book_list.html', {
            'page_obj': page_obj,
            'form': form
        })


class BookCreateView(View):
    def get(self, request):
        return render(request, 'blog/books_create.html')

    def post(self, request):
        title = request.POST.get('title')
        author = request.POST.get('author')
        AboutYou.objects.create(title=title, author=author)
        return redirect('book_list')
