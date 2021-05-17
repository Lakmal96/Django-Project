from django.shortcuts import render

# Create your views here.


def customized_order(request):
    return render(request, 'customized/customized_form.html', {})
