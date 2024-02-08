from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import File
from .serializers import WorkSerializer
from .tasks import process_uploaded_file


# Для загрузки файлов
class WorkAPIView(APIView):
    # def get(self, request):
    #     w = File.objects.all()
    #     return Response({'posts': WorkSerializer(w, many=True).data})

    def post(self, request):
        # Делаем serializer из переданных данных
        serializer = WorkSerializer(data=request.data)
        # Проверяем на валидность
        if serializer.is_valid():  # raise_exception=True
            post_new = File.objects.create(
                file=request.data['file'],
                # uploaded_at=request.data['uploaded_at']
            )
            # ДОЛЖЕН БЫТЬ ВКЛЮЧЕН RADIS и виртуальная машина !!!!!!!!!!!!!
            # Помещение задачи в Celery - и изменение processed на True
            process_uploaded_file.delay(post_new.id)

            return Response({'file': WorkSerializer(post_new).data}, status=status.HTTP_201_CREATED)
        else:
            return Response(status.HTTP_400_BAD_REQUEST)


# Для вывода данных
class FilesAPIView(APIView):
    def get(self, request):
        w = File.objects.all()
        return Response({'posts': WorkSerializer(w, many=True).data})


# # ListAPIView -  это представления
# class WorkAPIView(generics.ListAPIView):
#     queryset = File.objects.all()
#     # Передаем сериалайзер
#     serializer_class = WorkSerializer
