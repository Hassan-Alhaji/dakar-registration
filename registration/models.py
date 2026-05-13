from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse

class Registration(models.Model):
    """نموذج بيانات التسجيل"""
    
    # اختيارات للحقول
    GENDER_CHOICES = [('M', _('ذكر')), ('F', _('أنثى'))]
    CATEGORY_CHOICES = [('D', _('متسابق')), ('N', _('ملاح'))]
    STATUS_CHOICES = [
        ('P', _('قيد الانتظار')),
        ('A', _('موافق عليه')),
        ('R', _('مرفوض')),
        ('W', _('متراجع عنه'))
    ]
    EXPERIENCE_CHOICES = [
        ('1-2', _('من 1 إلى 2 سنة')),
        ('2-5', _('من 2 إلى 5 سنوات')),
        ('5+', _('أكثر من 5 سنوات'))
    ]
    RACE_TYPES = [
        ('rallies', _('الراليات')),
        ('karting', _('الكارتينج')),
        ('autocross', _('الأوتوكروس')),
        ('time_trial', _('كسر الزمن')),
        ('drifting', _('الدرفت')),
        ('motorcycles', _('الدراجات النارية'))
    ]
    REGIONS = [
        ('riyadh', _('الرياض')),
        ('makkah', _('مكة المكرمة')),
        ('medina', _('المدينة المنورة')),
        ('eastern', _('المنطقة الشرقية')),
        ('asir', _('عسير')),
        ('baha', _('الباحة')),
        ('northern', _('المنطقة الشمالية')),
        ('qassim', _('القصيم')),
        ('hail', _('حائل')),
        ('jizan', _('جازان')),
        ('najran', _('نجران'))
    ]
    
    # معلومات شخصية
    full_name = models.CharField(max_length=100, verbose_name=_('الاسم الكامل'))
    age = models.PositiveIntegerField(validators=[MinValueValidator(16)], verbose_name=_('العمر'))
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, verbose_name=_('الجنس'))
    id_number = models.CharField(max_length=20, unique=True, verbose_name=_('رقم الهوية'))
    nationality = models.CharField(max_length=50, verbose_name=_('الجنسية'))
    phone = models.CharField(max_length=20, unique=True, verbose_name=_('رقم الجوال'))
    email = models.EmailField(unique=True, verbose_name=_('البريد الإلكتروني'))
    
    # معلومات فنية
    category = models.CharField(max_length=1, choices=CATEGORY_CHOICES, verbose_name=_('الفئة'))
    has_driving_license = models.BooleanField(verbose_name=_('رخصة القيادة'))
    has_sports_license = models.BooleanField(verbose_name=_('الرخصة الرياضية'))
    sports_license_number = models.CharField(max_length=50, blank=True, null=True, verbose_name=_('رقم الرخصة الرياضية'))
    
    # الخبرة السابقة
    has_previous_experience = models.BooleanField(verbose_name=_('خبرة سابقة'))
    race_types = models.JSONField(default=list, blank=True, verbose_name=_('أنواع السباقات'))
    number_of_races = models.PositiveIntegerField(blank=True, null=True, verbose_name=_('عدد السباقات'))
    years_of_experience = models.CharField(
        max_length=3,
        choices=EXPERIENCE_CHOICES,
        blank=True,
        verbose_name=_('سنوات الخبرة')
    )
    
    # التقييم والأهداف
    desert_driving_rating = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        verbose_name=_('تقييم القيادة الصحراوية')
    )
    program_goal = models.TextField(verbose_name=_('ما هو هدفك من التسجيل في البرنامج'))
    committed_to_5_days = models.BooleanField(verbose_name=_('الالتزام بـ 5 أيام'))
    health_conditions = models.TextField(blank=True, verbose_name=_('الحالات الصحية'))
    
    # معلومات إضافية
    residence_region = models.CharField(
        max_length=20,
        choices=REGIONS,
        verbose_name=_('منطقة الإقامة')
    )
    can_travel = models.BooleanField(verbose_name=_('القدرة على السفر'))
    
    # الملفات والموافقات
    profile_photo = models.ImageField(upload_to='photos/', verbose_name=_('الصورة الشخصية'))
    experience_docs = models.FileField(upload_to='documents/', blank=True, null=True, verbose_name=_('مستندات الخبرة'))
    agreed_to_terms = models.BooleanField(default=False, verbose_name=_('موافق على الشروط والأحكام'))
    
    # الحالة والتواريخ
    status = models.CharField(
        max_length=1,
        choices=STATUS_CHOICES,
        default='P',
        verbose_name=_('حالة التسجيل')
    )
    application_date = models.DateTimeField(auto_now_add=True, verbose_name=_('تاريخ التسجيل'))
    updated_date = models.DateTimeField(auto_now=True, verbose_name=_('آخر تحديث'))
    reviewed_date = models.DateTimeField(blank=True, null=True, verbose_name=_('تاريخ المراجعة'))
    
    # ملاحظات المسؤول
    admin_notes = models.TextField(blank=True, verbose_name=_('ملاحظات المسؤول'))
    reviewed_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='reviewed_registrations',
        verbose_name=_('تمت المراجعة من قبل')
    )
    
    # الفهارس
    class Meta:
        verbose_name = 'تسجيل'
        verbose_name_plural = 'التسجيلات'
        ordering = ['-application_date']
        indexes = [
            models.Index(fields=['email']),
            models.Index(fields=['id_number']),
            models.Index(fields=['phone']),
            models.Index(fields=['status']),
            models.Index(fields=['application_date']),
        ]
    
    def __str__(self):
        return f"{self.full_name} - {self.get_category_display()}"
    
    def get_absolute_url(self):
        return reverse('registration_detail', kwargs={'pk': self.pk})

