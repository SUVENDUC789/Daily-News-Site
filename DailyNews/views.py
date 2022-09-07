import imp
import requests
from django.shortcuts import render,HttpResponse

def home(request):
    data=requests.get("https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=9bf9b3d682f142259e66b346a06d85ab")

    data=data.json()
    
    # try:
    #     for i in range(data['totalResults']):
    #         print("SL : ",i+1)
    #         print("Title :>\n",data['articles'][0]['title'])
    #         print(50*"*")
    #         print(data['articles'][i]['author'])
    #         print(50*"*")
    #         print(data['articles'][i]['description'])
    #         print(50*"*")
    #         print(data['articles'][i]['url'])
    #         print(50*"*")
    #         print(data['articles'][i]['urlToImage'])
    #         print(50*"*")
    #         print(data['articles'][i]['content'])
    #         print(50*"*")
    #         print(data['totalResults'])
    #         print(50*"*")
    # except:
    #     print("News is end !")
    # print(len(data))

    return render(request,'index.html',{'data':data['articles']})