from django.shortcuts import render


def handler404(request, exception):
    return render(request, 'errors/_404.html', status=404)

def handler500(request):
    return render(request, 'errors/_500.html', status=500)