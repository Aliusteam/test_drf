from rest_framework import serializers
from .models import File


class WorkSerializer(serializers.Serializer):
    file = serializers.FileField()
    uploaded_at = serializers.DateTimeField(required=False)
    processed = serializers.BooleanField(default=False)






# # наследуемся от базового касса ModelSerializer
# # Этот сериализатор работает с моделями
# # Будет формировать json на запрос пользователей
# class WorkSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = File
#         # fields - поля которые будут использоваться
#         # для сериализации. Они отправляются пользователю
#         fields = ('file', 'uploaded_at')