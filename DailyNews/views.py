import requests
from django.shortcuts import render,HttpResponse

def home(request):
    country="in"
    category="business"

    api=f"https://newsapi.org/v2/top-headlines?country={country}&category={category}&apiKey=9bf9b3d682f142259e66b346a06d85ab"

    data=requests.get(api)

    data=data.json()

    if data['articles'] == [] :
        return render(request,'index.html',{'error':True})
    else :
        return render(request,'index.html',{'data':data.get('articles'),'error':False})

def usa(request):
    country="us"
    category="business"

    api=f"https://newsapi.org/v2/top-headlines?country={country}&category={category}&apiKey=9bf9b3d682f142259e66b346a06d85ab"

    data=requests.get(api)

    data=data.json()

    if data['articles'] == [] :
        return render(request,'usa.html',{'error':True})
    else :
        return render(request,'usa.html',{'data':data.get('articles'),'error':False})

def tesla(request):

    api=f"https://newsapi.org/v2/everything?q=tesla&from=2022-08-08&sortBy=publishedAt&apiKey=9bf9b3d682f142259e66b346a06d85ab"

    data=requests.get(api)

    data=data.json()

    if data['articles'] == [] :
        return render(request,'tesla.html',{'error':True})
    else :
        return render(request,'tesla.html',{'data':data.get('articles'),'error':False})

def TechCrunch(request):

    api=f"https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=9bf9b3d682f142259e66b346a06d85ab"

    data=requests.get(api)

    data=data.json()

    if data['articles'] == [] :
        return render(request,'TechCrunch.html',{'error':True})
    else :
        return render(request,'TechCrunch.html',{'data':data.get('articles'),'error':False})

def Wall_Street_Journal(request):

    api=f"https://newsapi.org/v2/everything?domains=wsj.com&apiKey=9bf9b3d682f142259e66b346a06d85ab"

    data=requests.get(api)

    data=data.json()

    if data['articles'] == [] :
        return render(request,'Wall_Street_Journal.html',{'error':True})
    else :
        return render(request,'Wall_Street_Journal.html',{'data':data.get('articles'),'error':False})

def Apple(request):

    api=f"https://newsapi.org/v2/everything?q=apple&from=2022-09-07&to=2022-09-07&sortBy=popularity&apiKey=9bf9b3d682f142259e66b346a06d85ab"

    data=requests.get(api)

    data=data.json()

    if data['articles'] == [] :
        return render(request,'Apple.html',{'error':True})
    else :
        return render(request,'Apple.html',{'data':data.get('articles'),'error':False})





# Apple="https://newsapi.org/v2/everything?q=apple&from=2022-09-07&to=2022-09-07&sortBy=popularity&apiKey=9bf9b3d682f142259e66b346a06d85ab"