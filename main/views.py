from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2306215154',
        'name': 'Raden Ahmad Yasin Mahendra',
        'class': 'PBP F'
    }

    return render(request, "main.html", context)