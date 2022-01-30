from django.shortcuts import render


def swagger_index(request):
    return render(request, 'swagger_index.html')
