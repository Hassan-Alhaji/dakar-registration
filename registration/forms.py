from django import forms
from .models import Registration

class RegistrationForm(forms.ModelForm):
    race_types = forms.MultipleChoiceField(
        choices=Registration.RACE_TYPES,
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label='أنواع السباقات السابقة'
    )

    class Meta:
        model = Registration
        exclude = ['status', 'admin_notes', 'reviewed_by', 'reviewed_date']
        widgets = {
            'program_goal': forms.Textarea(attrs={'rows': 4}),
            'health_conditions': forms.Textarea(attrs={'rows': 3}),
            'application_date': forms.HiddenInput(),
            'updated_date': forms.HiddenInput(),
        }

    def clean_race_types(self):
        return self.cleaned_data.get('race_types', [])
