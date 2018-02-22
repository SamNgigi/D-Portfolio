from django.shortcuts import render  # , redirect
# from django.http import HttpResponse, Http404

"""
We define all our views functions here.
"""


def index(request):
    title = "hai"
    return render(request, 'index.html', {"title": title})
