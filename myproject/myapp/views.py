from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404
from .models import TopSellingProducts, Cards, Profile_Detail
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.


def index(request):
    topSelling = TopSellingProducts.objects.all()
    details = Profile_Detail.objects.all()
    detail = {'detail1': details[0]}
    # topSellings = [topSelling1, topSelling2, topSelling3, topSelling4, topSelling5]
    topSellings = {'topSelling1': topSelling[0], 'topSelling2': topSelling[1], 'topSelling3': topSelling[2], 'topSelling4': topSelling[3], 'topSelling5': topSelling[4]}
    return render(request, 'index.html', topSellings)


def Card(request):
    cards = Cards.objects.all()
    card = {'card1': cards[0]}
    return render(request, 'components-cards.html', card)


# def getNumber(request, id):
#     if id >= 5:
#         return HttpResponse(f"Id={id}")
#     else:
#         raise Http404()
#
#
# def counter(request):
#     text = request.POST['text']
#     amount_of_words = len(text.split())
#     return render(request, 'counter.html', {'amount': amount_of_words})


def Profile(request):
    details = Profile_Detail.objects.all()
    detail = {'detail1': details[0]}
    return render(request, 'users-profile.html', detail)


def Register(request):
    if request.method == 'POST':
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        if User.objects.filter(email=email).exists():
            messages.info(request, 'Email Already Used')
            return redirect('register', permanent=True)
        elif User.objects.filter(username=username).exists():
            messages.info(request, 'Username Already Used')
            return redirect('register', permanent=True)
        else:
            user = User.objects.create_user(email=email, username=username, password=password)
            user.save()
            return redirect('login')

    else:
        return render(request, 'pages-register.html')


def Login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/', permanent=True)
        else:
            messages.info(request, 'Credentials Invalid')
            return redirect('login', permanent=True)
    else:
        return render(request, 'pages-login.html')


def Logout(request):
    auth.logout(request)
    return redirect('/')


def Post(request, pk):
    return render(request, 'post.html', {'pk': pk})


def Func2(request, high):
    return HttpResponse(f"<h1>Hello World</h1> <h1>{high}</h1>")


def PageNotFound(request, exception):
    return HttpResponseNotFound("PageNotFound")
