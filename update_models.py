import re

with open('registration/models.py', 'r', encoding='utf-8') as f:
    content = f.read()

if 'from django.utils.translation import gettext_lazy as _' not in content:
    content = content.replace('from django.db import models', 'from django.db import models\nfrom django.utils.translation import gettext_lazy as _')

content = re.sub(r"verbose_name='([^']+)'", r"verbose_name=_('\1')", content)
content = re.sub(r"\('([^']+)',\s*'([^']+)'\)", r"('\1', _('\2'))", content)

with open('registration/models.py', 'w', encoding='utf-8') as f:
    f.write(content)
