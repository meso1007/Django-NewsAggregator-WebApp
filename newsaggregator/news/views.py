from django.shortcuts import render
from .scraper import get_news_data  # スクレイピング関数をインポート

def news_list(request):
    data = get_news_data()
    return render(request, 'news/news_list.html', {
        'news_data': data['news_data'],
        'reversed_news_data': data['reversed_news_data']
    })
