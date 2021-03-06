from django.test import TestCase
from django.contrib.auth.models import User
from django.test.client import Client
from feedback import app_settings
from feedback import models
from django.core import mail
from django.core.urlresolvers import reverse

class FeedbackTest(TestCase):
    def setUp(self):
        self.u = User.objects.create_user('testuser', 'test@example.com', 'testpw')
        self.client = Client()
        self.client.login(username='testuser',password='testpw')

    def test_email(self):
        app_settings.FEEDBACK_SEND_MAIL=True
        feedback = models.Feedback(
                feedback='test feedback',
                path='/',
                )
        feedback.save()
        self.assertEqual(len(mail.outbox),1)

        app_settings.FEEDBACK_SEND_MAIL=False
        feedback = models.Feedback(
                feedback='another test feedback',
                path='/other/path/',
                )
        feedback.save()
        self.assertEqual(len(mail.outbox),1)


    def test_url_feedback_no_ajax(self):
        c = self.client
        url = reverse('feedback.views.feedback')
        response = c.post(url,{'feedback':'test_feedback','path':'/'})
        feedback = models.Feedback.objects.filter(feedback='test_feedback')
        self.assertEqual(len(feedback),1)
        self.assertEqual(feedback[0].feedback,'test_feedback')
        self.assertEqual(feedback[0].path,'/')
        self.assertEqual(response.status_code,302)

    def test_url_feedback_ajax(self):
        c = self.client
        url = reverse('feedback.views.feedback')
        response = c.post(url,{'feedback':'test_feedback','path':'/'},
                HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertEqual(response.status_code,200)
        self.assertEqual(response.content,'{"feedback": "accepted"}')
