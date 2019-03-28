
# pages/views.py
from django.http import HttpResponse
import os

def index(request):

    env = ""
    for k in os.environ.keys():
        env += f"{k}={os.environ[k]}\n<br/>"

    return HttpResponse(f"""
    Hello, World!<br/>

    env:{env}
    """
    )
