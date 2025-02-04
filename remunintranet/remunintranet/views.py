from django.http import HttpResponse

def homepage(request):
    return HttpResponse("yep")


def about(request):
    return HttpResponse("aqui esta el about")