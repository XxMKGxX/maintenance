import urllib
import datetime

from django.test import TestCase, Client
from django.contrib.auth.models import User
from maintenanceapp.models import *

class MaintenanceViewTests(TestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.client = Client()

    @classmethod
    def setUpTestData(cls):
        cls.breakdown = BreakdownMaintenanceWorkRequest.objects.create(created_by='test', down_time='00:00', labour_time='00:00', duration='02:00')
        cls.usr = User.objects.create_user(username='someperson')
        cls.preventative = PreventativeMaintenanceWorkRequest.objects.create(created_by='test', down_time='00:00', labour_time='00:00', duration='02:00', scheduled_date='2001-01-01')
        cls.maintenance = MaintenanceRecord.objects.create(approved_date='2001-01-01', breakdown=cls.breakdown, planned_job=cls.preventative)

    def test_get_maintenance_list(self):
        resp = self.client.get('/maintenance/maintenance-list',)
        self.assertEqual(resp.status_code, 200)

    def test_get_maintenance_detail(self):
        resp = self.client.get('/maintenance/maintenance-detail/'+str(self.breakdown.pk))
        self.assertEqual(resp.status_code, 200)

    def test_get_maintenance_create(self):
        resp = self.client.get('/maintenance/maintenance-create/')
        self.assertEqual(resp.status_code, 200)

    def test_get_preventative_create(self):
        resp = self.client.get('/maintenance/preventative-create/')
        self.assertEqual(resp.status_code, 200)

    def test_get_preventative_list(self):
        resp = self.client.get('/maintenance/preventative-list')
        self.assertEqual(resp.status_code, 200)

    def test_get_preventative_detail(self):
        resp = self.client.get('/maintenance/preventative-detail/'+str(self.preventative.pk))
        self.assertEqual(resp.status_code, 200)

    def test_get_maintenance_record_create(self):
        resp = self.client.get('/maintenance/maintenance-record-create/')
        self.assertEqual(resp.status_code, 200)

    def test_get_maintenance_record_list(self):
        resp = self.client.get('/maintenance/maintenance-record-list')
        self.assertEqual(resp.status_code, 200)

    def test_get_maintenance_record_detail(self):
        resp = self.client.get('/maintenance/maintenance-record-detail/'+str(self.maintenance.pk))
        self.assertEqual(resp.status_code, 200)
