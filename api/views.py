import random
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import ModelQuestion
from .serializers import ModelQuestionSerializer


@api_view(["GET"])
def model_question(request):
    questions = ModelQuestion.objects.order_by("id").values_list('id', flat=True)
    # question = models.ModelQuestion.objects.all().values_list('id', flat=True)
    random_id = random.choice(questions)
    print("---------------------------")
    print(random_id)
    print("---------------------------")
    question = ModelQuestion.objects.get(pk=random_id)
    data = ModelQuestionSerializer(question, many=False)
    return Response(data.data)
