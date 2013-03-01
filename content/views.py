from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .forms import WriteForm
from .models import Content

def home ( request ):
    return HttpResponse ( "" )

def write ( request ):
    slug = request.GET.get ( "id", None )
    if not slug:
        content = None
    else:
        content = Content.objects.get ( slug = slug )
    if request.method == "POST":
        write_form = WriteForm ( request.POST, instance = content )
        if write_form.is_valid ( ):
            write_form.save ( )
            return HttpResponseRedirect ( "/" )
    else:
        write_form = WriteForm ( instance = content )

    context = {\
        "write_form": write_form
    }
    return render ( request, "content/write.html", context )

