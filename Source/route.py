from flask import Flask
from Model.API.getNews import *
from Model.API.searchNews import *
from Model.apiKey import ApiKey



app = Flask(__name__)

newApiKey = ApiKey()
apiKey = newApiKey.getApiKey()


@app.route('/getNews/<count>', methods = ['GET'])
def get_news(count):
    return getNews(count, apiKey)

@app.route('/searchNews/<searchQuery>/<count>', methods = ['GET'])
def search_news(searchQuery, count):
    return searchNews(searchQuery, count, "", apiKey)

@app.route('/searchNews/<searchQuery>/<count>/<searchType>', methods = ['GET'])
def search_news_with_type(searchQuery, count, searchType):
    return searchNews(searchQuery, count, searchType, apiKey)


@app.route('/')
def welcome():
    response = '''
        <html>
            <h1> Welcome to the Global News Junction </h1>
            <div>
                This is a news site. Here you will be able to read daily hot news. 
            </div>
        </html>
    '''
    return response


if __name__ == "__main__":
    app.run(debug=True)