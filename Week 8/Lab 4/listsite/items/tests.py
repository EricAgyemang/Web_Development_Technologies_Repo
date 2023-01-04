from django.test import TestCase, Client
from django.test.utils import setup_test_environment
from django.urls import reverse
from items import models

# Create your tests here.


class TestEmptyList(TestCase):
    """
    As a list author I need to know if my list is empty so I know to add items
    AC: retieve a special message for an empty list
    """
   
    def setUp(self):
        self.client = Client()
        
    def test_retrieve_list(self):
        response = self.client.get(reverse("item_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Your list is empty. Add an item!")
        


class TestFullList(TestCase):
    """
    As a list author I need to see my list items so I know what is on my list
    AC:retieve a list of items from /list/
    """
    def setUp(self):
        self.client = Client()
        models.Item.objects.create(text="Walk the dog")
        models.Item.objects.create(text="Walk the other dog")
        
    def test(self):
        response = self.client.get(reverse('item_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Walk the dog")
        self.assertContains(response, "Walk the other dog")



class TestAddingItems(TestCase):
    """
    As a list author I need to add a list item so that see it later
    AC: items can be added then retrieved
    """

    def setUp(self):
        self.client = Client()
    
    def test(self):
        self.client.post('/items/', {'text':'Get free food on the quad'})
        response = self.client.get(reverse('item_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Get free food on the quad")


    


"""
As a list author I need to mark an Item as done so that I don't do it again.
AC:
    There is a button for each item
    pressing a button marks that item as done and reloads the page
    
"""

