
# pages/views.py
from django.http import HttpResponse
import os

def index(request):
    return HttpResponse("""
    Hello, World!<br/>

    buildpack-notes:{}
    """.format(os.environ['NOTES'])
    )
