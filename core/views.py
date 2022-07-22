from django.shortcuts import render, redirect
from .forms import *
from .ml_code import MLCode
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from .models import *


@csrf_exempt
def home(request):

    if request.method == 'POST':
        form = InputDataForm(request.POST, request.FILES)

        if form.is_valid():
            model_data = form.save()
            return redirect('result', id=model_data.pk)

    else:
        form = InputDataForm()

    return render(request, 'index.html', {'form': form})


def result(request, id):

    model_data = get_object_or_404(MLModelData, id=id)

    user = model_data.user
    file = model_data.file
    try:
        cluster, *infected = MLCode().contactTracing(user, file)
    except AssertionError:
        context = {
            "model_data": model_data,
            "msg": "User doesn't exist",
        }
        return render(request, 'result1.html', context=context)

    context = {
        "model_data": model_data,
        'cluster': cluster,
        'infected': infected
    }

    return render(request, 'result.html', context=context)
