from django.shortcuts import render


def user_list(request):
    return render(request, 'user/user_list.html')
