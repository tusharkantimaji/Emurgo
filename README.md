This is a news Application Backend. 

Technical Requirement.
1. We need to install Python in local machine. So, Install Python Latest Version First
2. pip install flask
3. pip install request-cache
4. If anything more is required, Just run the command `pip install <ModuleName>`


As of now we are supporting couple of Features.
1. Domain/getNews/<NumberOfNews(1-100)>
        This URL is for getting the news list for the feed portion
2. Domain/searchNew/<SearchParam>/<NumberOfNews(1-100)>
        This URL is for getting the news with a searchParam
3. Domain/searchNew/<SearchParam>/<NumberOfNews(1-100)>/title
        This URL is same like point 2, but, it will search on the title
3. Domain/searchNew/<SearchParam>/<NumberOfNews(1-100)>/description
        This URL is same like point 2, but, it will search on the description