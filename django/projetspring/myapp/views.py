import json
from datetime import timezone, date

from django.contrib import messages
from django.shortcuts import render, redirect

import requests

# Create your views here.
from myapp.forms import signupform, SymptomsForm



def val():
    pass
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        passwrd = request.POST.get('password')
        user={'username':username,'password':passwrd}
        try:

            x = requests.post('http://127.0.0.1:8080/api/users/login', json=user)
            print("statut:",x.status_code)
            # print(x.text)
            if x.status_code==200:
                result = json.loads(x.text)
                # print("resultat:",result)
                print(result['id'])
                idd=result["id"]

                global val
                def val():
                    if idd is not None:
                        return idd


                return redirect('home')


            else:
                messages.error(request, "l'utilisateur ou mot de passe  erroné")
        except:
            messages.error(request, "l'utilisateur ou mot de passe  erroné")

    context = {}
    return render(request, 'login.html', context)

def signup(request):
    form=signupform()
    if request.method == 'POST':
        form=signupform(request.POST)
        if form.is_valid():
            # convert the form data to a dictionary:
            form_data = form.cleaned_data
            # convert the dictionary to JSON:

            print(form_data)
            print(type(form_data))
            x = requests.post('http://127.0.0.1:8080/api/users/createUser', json=form_data)
            print(x.status_code)
            print(x.text)

            # return a JSON response:
            #return JsonResponse({'data': json_data})
    context = {'form': form}
    return render(request, 'signup.html',context )

def home(request):
    a=val()

    form=SymptomsForm()
    if request.method == 'POST':
        form=SymptomsForm(request.POST)
        if form.is_valid():
            # convert the form data to a dictionary:
            form_data = form.cleaned_data
            tableau=[]
            # convert the dictionary to JSON:
            for i in form_data:
                if form_data[i]=='yes'or form_data[i]=='Yes' :
                    tableau.append(1)
                else:
                    tableau.append(0)
            jsonne={"symptoms":tableau}
            x = requests.post('http://127.0.0.1:5000/prediction', json=jsonne)
            result = json.loads(x.text)
            #print(result)
            illness=result['result']
            print(illness)
            jayson={"user_id":str(a),"result":illness,"createdDate":str(date.today())}
            # x = requests.post('http://127.0.0.1:8080/userHistories', json=jayson)
            # print(x.status_code)
            # print(x.text)
            y=requests.get("http://127.0.0.1:8080/userHistories")
            result = y.json()["_embedded"]["userHistories"]
            print("result",result)
            context={'maladie':illness,"tableau":result}
            return render(request, 'home2.html',context)




    context = {'form': form}
    return render(request, 'home.html',context )

