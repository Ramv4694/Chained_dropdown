from django.shortcuts import render
from django.http import HttpResponse
from .models import Country,City,District
import pdb
import json,ast
# Create your views here.
def country_list(request,template_name="file.html"):

    all_countries = Country.objects.all()


    return render(request,template_name,{"countries":all_countries})

def Ajaxcall(request):
    if request.method == "POST":
        print("hello from ajax")
        country_id = request.POST.get('value')
        cid = country_id.encode('ascii', 'ignore')

        cities=City.objects.filter(country__id=cid[1]).order_by('name').values('name','pk')
        print cities
        str1 = []
        for city in cities:
            currentcity = city['name']
            currentcityint = city['pk']
            currentcitypk = str(currentcityint)
            str1.append("<option name = \'" + currentcity + "\' value = \'" + currentcitypk + '\'' + "> " + currentcity +"</option>")

        print(str1)

        data = str1

        return HttpResponse(data)


def Ajaxcall_district(request):
    if request.method == "POST":
        print("hello from ajax_District")
        city_id = request.POST.get('value')
        cid = city_id.encode('ascii', 'ignore')
        cint = int(cid[1])


        Districts=District.objects.filter(city__id=cint).order_by('name').values('name')
        print Districts
        str2 = []
        for Dis in Districts:
            currentdistrict = Dis['name']
            str2.append("<option name = \'" + currentdistrict + "\' value = \'" + currentdistrict + '\'' + "> " + currentdistrict +"</option>")

        print(str2)

        response2 = str2

        return HttpResponse(response2)

def Ajaxcallcountry(request):
    if request.method == "POST":
        country_name = request.POST.get('value')
        country_n = country_name.encode('ascii', 'ignore')
        c_n = country_n[1:]
        finalc = c_n.replace('"',"")
        finalc_str = str(finalc)

        #finalc = ("%s" %(repr(country_n)[1:-1]))


        print(country_name)




        str3 = []
        if(country_name == u'""'):

            print("nothing")
            result= []

        else:
            result = Country.objects.filter(name__contains=finalc_str).values('name')
        for r in result:
            r1 = r['name'].encode('ascii', 'ignore')


            str3.append("<li>" + r1 + "</li>")
        print(str3)


        return HttpResponse(str3)
