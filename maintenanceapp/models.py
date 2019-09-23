from django.db import models
from django.urls import reverse
# Create your models here.

class MaintenanceWorkRequest(models.Model):
    class Meta:
        abstract=True

    description = models.CharField(max_length=20, null=True, blank=True)
    created_by = models.CharField(max_length=20)
    category = models.CharField(max_length=20, choices=[
        ('Electrical','Electrical'),
        ('Mechanical','Mechanical'),
        ('Automotive','Automotive'),
        ('Plumbing','Plumbing'),
        ('Carpentry','Carpentry'),
    ])
    down_time = models.TimeField(null=True)
    labour_time = models.TimeField(null=True)
    team = models.CharField(max_length=24)
    responsible = models.CharField(max_length=24)
    duration = models.TimeField(null=True)
    consumables_required = models.TextField(max_length=256)
    resolved_by_vendor = models.BooleanField(default=False)
    vendor = models.CharField(max_length=255)
    service_order_ref = models.CharField(max_length=255)

class BreakdownMaintenanceWorkRequest(MaintenanceWorkRequest):
    
    def get_absolute_url(self):
        return reverse("maintenanceapp:maintenance-detail", kwargs={"pk": self.pk})

class PreventativeMaintenanceWorkRequest(MaintenanceWorkRequest):
    scheduled_date = models.DateField()
    down_time = models.TimeField()
    labour_time = models.TimeField()
    tasks = models.CharField(max_length=264)

    def get_absolute_url(self):
        return reverse("maintenanceapp:preventative-detail", kwargs={"pk": self.pk})

class MaintenanceRecord(models.Model):
    breakdown = models.ForeignKey(BreakdownMaintenanceWorkRequest, on_delete=models.CASCADE)
    planned_job = models.ForeignKey(PreventativeMaintenanceWorkRequest, on_delete=models.CASCADE)
    resolver = models.CharField(max_length=32)
    status = models.CharField(max_length=32, choices=[
        ('In Progress','In Progress'),
        ('Rejected','Rejected'),
        ('Approved','Approved'),
    ])
    approved_by = models.CharField(max_length=32)
    approved_date = models.DateField()
    consumables_used = models.TextField()

    def get_absolute_url(self):
        return reverse("maintenanceapp:maintenance-record-detail", kwargs={"pk": self.pk})

class MaintenanceChecklist(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    start_time = models.TimeField()
    start_date = models.DateField()
    frequency = models.CharField(max_length=24)
    duration = models.DurationField()
    category = models.CharField(max_length=255, choices=[
        ('electrical','Electrical'),
        ('mechanical','Mechanical'),
        ('automotive','Automotive'),
        ('plumbing','Plumbing'),
        ('carpentry','Carpentry'),
        ('hydraulics','Hydraulics'),
        ('pneumatics','Pneumatics'),
    ])
    resolver = models.CharField(max_length=32)

    def get_absolute_url(self):
        return reverse("maintenanceapp:checklist-detail", kwargs={"pk": self.pk})
    

class ChecklistItem(models.Model):
    checklist = models.ForeignKey(MaintenanceChecklist, on_delete = models.CASCADE)
    description = models.TextField()

    def get_absolute_url(self):
        return reverse("maintenanceapp:checklistitem-detail", kwargs={"pk": self.pk})