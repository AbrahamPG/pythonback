from django.shortcuts import render

# Create your views here.



def app1_list(request):

    data_context = {
        'nombre': 'Katy Paredes',
        'edad': 20,
        'dni': '74096065',
        'pais': 'Peru',
        'vigente': False,
    }

    return render(request, 'app1_list.html', context={'data': data_context})