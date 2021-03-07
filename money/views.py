from django.shortcuts import render, redirect
import random
from datetime import datetime



def index(request):
    
    if not "total" in request.session or "ledger" in request.session:
        request.session['total'] = 0
        request.session['ledger'] = ()
    
    return render(request, 'index.html')

def process(request):
    if request.method == 'GET':
        return redirect('/')
    

    if request.POST['place'] == 'farm':
        gold = random.randint(10, 20)
        message = f"you gained {gold} gold on the farm"
        result = "gain"

    if request.POST['place'] == 'cave':
        gold = random.randint(5, 10)
        message = f"you gained {gold} gold in the cave"
        result = "gain"

    if request.POST['place'] == 'house':
        gold = random.randint(2, 5)   
        message = f"you gained {gold} gold in the house"
        result = "gain"

    if request.POST['place'] == 'casino':
        gold = random.randint(-50, 50)
        if gold > 0:
            message = f"you gained {gold} gold in the casino"
            result = "gain"

        if gold < 0:
            message = f"you lost {gold} gold in the casino"
            result = "loss"

    request.session['total'] += gold
    request.session['ledger'].append({"message": message, "result": result})
    return redirect('/')

    




    
    




# Create your views here.
