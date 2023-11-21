import json
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from main.forms import ProductForm
from main.models import Item
from django.http import HttpResponse, HttpResponseNotFound
from django.core import serializers

import datetime

from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods


# Create your views here.

@login_required(login_url='/login')
def show_main(request):
    items = Item.objects.filter(user=request.user)

    jumlah_item = items.count()
    context = {
        'name': request.user.username,
        'class': 'PBP A',
        'items': items,
        'jumlah_item' : jumlah_item,
        'last_login': request.COOKIES.get('last_login'),
    }

    return render(request, "main.html", context)

def create_item(request):

    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        item = form.save(commit=False)
        item.user = request.user
        item.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_product.html", context)

def show_xml(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main")) 
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def delete_item(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    item.delete()
    return HttpResponseRedirect(reverse('main:show_main'))

def edit_item(request, id):
    item = Item.objects.get(pk = id)
    form = ProductForm(request.POST or None, instance=item)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "edit_item.html", context)

def get_product_json(request):
    product_item = Item.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', product_item))

@csrf_exempt
def add_item_ajax(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        amount = request.POST.get("amount")
        description = request.POST.get("description")
        category = request.POST.get("category")
        user = request.user

        new_product = Item(name=name, amount=amount, description=description, category=category, user=user)
        new_product.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()

@csrf_exempt
def delete_item_ajax(request, item_id):
    if request.method == 'DELETE':
        item = get_object_or_404(Item, pk=item_id)
        item.delete()
        return HttpResponse(b"DELETED", status=200)
    return HttpResponseNotFound()

@csrf_exempt
def increase_amount(request, item_id):
    if request.method == 'POST':
        item = get_object_or_404(Item, pk=item_id)
        item.amount += 1
        item.save()
        return JsonResponse({'status': 'ok', 'amount': item.amount})
    return HttpResponseNotFound()

@csrf_exempt
def decrease_amount(request, item_id):
    if request.method == 'POST':
        item = get_object_or_404(Item, pk=item_id)

        if item.amount > 0:
            item.amount -= 1
            item.save()

        if item.amount == 0:
            item.delete()

        return JsonResponse({'status': 'ok', 'amount': item.amount})
    return HttpResponseNotFound()

@csrf_exempt
def edit_item_ajax(request, item_id):
    item = get_object_or_404(Item, pk=item_id)

    if request.method == "POST":
        form = ProductForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return HttpResponse(b"UPDATED", status=200)
        else:
            return HttpResponse(b"ERROR", status=400)

    return JsonResponse(serializers.serialize('json', [item]), safe=False)

@csrf_exempt
def create_product_flutter(request):
    if request.method == 'POST':
        
        data = json.loads(request.body)

        new_product = Item.objects.create(
            user = request.user,
            name = data["name"],
            price = int(data["price"]),
            description = data["description"]
        )

        new_product.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)