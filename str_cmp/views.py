from django.shortcuts import render, redirect

def string_compare(request):
    return render(request, 'str_cmp/str_compare.html')
