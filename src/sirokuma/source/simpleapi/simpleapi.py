import requests
from sirokuma.source import Source

class SimpleAPI(Source):
    def __init__(self, api_url):
        self.api_url = api_url

    def crawl(self):
        response = requests.get(self.api_url)
        response.raise_for_status()  # HTTPエラーが発生した場合は例外をスロー
        return response.content  # bytes型でレスポンスを返す
