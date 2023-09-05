from django.shortcuts import render

def proc_imgs(request):
    return render(request, 'imgs/image_processing.html')
