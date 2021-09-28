from django.db.models import query
from django.test import TestCase, testcases
from .models import Neighbourhood,Alert,Business

# Create your tests here.
class NeighbourhoodTestClass(TestCase):
    def setUp(self):
        self.hood= Neighbourhood(1,'name','location',40)
        
    def test_hood(self):
        self.assertTrue(isinstance(self.hood,Neighbourhood))
    def test_add(self):
        self.hood.addhood()
        query=Neighbourhood.objects.all()
        self.assertTrue(len(query)>0)
        
    def test_delete(self):
        self.hood.deletehood()
        query=Neighbourhood.objects.all()
        self.assertTrue(len(query)==0)
        
   
        
    