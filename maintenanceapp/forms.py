from django.forms import ModelForm
from django import forms
from .models import *
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row,Column, HTML
from crispy_forms.bootstrap import Tab, TabHolder

class BreakdownMaintenaceWorkRequestForm(forms.ModelForm):
    class Meta:
        model = BreakdownMaintenanceWorkRequest
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            HTML(
                "<h4>Breakdown Maintenance Work Request Form </h4>"
            ),
            Row(
                Column(HTML('<h4>Basic</h4>'),css_class='col-6'),
                Column(HTML("<h4>Additional</h4>"), css_class='col-6'),
            ),
            Row(
                Column('created_by', 'category', 'down_time', 'labour_time', 'vendor', css_class='form-group col-md-6'),
                Column('team', 'responsible', 'duration', 'service_order_ref', css_class='form-group col-md-6')
            ),
            Row(
                Column('consumables_required', css_class='form-group col-md-12'),
            ),
        )
        self.helper.add_input(Submit('submit', "Submit"))

class PreventativeMaintenanceWorkRequestForm(forms.ModelForm):
    class Meta:
        model = PreventativeMaintenanceWorkRequest
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            HTML(
                "<h4>Maintenance Work Request Form </h4>"
            ),
            Row(
                Column(HTML('<h4>Basic</h4>'),css_class='col-6'),
                Column(HTML("<h4>Additional</h4>"), css_class='col-6'),
            ),
            Row(
                Column('created_by', 'category', 'down_time', 'labour_time', 'scheduled_date', css_class='form-group col-md-6', label='e.g Kitchen Maintenance'),
                Column('team', 'responsible', 'duration', 'service_order_ref',
                'vendor','tasks', css_class='form-group col-md-6')
            ),
            Row(
                Column('consumables_required', css_class='form-group col-md-12'),
            ),
        )
        self.helper.add_input(Submit('submit', "Submit"))

class MaintenanceRecordForm(forms.ModelForm):
    class Meta:
        model = MaintenanceRecord
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            HTML(
                "<h4>Maintenance Record Form </h4>"
            ),
            Row(
                Column(HTML('<h4>Basic</h4>'),css_class='col-6'),
                Column(HTML("<h4>Additional</h4>"), css_class='col-6'),
            ),
            Row(
                Column('planned_job', 'approved_by', css_class='form-group col-md-6'),
                Column('status', 'approved_date', css_class='form-group col-md-6'),
            ),
            Row(
                Column('resolver', css_class='form-group col-md-6'),
                Column('breakdown', css_class='form-group col-md-6'),
            ),
            Row(
                Column('consumables_used', css_class='form-group col-md-12'),
            ),
        )
        self.helper.add_input(Submit('submit', "Submit"))

class MaintenanceCheklistForm(forms.ModelForm):
    class Meta:
        model = MaintenanceChecklist
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].label = "e.g Kitchen Checklist"
        self.helper = FormHelper()
        self.helper.layout = Layout(
            HTML(
                "<h3>Maintenance Checklist Form </h3>"
            ),
            Row(
                Column(HTML('<h4>Main</h4>'),css_class='col-6'),
                Column(HTML('<h4>Details</h4>'),css_class='col-6'),
            ),
            Row(
                Column('name','resolver','category',css_class='form-group col-md-6'),
                Column('start_time','start_date','frequency','duration',css_class='form-group col-md-6'),                
            ),
            'description'
        )
        self.helper.add_input(Submit('submit', "Submit"))

class CheklistItemForm(forms.ModelForm):
    class Meta:
        model = ChecklistItem
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            HTML(
                "<h3>Checklist Item Form </h3>"
            ),
            'checklist',
            'description',
        )
        self.helper.add_input(Submit('submit', "Submit"))
