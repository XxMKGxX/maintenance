from django.shortcuts import render
from django import forms
from django.urls import reverse_lazy
from .forms import *
from django.views.generic import CreateView, DetailView, ListView, DeleteView, UpdateView
from . import models
import os 

# Create your views here.

def dashboard(request):
    return render(request, 'dashboard.html')

class BreakdownMaintenanceWorkView(CreateView):
    template_name = os.path.join('maintenanceapp','maintenance-work-request.html')
    form_class = BreakdownMaintenaceWorkRequestForm
    
class MaintenanceRecordView(CreateView):
    template_name = os.path.join('maintenanceapp','maintenance-record.html')
    form_class = MaintenanceRecordForm

class PreventativeMaintenaceWorkView(CreateView):
    template_name = os.path.join('maintenanceapp','preventative-maintenance.html')
    form_class = PreventativeMaintenanceWorkRequestForm

class MaintenanceChecklistCreate(CreateView):
    template_name = os.path.join('maintenanceapp','maintenance-checklist.html')
    form_class = MaintenanceCheklistForm

class ChecklistItemCreate(CreateView):
    template_name = os.path.join('maintenanceapp','checklistitem.html')
    form_class = CheklistItemForm

class BreakdownMaintenanceWorkDetailView(DetailView):
    model = models.BreakdownMaintenanceWorkRequest
    template_name = os.path.join('detail','work-request-detail.html')

class PreventativeMaintenanceWorkDetailView(DetailView):
    model = models.PreventativeMaintenanceWorkRequest
    template_name = os.path.join('detail','preventative-detail.html')

class MaintenanceRecordDetailView(DetailView):
    model = models.MaintenanceRecord
    template_name = os.path.join('detail','record-detail.html')

class MaintenanceChecklistDetail(DetailView):
    model = models.MaintenanceChecklist
    template_name = os.path.join('detail','checklist-detail.html')

class ChecklistItemDetail(DetailView):
    model = models.ChecklistItem
    template_name = os.path.join('detail','checklistitem-detail.html')

class BreakdownMaintenanceWorkRequestList(ListView):
    template_name = os.path.join('list', 'maintenance-list.html')
    context_object_name = 'work'

    def get_queryset(self):
        return models.BreakdownMaintenanceWorkRequest.objects.order_by('pk')

class PreventativeMaintenanceWorklist(ListView):
    template_name = os.path.join('list', 'preventative-list.html')
    context_object_name = 'preventative'

    def get_queryset(self):
        return models.PreventativeMaintenanceWorkRequest.objects.order_by('pk')

class MaintenanceRecordlist(ListView):
    template_name = os.path.join('list', 'maintenance-record-list.html')
    context_object_name = 'record'

    def get_queryset(self):
        return models.MaintenanceRecord.objects.order_by('pk')

class MaintenanceChecklistList(ListView):
    template_name = os.path.join('list','maintenance-checklist-list.html')

    def get_queryset(self):
        return models.MaintenanceChecklist.objects.order_by('pk')

class ChecklistItemList(ListView):
    template_name = os.path.join('list','checklistitem-list.html')

    def get_queryset(self):
        return models.ChecklistItem.objects.order_by('pk')

class BreakdownMaintenanceWorkUpdateView(UpdateView):
    form_class = BreakdownMaintenaceWorkRequestForm
    model = models.BreakdownMaintenanceWorkRequest
    template_name = os.path.join('maintenanceapp','maintenance-work-request.html')

class PreventativeMaintenanceWorkUpdateView(UpdateView):
    form_class = PreventativeMaintenanceWorkRequestForm
    model = models.PreventativeMaintenanceWorkRequest
    template_name = os.path.join('maintenanceapp','preventative-maintenance.html')

class MaintenanceRecordUpdateView(UpdateView):
    form_class = MaintenanceRecordForm
    model = models.MaintenanceRecord
    template_name = os.path.join('maintenanceapp','maintenance-record.html')

class MaintenanceChecklistUpdate(UpdateView):
    form_class = MaintenanceCheklistForm
    model = models.MaintenanceChecklist
    template_name = os.path.join('maintenanceapp','maintenance-checklist.html')

class ChecklistItemUpdate(UpdateView):
    form_class = CheklistItemForm
    model = models.ChecklistItem
    template_name = os.path.join('maintenanceapp','checklistItem.html')

class BreakdownMaintenanceWorkDelete(DeleteView):
    template_name = os.path.join('maintenanceapp','maintenance_confirm_delete.html')
    model = models.BreakdownMaintenanceWorkRequest
    success_url = reverse_lazy('maintenanceapp:maintenance-list')

class MaintenanceRecordDelete(DeleteView):
    template_name = os.path.join('maintenanceapp','maintenance_record_confirm_delete.html')
    model = models.MaintenanceRecord
    success_url = reverse_lazy('maintenanceapp:maintenance-record-list')

class PreventativeMaintenanceDelete(DeleteView):
    template_name = os.path.join('maintenanceapp',
    'preventative_confirm_delete.html')
    model = models.PreventativeMaintenanceWorkRequest
    success_url = reverse_lazy('maintenanceapp:preventative-list')

class MaintenaceChecklistDelete(DeleteView):
    template_name = os.path.join('maintenanceapp','checklist_confirm_delete.html')
    model = models.MaintenanceChecklist
    success_url = reverse_lazy('maintenanceapp:checklist-list')

class ChecklistItemDelete(DeleteView):
    template_name = os.path.join('maintenanceapp','checklistitem_confirm_delete.html')
    model = models.ChecklistItem
    success_url = reverse_lazy('maintenanceapp:checklistitem-list')
