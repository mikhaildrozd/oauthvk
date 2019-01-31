from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
import requests


@login_required(login_url='/login/')
def home(request):
    name_user = request.user.social_auth.filter(provider='vk-oauth2')[0]
    if name_user:
        user_params = {
            'v': '5.92',
            'access_token': name_user.extra_data.get('access_token'),
            'count': '5',
            'order': 'random',
            'fields': ['photo_100']
        }
        response = requests.get('https://api.vk.com/method/friends.get', params=user_params).json()
        return render(request, 'signinapp/page/home.html', response)
    else:
        logout_vk(request)


def logout_vk(request):
    logout(request)
    return redirect('/')


def login_vk(request):
    if request.user.is_authenticated:
        return redirect('/')

    return render(request, 'signinapp/page/login.html')