class AdminUser(models.Model):
    """نموذج المسؤول"""
    
    ROLE_CHOICES = [
        ('admin', _('مسؤول')),
        ('reviewer', _('مراجع')),
        ('viewer', _('عارض'))
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name=_('المستخدم'))
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='viewer', verbose_name=_('الدور'))
    department = models.CharField(max_length=100, blank=True, verbose_name=_('القسم'))
    phone = models.CharField(max_length=20, blank=True, verbose_name=_('الهاتف'))
    is_active = models.BooleanField(default=True, verbose_name=_('نشط'))
    
    created_date = models.DateTimeField(auto_now_add=True, verbose_name=_('تاريخ الإنشاء'))
    last_login = models.DateTimeField(blank=True, null=True, verbose_name=_('آخر دخول'))
    
    class Meta:
        verbose_name = 'مسؤول'
        verbose_name_plural = 'المسؤولون'
    
    def __str__(self):
        return f"{self.user.get_full_name()} - {self.get_role_display()}"

class RegistrationStats(models.Model):
    """نموذج الإحصائيات"""
    
    total_registrations = models.PositiveIntegerField(default=0, verbose_name=_('إجمالي التسجيلات'))
    approved = models.PositiveIntegerField(default=0, verbose_name=_('الموافق عليها'))
    pending = models.PositiveIntegerField(default=0, verbose_name=_('قيد الانتظار'))
    rejected = models.PositiveIntegerField(default=0, verbose_name=_('المرفوضة'))
    
    drivers = models.PositiveIntegerField(default=0, verbose_name=_('المتسابقون'))
    navigators = models.PositiveIntegerField(default=0, verbose_name=_('الملاحون'))
    
    male = models.PositiveIntegerField(default=0, verbose_name=_('الذكور'))
    female = models.PositiveIntegerField(default=0, verbose_name=_('الإناث'))
    
    region_breakdown = models.JSONField(default=dict, blank=True, verbose_name=_('توزيع المناطق'))
    
    last_updated = models.DateTimeField(auto_now=True, verbose_name=_('آخر تحديث'))
    
    class Meta:
        verbose_name = 'إحصائية'
        verbose_name_plural = 'الإحصائيات'
    
    def __str__(self):
        return f"الإحصائيات - {self.total_registrations} تسجيل"

class SiteSettings(models.Model):
    """إعدادات النظام العامة"""
    
    registration_open = models.BooleanField(default=True, verbose_name=_('التسجيل متاح'))
    closed_message = models.TextField(
        default=_('عذراً، فترة التسجيل منتهية حالياً. يرجى متابعة قنواتنا الرسمية لأي تحديثات.'),
        verbose_name=_('رسالة إغلاق التسجيل')
    )
    
    class Meta:
        verbose_name = 'إعدادات النظام'
        verbose_name_plural = 'إعدادات النظام'
        
    def __str__(self):
        return "إعدادات النظام"
    
    def save(self, *args, **kwargs):
        # Ensure only one row exists
        if SiteSettings.objects.exists() and not self.pk:
            return SiteSettings.objects.first()
        return super().save(*args, **kwargs)
