from django.shortcuts import render
from news.form import ContactModelForm
from news.models import NewsModel, NewsCollectionModel, CategoryModel


def home_page_view(request):
    carousel_news = NewsCollectionModel.objects.filter(type='carousel').first().news.all()
    most_viewed_news = NewsModel.objects.all().order_by('views_count')[:6]
    latest_news = NewsModel.objects.all().order_by('-id')[:6]
    categories = CategoryModel.objects.all()

    context = {
        "carousel_news": carousel_news,
        "most_viewed_news": most_viewed_news,
        "latest_news": latest_news,
        "categories": categories
    }
    return render(request, 'index.html', context)


def news_detail_page(request, pk):
    news = NewsModel.objects.filter(pk=pk)
    if news.exists():
        news = news.first()
        news.views_count += 1
        news.save()
        context = {"news": news}
        return render(request, 'news_detail.html', context)
    return render(request, '404.html')


def single_page_view(request):
    return render(request, 'news_detail.html')


def contact_page_view(request):
    if request.method == 'POST':
        form = ContactModelForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'contact_success.html')
        else:
            context = {"errors": form.errors}
            return render(request, 'contact.html', context)
    else:
        return render(request, 'contact.html')


def category_page_view(request):
    return render(request, 'category.html')


def get_all_news_view(request):
    q = request.GET.get('q')
    cat = request.GET.get('cat')
    news = NewsModel.objects.filter(status=True)
    if q:
        news = news.filter(title__icontains=q)
    if cat:
        news = news.filter(categories__exact=cat)

    context = {"news_list": news}
    return render(request, 'category.html', context)
