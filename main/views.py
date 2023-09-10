from django.shortcuts import render

# Create your views here.

def show_main(request):
    context = {
        'name': 'The Art of War',
        'amount': '40',
        'description': 'Written by Sun Tzu',
        'category': 'Military Art'
    }

    return render(request, "main.html", context)