import random
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import ModelQuestion

# from .serializers import ModelQuestionSerializer


@api_view(["GET", "POST"])
def model_question(request):
    total_question_ids = list(
        ModelQuestion.objects.order_by("id").values_list("id", flat=True)
    )
    question_ids = total_question_ids.copy()

    # number of model questions to return per request
    no_of_model_question = 50
    len_question_ids = len(total_question_ids)
    if len_question_ids < no_of_model_question:
        no_of_model_question = len_question_ids

    len_solved_ids = len(request.data)

    solved_question_ids = []
    if len_solved_ids > 0:
        if len_question_ids > len_solved_ids:
            solved_question_ids = list(request.data)[0].strip("[]").split(",")
            # removed all solved question ids
            for id in solved_question_ids:
                id = int(id.strip('"'))
                question_ids.remove(id)

    if len(question_ids) < no_of_model_question:
        no_of_model_question = len(total_question_ids)
        question_ids = total_question_ids
        solved_question_ids = []

    random_ids = random.sample(question_ids, no_of_model_question)
    model_questions = []
    to_save_ids = random_ids + solved_question_ids
    model_questions.append(
        to_save_ids
    )  # keep record of solved ids in user's local storage
    for id in random_ids:
        question_data = ModelQuestion.objects.get(pk=id)

        result = {
            "id": question_data.id,
            "question": question_data.question,
            "option_1": question_data.option_1,
            "option_2": question_data.option_2,
            "option_3": question_data.option_3,
            "option_4": question_data.option_4,
            "correct_option": question_data.correct_option,
        }
        model_questions.append(result)

    # data = ModelQuestionSerializer(model_question, many=True)
    # return Response(data.data)

    return Response(model_questions)
