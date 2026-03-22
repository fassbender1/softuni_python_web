from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import ListCreateAPIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from books.models import Book
from books.serializers import BookSerializer


# Create your views here.


class HomeView(APIView):
    def get(self, request):
        return HttpResponse({"text": "Hello World"}, content_type='application/json')

class BookListCreateView(APIView):
    def get(self, request: HttpRequest) -> HttpResponse:
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request: Request) -> Response:
        serializer = BookSerializer(date=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)