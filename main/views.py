from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
#from .serializers import ChoiceSerializer, QuestionSerializer, LaptopSerializer
from django.db.models import Q
from .filters import LaptopFilter
from django.core.paginator import Paginator

# Create your views here.
# 동적인 값들을 가져와야 합니다.
from .models import Question, Laptop, Choice, Answer


def index(request):

    laptops = Laptop.objects.all()
    counts = Laptop.objects.count()

    context = {'laptops': laptops}

    return render(request, 'main/index.html', context=context)


def details(request):
    questions = Question.objects.all()

    context = {'questions': questions}

    return render(request, 'main/details.html', context=context)



'''
def results(request):
    context = {}
    
    filtered_laptops = LaptopFilter(
        request.GET,
        queryset = Laptop.objects.all()
    )
    
    context['filtered_laptops'] = filtered_laptops
    
    paginated_filtered_laptops = Paginator(filtered_laptops.qs, 2)
    page_number = request.GET.get('page')
    laptop_page_obj = paginated_filtered_laptops.get_page(page_number)
    
    context['laptop_page_obj'] = laptop_page_obj
    
    return render(request, 'main/results.html', context=context)
'''


'''
def results(request):
    context = []
    
    filtered_laptops = LaptopFilter(
    )
'''


    # # Question1
    # if (선택지1):
    #     results = Laptop.objects.filter(display>=15)
    # else:
    #     results = Laptop.objects.filter(display<15)
        
    
    # results = Laptop.objects.filter(cpu_level="1")
    
#     display               = request.GET.getlist('display', None)
#     cpu_level              = request.GET.getlist('cpu_level', None)
#     price_upper_range  = request.GET.get('PriceUpper', 1000000)
#     price_lower_range  = request.GET.get('PriceLower', 0)

#     q=Q()
#     if category:
#         q &= Q(category_id = category)
#     if color:
#         q &= Q(color_name__in = color)
#     if size:
#         q &= Q(size__name__in = size)

#     q &= Q(price__range = (price_lower_range,price_upper_range))
    
    
    

#    return render(request, 'main/results.html', context=context)


# class LaptopListAPI(APIView):
#     def get(self, request):
#         # queryset = Laptop.objects.all()
        
#         laptops = Laptop.objects.all()
        
#         print(queryset)
#         serializer = LaptopSerializer(laptops, many=True)
#         return Response(serializer.data)


# class ChoiceListAPI(APIView):
#     def get(self, request):
#         queryset = Choice.objects.all()
#         print(queryset)
#         serializer = ChoiceSerializer(queryset, many=True)
#         return Response(serializer.data)


# class QuestionListAPI(APIView):
#     def get(self, request):
#         queryset = Question.objects.all()
#         print(queryset)
#         serializer = QuestionSerializer(queryset, many=True)
#         return Response(serializer.data)

# class QNAListAPI(APIView):
#     def get(self, request):
#         queryset = Question.objects.all()
#         print(queryset)
#         serializer = QNASerializer(queryset, many=True)
#         return Response(serializer.data)

# 연습
def results(request):
    q0_choice = request.POST.get("question0")
    q1_choice = request.POST.get("question1")
    q2_choice = request.POST.get("question2")
    q3_choice = request.POST.get("question3")
    q4_choice = request.POST.get("question4")
    q5_choice = request.POST.get("question5")   
    q6_choice = request.POST.get("question6")
    q7_choice = request.POST.get("question7")
    q8_choice = request.POST.get("question8")
    '''
    if q0 == 1:
        result0 = Laptop.objects.filter(cpu_level =1)
    else:
        reulst0 = ~~
        
    if q1 == 3:
        result1 = result0.ogg()
        
     '''   
        
        
    results = Laptop.objects.filter(cpu_level=1)
    results2 = results.filter(ram=16)
    
    answer = [q0_choice, q1_choice, q2_choice,q3_choice, q4_choice, q5_choice,q6_choice, q7_choice, q8_choice]
    return render(request, 'main/results.html', {"key" : results2})
    
#
#
#
#