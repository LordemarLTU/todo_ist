from django.test import TestCase
from django.urls import reverse
from .models import *

class TaskTestCase(TestCase):
    def test_add_task(self):
       task_data = { 'title':'add task' }
       response = self.client.post(reverse('addTask'), data=task_data)
       self.assertEqual(response.status_code, 302)
       self.assertTrue(Task.objects.filter(title='add task').exists())
       task = Task.objects.get(title='add task')
       self.assertFalse(task.completed)

    def setUp(self):
        self.task = Task.objects.create(title='remove task')

    def test_done_task(self):
        url = reverse('changeStatus', kwargs={'taskId': self.task.id})
        response = self.client.post(url)
        self.assertEqual(response.status_code, 302)
        self.task.refresh_from_db()
        self.assertTrue(self.task.completed)

    def test_undone_task(self):
        self.task.completed = True
        self.task.save()

        url = reverse('changeStatus', kwargs={'taskId': self.task.id})
        response = self.client.post(url)
        self.assertEqual(response.status_code, 302)
        self.task.refresh_from_db()
        self.assertFalse(self.task.completed)


    def test_remove_task(self):
        url = reverse('removeTask', kwargs={'taskId': self.task.id})
        response = self.client.post(url)
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Task.objects.filter(title='remove task').exists())