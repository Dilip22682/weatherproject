from django.shortcuts import render,HttpResponse
import requests 
import datetime

# Create your views here.
def home(request):
    if 'city' in request.POST:
        city = request.POST['city']
        url=f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=ef714887a4bcaf252cf30afa684310af'
        params={'units':'metric'}
        data=requests.get(url,params).json()
        print(data)
        
        
        try:
            print("params:",params)
            
            description=data['weather'][0]['description']
            icon=data['weather'][0]['icon']
            temp=data['main']['temp']
            city=data['name']
            wind=data['wind']['speed']
            country=data['sys']['country']
            day=datetime.date.today()
            print("day------->:",day)
            context={
                    'data':data,
                    'description':description,
                    'icon':icon,
                    'temp':temp,
                    'date':day,
                    'city':city,
                    'wind':wind,
                    'country':country,
                    
            }
        
            return render(request,'index.html',context)
        except:
            context={
                    'city1':'City is not found in the world(API)'
            }
            return render(request,'index.html',context)
    else:
        context1={
        #             'city':'varansi',
        #             'description':description,
        #             'icon':icon,
        #             'temp':temp,
        #             'date':day,
            }
        return render(request,'index.html',context1)
        