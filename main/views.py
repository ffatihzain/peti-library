from django.shortcuts import render

# Create your views here.

def show_main(request):
    context = {
        'name': 'Muhammad Fatih Zain',
        'class': 'PBP A',
    }

    return render(request, "main.html", context)