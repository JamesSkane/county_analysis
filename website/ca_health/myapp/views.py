

from django.core.paginator import Paginator, EmptyPage, \
    PageNotAnInteger
from .models import Food_Desert
from django.shortcuts import render_to_response
from django.shortcuts import render
from bokeh.plotting import figure,show,output_file
from bokeh.resources import CDN
from bokeh.embed import components
from django_pandas.io import read_frame

def index(request):
    return render(request,
                  'myapp/base.html')


def detail(request):
    fds = Food_Desert.objects.all()
    return render(request,
                  'myapp/Food_Desert/detail.html',
                  {'Food_Deserts': fds})



def Food_Desert_list(request):
    fds = Food_Desert.objects.all()
    return render(request,
                  'myapp/Food_Desert/list.html',
                  {'Food_Deserts': fds})






def chart(request):
    qs = Food_Desert.objects.all()
    df = read_frame(qs)
    cols = df.columns.tolist()
    x = cols[2]
    y = cols[3]

    plot = figure(title="Food Deserts & 2010 Population")
    # fds = Food_Desert.objects.all()
    # x = Food_Desert.pop2010.value_from_object()
    # y = Food_Desert.num_fd

    plot.circle(df[x], df[y])
    plot.xaxis.axis_label = 'Population'
    plot.yaxis.axis_label = 'N Food deserts'
    script, div = components(plot)
    show(plot)
    return render_to_response('myapp/Food_Desert/chart.html',
            {'script' : script , 'div' : div} )



def county_list(request, category=None):
    fds = Food_Desert.objects.all()
    paginator = Paginator(fds, 3) # 3 posts in each page
    page = request.GET.get('page')
    try:
        fds = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        fds = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        fds = paginator.page(paginator.num_pages)
    return render(request, 'myapp/Food_Desert/list.html', {'Food_Desert': page,
                                                   'Food_deserts': fds})
