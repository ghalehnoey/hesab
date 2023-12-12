from django.shortcuts import render
from django.http import JsonResponse
from json import JSONEncoder
from django.views.decorators.csrf import csrf_exempt
from webSite.models import User,Token,Expense,Income
from datetime import datetime
from django.shortcuts import render
#Random STR
from django.utils.crypto import get_random_string
#Registrations
from django.contrib.auth.models import User
from django.shortcuts import render
from .forms import RegistrationForm
from .models import Token


# create random string for Toekn
random_str = lambda N: ''.join(
    random.SystemRandom().choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(N))

def index(request):
    context={}
    return render(request,'index.html',context)

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # Create a new user
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            
            new_user = User.objects.create_user(username=username, email=email, password=password)
            
            # Create a token for the new user
            token_code = get_random_string(length=32)
            token = Token.objects.create(user=new_user, token=token_code)
            
            return render(request, 'registration_success.html')  # Redirect to success page
    else:
        form = RegistrationForm()

    return render(request, 'registration_view.html', {'form': form})


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
