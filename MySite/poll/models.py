from django.db import models

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(verbose_name = 'question', max_length = 200)
    published_date = models.DateTimeField(verbose_name = 'date published')

    def __str__(self):
        return self.question_text + ' - ' + str(self.published_date)

    class Meta:
        pass

class Choice(models.Model):
    question = models.ForeignKey(verbose_name = 'question',to = Question, on_delete = models.CASCADE)
    choice_text = models.CharField(verbose_name = 'choice', max_length = 200)
    votes = models.IntegerField(verbose_name = 'votes', default = 0)

    def __str__(self):
        return str(self.question) + ' - ' + self.choice_text + ' - ' + str(self.votes)

    class Meta:
        pass