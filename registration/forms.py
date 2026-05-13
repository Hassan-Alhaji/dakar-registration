from django import forms
from .models import Registration
from django.utils.translation import gettext_lazy as _

class RegistrationForm(forms.ModelForm):
    race_types = forms.MultipleChoiceField(
        choices=Registration.RACE_TYPES,
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label=_('أنواع السباقات السابقة')
    )
    
    agreed_to_terms = forms.BooleanField(
        required=True,
        label=_('قرأت وأوافق على جميع الشروط والأحكام الخاصة بالبرنامج'),
        error_messages={
            'required': _('يجب الموافقة على الشروط والأحكام لإتمام التسجيل.')
        }
    )

    class Meta:
        model = Registration
        exclude = ['status', 'admin_notes', 'reviewed_by', 'reviewed_date']
        widgets = {
            'program_goal': forms.Textarea(attrs={'rows': 4}),
            'health_conditions': forms.Textarea(attrs={'rows': 3}),
        }

    def clean_race_types(self):
        return self.cleaned_data.get('race_types', [])
