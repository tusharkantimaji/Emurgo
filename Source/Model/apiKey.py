
class ApiKey:
    
    #this is hard coded API key for getting the news for my account
    def __init__(self):
        self.apiKey = "d138fffdf0a61a8c735f8b56edd85ab6" 

    def getApiKey(self):
        return self.apiKey
    
    def setApiKey(self, key):
        self.apiKey = key