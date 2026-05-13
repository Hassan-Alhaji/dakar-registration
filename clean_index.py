import re

def clean_index():
    with open('templates/index.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # The issue is we have strings like:
    # {% trans "الرئيسية | {% trans "برنامج" %} {% trans "الجيل القادم" %} - داكار 2027" %}
    # We want to replace inner {% trans "X" %} with just X.
    
    # We can just do string replacements for the known bad ones:
    content = content.replace('{% trans "الرئيسية | {% trans "برنامج" %} {% trans "الجيل القادم" %} - داكار 2027" %}', '{% trans "الرئيسية | برنامج الجيل القادم - داكار 2027" %}')
    content = content.replace('ال{% trans "برنامج" %}', 'البرنامج')
    content = content.replace('{% trans "برنامج" %}', 'برنامج')
    content = content.replace('{% trans "الجيل القادم" %}', 'الجيل القادم')
    content = content.replace('{% trans "اكتشف قدراتك وتحدى الصحراء. هذا هو المكان الذي يبدأ منه طريقك إلى رالي داكار 2027." %}', '{% trans "اكتشف قدراتك وتحدى الصحراء. هذا هو المكان الذي يبدأ منه طريقك إلى رالي داكار 2027." %}')
    
    # Also fix anything like: `{% trans "text {% trans "inner" %} text" %}`
    # To do this safely using regex:
    def remove_nested(match):
        inner = match.group(0)
        # remove outer {% trans " and " %}
        inner_text = inner[10:-3] 
        # remove inner {% trans " and " %}
        inner_text = inner_text.replace('{% trans "', '').replace('" %}', '')
        return '{% trans "' + inner_text + '" %}'
        
    # Find all outer trans tags
    pattern = re.compile(r'\{% trans ".*?" %\}', re.DOTALL)
    # Wait, the regex might stop at the first " %}, let's just do a specific cleanup.
    content = content.replace('{% trans "الرئيسية | برنامج الجيل القادم - داكار 2027" %}', '{% trans "الرئيسية | برنامج الجيل القادم - داكار 2027" %}')
    
    # Actually, simpler: I'll read the original text from my first translate_index script, and revert the file!
    # Wait, I don't have the original text. Let's just fix the specific broken tags:
    content = content.replace('{% trans "الرئيسية | برنامج الجيل القادم - داكار 2027" %}', '{% trans "الرئيسية | برنامج الجيل القادم - داكار 2027" %}')
    
    with open('templates/index.html', 'w', encoding='utf-8') as f:
        f.write(content)

clean_index()
