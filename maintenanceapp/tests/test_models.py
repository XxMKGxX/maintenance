import datetime
from django.test import TestCase
from maintenanceapp.models import *
from django.contrib.auth.models import User

class MaintenanceTests(TestCase):

    @classmethod
    def setUpClass(cls):
        return super().setUpClass()

    @classmethod
    def setUpTestData(cls):
        cls.breakdown = BreakdownMaintenanceWorkRequest.objects.create(created_by='test', down_time='00:00', labour_time='00:00', duration='02:00')
        cls.usr = User.objects.create_user(username='someperson')
        cls.preventative = PreventativeMaintenanceWorkRequest.objects.create(created_by='test', down_time='00:00', labour_time='00:00', duration='02:00', scheduled_date='2001-01-01')

    def setUp(self):
        pass

    def test_create_breakdown(self):
        obj = BreakdownMaintenanceWorkRequest.objects.create(
            created_by='test',
            category = 'electrical',
            down_time = '16:00',
            labour_time = '00:00',
            duration='03:00',
        )
        self.assertIsInstance(obj, BreakdownMaintenanceWorkRequest)

    def test_update_breakdown(self):
        obj = BreakdownMaintenanceWorkRequest.objects.get(pk=1)
        self.assertIsInstance(obj, BreakdownMaintenanceWorkRequest)

    def test_create_preventative(self):
        obj = PreventativeMaintenanceWorkRequest.objects.create(
            scheduled_date=datetime.date.today(),
            duration='03:00',
            down_time = '16:00',
            labour_time = '00:00',
        )
        self.assertIsInstance(obj, PreventativeMaintenanceWorkRequest)

    def test_create_record(self):
        obj = MaintenanceRecord.objects.create(
            breakdown=self.breakdown,
            resolver = 'test1',
            approved_date='2001-01-01',
            planned_job=self.preventative,
        )
        self.assertIsInstance(obj, MaintenanceRecord)