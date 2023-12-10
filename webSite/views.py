from django.shortcuts import render
from django.http import JsonResponse
from json import JSONEncoder
from django.views.decorators.csrf import csrf_exempt
from webSite.models import User,Token,Expense,Income
from datetime import datetime
@csrf_exempt 
# Create your views here.
def submit_expense(request):
    """user submit an expense"""

    #TODO:validate data ,user might be fake,amount might be fake
    print ("request=",request)
    this_token = request.POST.get('token')
    print ("thistoken is here:",this_token)
    print ("the token is=?",this_token)
    this_user=      User.objects.filter(token__token=this_token).get()
    #TODO:user might be send new date
    if 'date' not in request.POST:
        date=datetime.now()
        date=str(date)
    Expense.objects.create(user=this_user,amount=request.POST['amount'],text=request.POST['text'],date=date)

    #print ("I'm in submit expense")
    #print (request.POST)
    return JsonResponse({
        'status':'ok',
    },encoder=JSONEncoder)
@csrf_exempt 
def submit_income(request):
    """user submit an Income"""

    #TODO:validate data ,user might be fake,amount might be fake
    print ("request=",request)
    this_token = request.POST.get('token')
    print ("thistoken is here:",this_token)
    print ("the token is=?",this_token)
    this_user=      User.objects.filter(token__token=this_token).get()
    #TODO:user might be send new date
    if 'date' not in request.POST:
        date=datetime.now()
        date=str(date)
    Income.objects.create(user=this_user,amount=request.POST['amount'],text=request.POST['text'],date=date)

    #print ("I'm in submit expense")
    #print (request.POST)
    return JsonResponse({
        'status':'ok',
    },encoder=JSONEncoder)
