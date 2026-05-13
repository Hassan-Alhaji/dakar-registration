import re

templates = [
    'templates/index.html',
    'templates/base.html',
    'templates/registration_form.html',
    'templates/registration_success.html'
]

for t in templates:
    with open(t, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check for nested trans tags
    nested = re.findall(r'\{% trans "[^"]*\{% trans', content)
    if nested:
        print(f'NESTED TAG in {t}: {nested}')
    else:
        print(f'OK (no nested tags): {t}')
