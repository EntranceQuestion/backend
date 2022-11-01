import random
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import ModelQuestion
from .serializers import ModelQuestionSerializer


@api_view(["GET"])
def model_question(request):
    question_ids = list( ModelQuestion.objects.order_by("id").values_list("id", flat=True))

    # number of model questions to return per request
    no_of_model_question = 50
    len_question_ids = len(question_ids)
    if len_question_ids < no_of_model_question:
        no_of_model_question = len_question_ids

    random_ids = random.sample(question_ids, no_of_model_question)
    # print("----------- random ids ----------------")
    # print(random_ids)
    # print("--------------------------------------")
    model_questions = []
    for id in random_ids:
        question_data = ModelQuestion.objects.get(pk=id)

        result = {
            "id": question_data.id,
            "question": question_data.question,
            "option_1": question_data.option_1,
            "option_2": question_data.option_2,
            "option_3": question_data.option_3,
            "option_4": question_data.option_4,
            "correct_option": question_data.correct_option
        }
        model_questions.append(result)

    # data = ModelQuestionSerializer(model_question, many=True)
    # return Response(data.data)

    return Response(model_questions)
