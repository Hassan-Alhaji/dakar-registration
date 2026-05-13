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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        from django.utils import translation
        if translation.get_language() == 'en':
            self.fields['has_driving_license'].label = 'Do you have a valid driving license?'
            self.fields['has_sports_license'].label = 'Do you have a racing license issued by SAMF?'
            self.fields['has_previous_experience'].label = 'Do you have previous experience in motorsports?'
            self.fields['agreed_to_terms'].label = 'I have read and agree to all terms and conditions of the program'
            self.fields['agreed_to_terms'].error_messages['required'] = 'You must agree to the terms and conditions to complete registration.'

    def clean_race_types(self):
        return self.cleaned_data.get('race_types', [])
