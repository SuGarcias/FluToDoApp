from django.test import TestCase, Client
from .models import Task
from django.urls import reverse
from .forms import TaskForm

class TaskModelTestCase(TestCase):
    def setUp(self):
        # Create a test task to use in the tests
        self.task = Task.objects.create(title="Test Task", description="Test Description", due_date="2024-03-31", priority="LOW", done=False)

    def test_task_creation(self):
        # Verify that a task can be created with the provided attributes
        task = Task.objects.get(title="Test Task")
        self.assertEqual(task.description, "Test Description")
        self.assertEqual(task.priority, "LOW")
        self.assertFalse(task.done)

    def test_task_str_representation(self):
        # Verify that the string representation of the task is correct
        task = Task.objects.get(title="Test Task")
        self.assertEqual(str(task), "Test Task")

class TaskViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_task_list_view(self):
        # Verify that the task list view loads correctly
        response = self.client.get(reverse('task_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'task_list.html')

    def test_create_task_view(self):
        # Verify that the create task view loads correctly
        response = self.client.get(reverse('create_task'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'create_task.html')

    def test_edit_task_view(self):
        # Verify that the edit task view loads correctly
        task = Task.objects.create(title="Test Task", description="Test Description", due_date="2024-03-31", priority="LOW", done=False)
        response = self.client.get(reverse('edit_task', args=[task.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'edit_task.html')

    def test_toggle_task_view(self):
        # Verify that the view to toggle task status executes correctly
        task = Task.objects.create(title="Test Task", description="Test Description", due_date="2024-03-31", priority="LOW", done=False)
        response = self.client.post(reverse('toggle_task', args=[task.id]))
        self.assertEqual(response.status_code, 302)  # Redirects after toggling task status

    def test_delete_task_view(self):
        # Verify that the view to delete task executes correctly
        task = Task.objects.create(title="Test Task", description="Test Description", due_date="2024-03-31", priority="LOW", done=False)
        response = self.client.post(reverse('delete_task', args=[task.id]))
        self.assertEqual(response.status_code, 302)  # Redirects after deleting task

class TaskFormTestCase(TestCase):
    def test_valid_task_form(self):
        # Verify that the task form is valid with valid data
        form_data = {'title': 'Test Task', 'description': 'Test Description', 'due_date': '2024-03-31', 'priority': 'LOW'}
        form = TaskForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_task_form(self):
        # Verify that the task form is invalid with invalid data
        form_data = {'title': '', 'description': 'Test Description', 'due_date': '2024-03-31', 'priority': 'LOW'}
        form = TaskForm(data=form_data)
        self.assertFalse(form.is_valid())
