from requests_cache import CachedSession


def searchNews(searchParam, count, field, apiKey):
    url = f"https://gnews.io/api/v4/search?q={searchParam}&lang=en&country=us&max={count}&in={field}&apikey={apiKey}"


    session = CachedSession(
        cache_name='cache/search_news',
        expire_after=600
    )

    response = session.get(url)
    return response.json()