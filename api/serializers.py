from rest_framework import serializers
from . import models


class ModelQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ModelQuestion
        fields = [
            "id",
            "question",
            "option_1",
            "option_2",
            "option_3",
            "option_4",
            "correct_option"
        ]
