# -*- coding: utf-8 -*-
from django.test import TestCase
from polls.models import Question
from django.utils import timezone


# Create your tests here.
class QuestionModelTests(TestCase):

    def test_vote_is_added_question(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is in the future.
        """
        question = Question(question_text = '测试', pub_date = timezone.now())
        question.save()
        
        question = Question.objects.get(pk=1)
        text = question.question_text;
        
        question.question_text = 'modify'
        question.save();
        
        question = Question.objects.get(pk=1)
        newText = question.question_text;
        
        self.assertEqual(newText, 'modify')