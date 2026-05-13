import re

def wrap_trans(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replacements
    replacements = [
        ('نموذج <span class="text-neon">التسجيل</span>', '{% trans "نموذج" %} <span class="text-neon">{% trans "التسجيل" %}</span>'),
        ('أكمل النموذج بدقة. كافة البيانات تخضع للمراجعة والتدقيق.', '{% trans "أكمل النموذج بدقة. كافة البيانات تخضع للمراجعة والتدقيق." %}'),
        ('01 / البيانات الشخصية', '{% trans "01 / البيانات الشخصية" %}'),
        ('02 / الخبرات والتراخيص', '{% trans "02 / الخبرات والتراخيص" %}'),
        ('03 / التقييم البدني والمهاري', '{% trans "03 / التقييم البدني والمهاري" %}'),
        ('إرسال طلب التسجيل', '{% trans "إرسال طلب التسجيل" %}'),
    ]

    for old, new in replacements:
        content = content.replace(old, new)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

wrap_trans('templates/registration_form.html')
print('Templates updated!')
