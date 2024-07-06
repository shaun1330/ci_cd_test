from django.shortcuts import render
import datetime

# Create your views here.
def index(request):
    now = datetime.datetime.now().strftime("%H:%M:%S")
    return render(request, "index.html", {"current_time": now})