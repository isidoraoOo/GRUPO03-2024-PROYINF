from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

def archive(request):
    return render(request, "archive/history.html")

def main_entry(request):
    return render(request, 'archive/main_entry.html')