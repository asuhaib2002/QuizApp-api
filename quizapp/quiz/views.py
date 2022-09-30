from django.shortcuts import render
import requests
from rest_framework.response import Response
from rest_framework import generics
from .models import Quizzes, Question
from .serializers import QuizSerializer,RandomQuestionSerializer,QuestionSerializer
from rest_framework.views import APIView

# Create your views here.

class Quiz(generics.ListAPIView):
    serializer_class = QuizSerializer
    queryset = Quizzes.objects.all()


class RandomQuestion(APIView):
    
    def get(self, request, format=None, **kwargs):
        question = Question.objects.filter(quiz__title=kwargs['topic']).order_by('?')[:1]
        serializer = RandomQuestionSerializer(question, many=True)
        return Response(serializer.data)
    # def post(self, request):
    #     print('data is ', request.data)
    #     return Response({"Message":"New Book Added!"})
    



# def getResult(request):
#     if request.method == 'POST':
#         result = request.POST.get('btn-check')
#         print(result)
#         return
    
   
    


class QuizQuestion(APIView):
    

    def get(self, request, format=None, **kwargs):
        question = Question.objects.filter(quiz__title=kwargs['topic'])
        serializer =  QuestionSerializer(question, many=True)
        return Response(serializer.data)