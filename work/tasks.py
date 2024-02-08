# Create your tasks here
from celery import shared_task

from work.models import File


@shared_task
def process_uploaded_file(id):
    # Получаем объект модели File по его идентификатору
    file_instance = File.objects.get(id=id)
    # Меняем пункт processed на 1
    file_instance.processed = 1
    file_instance.save()


# @shared_task
# def add(x, y):
#     print(x, y)
#     return x + y