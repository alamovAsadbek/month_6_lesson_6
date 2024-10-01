from django.urls import path

from news.views import home_page_view, contact_page_view, category_page_view, get_all_news_view, news_detail_page

app_name = 'news'

urlpatterns = [
    path('news/list/', get_all_news_view, name='list'),
    path('contact/', contact_page_view, name='contact'),
    path('<int:pk>', news_detail_page, name='news_detail_page'),
    path('', home_page_view),
]
