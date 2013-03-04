from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from pdb import set_trace as bp
from .forms import WriteForm
from .models import Content

def home ( request ):
    return HttpResponse ( "" )

def all ( request ):
    context = {\
        "contents": Content.objects.filter ( user = request.user )
    }
    return render ( request, "content/all.html", context )

def view ( request, user, path ):
    user = User.objects.get ( username = user )
    content = Content.objects.get ( user = user, slug = path )
    context = {\
        "user": user,
        "path": path,
        "content": content,
    }
    return render ( request, "content/view.html", context )

@login_required
def write ( request, path ):
    if not path:
        content = None
    else:
        content = Content.objects.get ( slug = path )
    if request.method == "POST":
        write_form = WriteForm ( request.POST, instance = content )
        if write_form.is_valid ( ):
            write_form.instance.user = request.user
            write_form.save ( )

            return HttpResponseRedirect ( \
                reverse ( "content_view", \
                          args = ( write_form.cleaned_data['slug'], ) ) )
    else:
        write_form = WriteForm ( instance = content )

    context = {\
        "write_form": write_form,
    }
    return render ( request, "content/write.html", context )

