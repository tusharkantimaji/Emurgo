from flask import Flask, jsonify
import json
import urllib.request
import requests

from typing import Final
from dataclasses import dataclass
from requests_cache import CachedSession


def getNews(count, apiKey):
    category = "general"
    url = f"https://gnews.io/api/v4/top-headlines?category={category}&lang=en&country=us&max={count}&apikey={apiKey}"

    session = CachedSession(
        cache_name='cache/get_news',
        expire_after=600
    )

    response = session.get(url)
    return response.json()