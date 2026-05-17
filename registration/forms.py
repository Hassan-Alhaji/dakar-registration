from django import forms
from .models import Registration
from django.utils.translation import gettext_lazy as _

NATIONALITY_CHOICES = [
    ('', 'اختر الجنسية / Select Nationality'),
    ('Saudi', 'السعودية - Saudi'),
    ('Emirati', 'الإمارات - Emirati'),
    ('Kuwaiti', 'الكويت - Kuwaiti'),
    ('Bahraini', 'البحرين - Bahraini'),
    ('Omani', 'عُمان - Omani'),
    ('Qatari', 'قطر - Qatari'),
    ('Egyptian', 'مصر - Egyptian'),
    ('Jordanian', 'الأردن - Jordanian'),
    ('Lebanese', 'لبنان - Lebanese'),
    ('Syrian', 'سوريا - Syrian'),
    ('Iraqi', 'العراق - Iraqi'),
    ('Yemeni', 'اليمن - Yemeni'),
    ('Moroccan', 'المغرب - Moroccan'),
    ('Algerian', 'الجزائر - Algerian'),
    ('Tunisian', 'تونس - Tunisian'),
    ('Sudanese', 'السودان - Sudanese'),
    ('American', 'الولايات المتحدة - American'),
    ('British', 'بريطانيا - British'),
    ('French', 'فرنسا - French'),
    ('Spanish', 'إسبانيا - Spanish'),
    ('Italian', 'إيطاليا - Italian'),
    ('German', 'ألمانيا - German'),
    ('Other', 'أخرى / Other'),
]

class RegistrationForm(forms.ModelForm):
    nationality = forms.ChoiceField(
        choices=NATIONALITY_CHOICES,
        label=_('الجنسية')
    )
    other_nationality = forms.CharField(
        required=False,
        label=_('أدخل الجنسية / Enter Nationality'),
        widget=forms.TextInput(attrs={'placeholder': 'أدخل جنسيتك هنا / Type your nationality here', 'id': 'id_other_nationality'})
    )
    
    race_types = forms.MultipleChoiceField(
        choices=Registration.RACE_TYPES,
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label=_('أنواع السباقات السابقة')
    )
    
    has_driving_license = forms.BooleanField(required=False, label=_('هل لديك رخصة قيادة سارية المفعول؟'))
    has_sports_license = forms.BooleanField(required=False, label=_('هل لديك رخصة سباق مصدرة من الاتحاد السعودي للسيارات؟'))
    has_previous_experience = forms.BooleanField(required=False, label=_('هل لديك خبرة سابقة في مجال رياضة السيارات؟'))
    can_travel = forms.BooleanField(required=False, label=_('هل لديك القدرة على السفر والإقامة في مدينة بيشة لمدة 5 أيام؟'))
    committed_to_5_days = forms.BooleanField(required=False, label=_('هل أنت ملتزم بحضور كامل أيام المعسكر؟'))

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
            'email': forms.EmailInput(attrs={'type': 'email'}),
            'phone': forms.TextInput(attrs={'type': 'tel', 'pattern': '[0-9]+', 'minlength': '9'}),
            'id_number': forms.TextInput(attrs={'type': 'text', 'pattern': '[0-9]+'}),
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        from django.core.validators import validate_email
        from django.core.exceptions import ValidationError
        try:
            validate_email(email)
        except ValidationError:
            raise forms.ValidationError(_('يرجى إدخال بريد إلكتروني صحيح'))
        return email

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if not phone.isdigit():
            raise forms.ValidationError(_('رقم الجوال يجب أن يحتوي على أرقام فقط'))
        if len(phone) < 9:
            raise forms.ValidationError(_('رقم الجوال يجب ألا يقل عن 9 أرقام'))
        return phone

    def clean_id_number(self):
        id_number = self.cleaned_data.get('id_number')
        if not id_number.isdigit():
            raise forms.ValidationError(_('رقم الهوية يجب أن يحتوي على أرقام فقط'))
        return id_number

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        from django.utils import translation
        if translation.get_language() == 'en':
            self.fields['has_driving_license'].label = 'Do you have a valid driving license?'
            self.fields['has_sports_license'].label = 'Do you have a racing license issued by SAMF?'
            self.fields['has_previous_experience'].label = 'Do you have previous experience in motorsports?'
            self.fields['can_travel'].label = 'Are you able to travel and stay in Bisha for 5 days?'
            self.fields['committed_to_5_days'].label = 'Are you committed to attending all days of the camp?'
            self.fields['agreed_to_terms'].label = 'I have read and agree to all terms and conditions of the program'
            self.fields['agreed_to_terms'].error_messages['required'] = 'You must agree to the terms and conditions to complete registration.'

    def clean(self):
        cleaned_data = super().clean()
        nationality = cleaned_data.get('nationality')
        other_nationality = cleaned_data.get('other_nationality')
        
        if nationality == 'Other':
            if not other_nationality:
                self.add_error('other_nationality', _('يرجى كتابة الجنسية'))
            else:
                cleaned_data['nationality'] = other_nationality
                
        return cleaned_data

    def clean_race_types(self):
        return self.cleaned_data.get('race_types', [])
