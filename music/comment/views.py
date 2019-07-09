from django.shortcuts import render


# Create your views here.


def show_text(request):
    return render(request, 'comment_one.html')
