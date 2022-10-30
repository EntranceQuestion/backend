from django.db import models


class ModelQuestion(models.Model):

    id = models.AutoField(primary_key=True)
    question = models.TextField(
        max_length=1500,
        unique=True,
        blank=False,
        null=False,
    )
    option_1 = models.CharField(max_length=100)
    option_2 = models.CharField(max_length=100)
    option_3 = models.CharField(max_length=100)
    option_4 = models.CharField(max_length=100)

    class Options(models.IntegerChoices):
        opt1 = 1, "Option 1"
        opt2 = 2, "Option 2"
        opt3 = 3, "Option 3"
        opt4 = 4, "Option 4"

    correct_option = models.PositiveSmallIntegerField(choices=Options.choices)

    def __str__(self):
        return self.question
