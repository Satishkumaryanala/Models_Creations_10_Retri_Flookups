from django.shortcuts import render
from app.models import *
from django.db.models.functions import Length
# Create your views here.

def display_topic(request):
    QSTO = Topic.objects.all()
    d={'TO':QSTO}
    return render(request,'display_topic.html',d)


def dispaly_webpage(request):
    QSWO = webpage.objects.all()
    QSWO = webpage.objects.order_by('topic_name')

    QSWO = webpage.objects.order_by('-name')

    QSWO = webpage.objects.order_by(Length('name'))

    QSWO = webpage.objects.all().order_by(Length('name').desc())

    QSWO = webpage.objects.filter(name__regex='i$')
    
    QSWO = webpage.objects.filter(name__regex='(^S|t$)')
    
    QSWO = webpage.objects.filter(name__regex='^S')
    
    QSWO = webpage.objects.filter(url__contains='S')

    QSWO = webpage.objects.exclude(name__contains='S')
    
    
    QSWO = webpage.objects.all()
    d={'QSWO':QSWO}
    return render(request,'dispaly_webpage.html',d)


def dispaly_Access(request):
    QSAO = AccessRecord.objects.all()
    QSAO = AccessRecord.objects.exclude(author='VK')

    QSAO = AccessRecord.objects.filter(author__startswith = 'VK')

    QSAO = AccessRecord.objects.filter(author__contains = 'o')

    QSAO = AccessRecord.objects.filter(author__endswith = 'k')

    QSAO = AccessRecord.objects.filter(date ='2023-08-03')
    
    QSAO = AccessRecord.objects.filter(date__year='2023')

    QSAO = AccessRecord.objects.filter(date__day='3')

    QSAO = AccessRecord.objects.filter(date__month='08')

    QSAO = AccessRecord.objects.filter(date__day__gt='3')
    
    QSAO = AccessRecord.objects.filter(date__day__gte='3')
    
    QSAO = AccessRecord.objects.filter(date__day__lt='3')
    
    QSAO = AccessRecord.objects.filter(date__day__lte='3')
    
    QSAO = AccessRecord.objects.all()

    d={'QSAO':QSAO}
    return render(request,'dispaly_Access.html',d)