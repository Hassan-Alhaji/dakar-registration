import os
import polib

TRANSLATIONS = {
    # === Page Titles ===
    'الرئيسية | برنامج الجيل القادم - داكار 2027': 'Home | Next Gen Program - Dakar 2027',
    'برنامج الجيل القادم - داكار 2027': 'Next Gen Program - Dakar 2027',
    'تسجيل مشارك | برنامج الجيل القادم': 'Register | Next Gen Program',
    'تم التسجيل بنجاح | برنامج الجيل القادم': 'Registration Successful | Next Gen Program',

    # === Navbar ===
    'الرئيسية': 'Home',
    'التسجيل': 'Registration',
    'سجل في المعسكر': 'Register in Camp',
    'الشروط': 'Terms',
    'مركز القيادة': 'Dashboard',

    # === Loader ===
    'شغل المحرك...': 'Start Engine...',

    # === Hero Section (index.html) ===
    'الجيل القادم': 'Next Gen',
    'الجيل': 'Next',
    'القادم.': 'Gen.',
    'البرنامج الوطني الأضخم لاستقطاب وتدريب المواهب السعودية الشابة في عالم الراليات والمحركات. طريقك نحو تمثيل المملكة في رالي داكار 2027 يبدأ من معسكر بيشة.': 'The largest national program for recruiting and training young Saudi talents in the world of rallying and motorsports. Your path to representing the Kingdom in Dakar Rally 2027 starts from Bisha Camp.',
    'سجل الآن': 'Register Now',
    'اكتشف البرنامج': 'Discover the Program',

    # === Marquee Divider ===
    'الراليات الصحراوية': 'Desert Rallies',
    'الفورمولا والكارتينج': 'Formula & Karting',
    'الأوتوكروس': 'Autocross',
    'الدرفت': 'Drifting',
    'كسر الزمن': 'Time Attack',
    'الدراجات النارية': 'Motorcycles',

    # === About Section ===
    'عن': 'About',
    'البرنامج': 'The Program',
    'تطلق وزارة الرياضة بالتعاون مع الاتحاد السعودي للسيارات والدراجات النارية برنامج الجيل القادم ضمن رؤية 2030 لتمكين أبطال المستقبل.': 'The Ministry of Sports, in cooperation with the Saudi Automobile and Motorcycle Federation, launches the Next Gen Program under Vision 2030 to empower future champions.',
    'نبحث عن السائقين والملاحين الذين يمتلكون الشغف الحقيقي، الإرادة الصلبة، والمهارة الفطرية للتعامل مع أقسى التضاريس. سيتم اختيار نخبة من المتقدمين للانضمام إلى معسكر تدريبي مغلق ومكثف في مدينة بيشة.': 'We are looking for drivers and navigators who possess true passion, solid willpower, and natural skills to handle the toughest terrains. An elite group of applicants will be selected to join a closed intensive training camp in Bisha.',
    'تدريب عملي ونظري مكثف لمدة 5 أيام': 'Intensive practical and theoretical training for 5 days',
    'سيارات رالي مجهزة بالكامل ومسارات قاسية حقيقية': 'Fully equipped rally cars and real tough tracks',
    'تقييم شامل للمهارات القيادية والملاحية': 'Comprehensive assessment of driving and navigation skills',
    'داكار 2027': 'Dakar 2027',
    'الهدف النهائي': 'The Ultimate Goal',

    # === Conditions Cards ===
    'والمعايير': 'and Standards',
    'العمر والخبرة': 'Age & Experience',
    'يجب ألا يقل عمر المتقدم عن 16 عاماً. يفضل وجود خبرة سابقة في أي من رياضات المحركات (رالي، كارتينج، أوتوكروس)، ولكن الشغف والالتزام هما المعيار الأهم للقبول المبدئي في البرنامج.': 'Applicants must be at least 16 years old. Previous experience in any motorsport (rally, karting, autocross) is preferred, but passion and commitment are the most important criteria for initial acceptance into the program.',
    'اللياقة والصحة': 'Fitness & Health',
    'رياضة الراليات تتطلب قدرة تحمل بدنية وذهنية هائلة. يجب على المتقدم اجتياز الفحوصات الطبية المعتمدة من الاتحاد، والإفصاح عن أي حالات صحية قد تؤثر على سلامته أثناء القيادة في ظروف قاسية.': 'Rally motorsport requires tremendous physical and mental endurance. Applicants must pass federation-approved medical examinations and disclose any health conditions that may affect their safety while driving in harsh conditions.',
    'الالتزام التام': 'Full Commitment',
    'المعسكر التدريبي في بيشة يتطلب تفرغاً تاماً لمدة 5 أيام متتالية. سيتم استبعاد أي متدرب يخل بجدول المعسكر أو لا يظهر الالتزام الكافي بقواعد السلامة وتعليمات المدربين.': 'The training camp in Bisha requires full dedication for 5 consecutive days. Any trainee who disrupts the camp schedule or fails to show sufficient commitment to safety rules and instructor guidelines will be excluded.',

    # === CTA Section ===
    'هل أنت': 'Are you',
    'مستعد؟': 'Ready?',
    'المقاعد محدودة جداً ولن تقبل إلا طلبات النخبة. قم بتعبئة الاستمارة الآن بدقة، وأرفق صوراً واضحة لرخصك وإثباتات خبراتك إن وجدت.': 'Seats are extremely limited and only elite applications will be accepted. Fill out the form accurately now, and attach clear photos of your licenses and proof of your experience if any.',
    'بدء عملية التسجيل': 'Start Registration',

    # === Registration Form ===
    'لوحة': 'Registration',
    'هذه هي نقطة الانطلاق. تأكد من إدخال جميع بياناتك بدقة لتزيد من فرص قبولك في المعسكر التجريبي بمدينة بيشة.': 'This is the starting point. Make sure to enter all your data accurately to increase your chances of acceptance in the training camp in Bisha.',
    'الحقول المميزة بـ (*) إلزامية.': 'Fields marked with (*) are required.',
    '01 / هويتك الشخصية': '01 / Personal Identity',
    '02 / التراخيص والخبرة الفنية': '02 / Licenses & Technical Experience',
    'حدد أنواع السباقات التي شاركت بها:': 'Select the race types you have participated in:',
    '03 / التقييم البدني والمهاري': '03 / Physical & Skill Assessment',
    'قيم قدراتك في القيادة على الكثبان الرملية (1-5)': 'Rate your desert dune driving skills (1-5)',
    'اكتب بوضوح دافعك الرئيسي. نبحث عن الشغف الحقيقي، لا الكلمات المنمقة.': 'Write your main motivation clearly. We are looking for true passion, not fancy words.',
    'الرالي يتطلب مجهوداً عالياً. الرجاء الإفصاح عن أي ظروف طبية للحرص على سلامتك.': 'Rallying requires high physical effort. Please disclose any medical conditions to ensure your safety.',
    '04 / المرفقات والالتزام': '04 / Attachments & Commitment',
    'السيرة الذاتية أو سجل الإنجازات (اختياري)': 'CV or achievements record (optional)',
    'إرسال طلب التسجيل': 'Submit Application',

    # === Model fields ===
    'الاسم الكامل': 'Full Name',
    'العمر': 'Age',
    'الجنس': 'Gender',
    'رقم الهوية': 'ID Number',
    'الجنسية': 'Nationality',
    'رقم الجوال': 'Phone Number',
    'البريد الإلكتروني': 'Email',
    'الفئة': 'Category',
    'رخصة القيادة': 'Driving License',
    'الرخصة الرياضية': 'Sports License',
    'رقم الرخصة الرياضية': 'Sports License Number',
    'خبرة سابقة': 'Previous Experience',
    'أنواع السباقات': 'Race Types',
    'عدد السباقات': 'Number of Races',
    'سنوات الخبرة': 'Years of Experience',
    'تقييم القيادة الصحراوية': 'Desert Driving Rating',
    'ما هو هدفك من التسجيل في البرنامج': 'What is your goal from registering in the program?',
    'الالتزام بـ 5 أيام': 'Committed to 5 days',
    'الحالات الصحية': 'Health Conditions',
    'منطقة الإقامة': 'Residence Region',
    'القدرة على السفر': 'Can Travel',
    'الصورة الشخصية': 'Profile Photo',
    'مستندات الخبرة': 'Experience Docs',
    'حالة التسجيل': 'Registration Status',
    'تاريخ التسجيل': 'Application Date',
    'تاريخ التحديث': 'Updated Date',
    'تاريخ المراجعة': 'Reviewed Date',
    'ملاحظات المسؤول': 'Admin Notes',
    'مراجع من قبل': 'Reviewed By',

    # === Model choices ===
    'ذكر': 'Male',
    'أنثى': 'Female',
    'متسابق': 'Driver',
    'ملاح': 'Navigator',
    'قيد الانتظار': 'Pending',
    'موافق عليه': 'Approved',
    'مرفوض': 'Rejected',
    'متراجع عنه': 'Withdrawn',
    'من 1 إلى 2 سنة': '1 to 2 years',
    'من 2 إلى 5 سنوات': '2 to 5 years',
    'أكثر من 5 سنوات': 'More than 5 years',
    'الراليات': 'Rallies',
    'الكارتينج': 'Karting',
    'كسر الزمن': 'Time Attack',
    'الدراجات النارية': 'Motorcycles',

    # === Regions ===
    'الرياض': 'Riyadh',
    'مكة المكرمة': 'Makkah',
    'المدينة المنورة': 'Medina',
    'المنطقة الشرقية': 'Eastern Region',
    'عسير': 'Asir',
    'الباحة': 'Al Baha',
    'المنطقة الشمالية': 'Northern Region',
    'القصيم': 'Qassim',
    'حائل': 'Hail',
    'جازان': 'Jazan',
    'نجران': 'Najran',

    # === Success page ===
    'تم الإرسال': 'Submitted',
    'شكراً، وسيتم التواصل معك قريباً. نتمنى لك كل التوفيق.': 'Thank you. We will contact you soon. We wish you all the best.',
    'تم التسجيل بنجاح | برنامج الجيل القادم': 'Registration Successful | Next Gen Program',

    # === Footer ===
    'البرنامج الوطني لاكتشاف المواهب السعودية في رياضة المحركات، برعاية الاتحاد السعودي للسيارات والدراجات النارية.': 'The National Program for Discovering Saudi Talents in Motorsports, sponsored by the Saudi Automobile and Motorcycle Federation.',
    'جميع الحقوق محفوظة للإتحاد السعودي للسيارات والدراجات النارية &copy; 2026': 'All Rights Reserved to the Saudi Automobile and Motorcycle Federation &copy; 2026',

    # === Admin ===
    'مسؤول': 'Admin',
    'مراجع': 'Reviewer',
    'عارض': 'Viewer',
    'المستخدم': 'User',
    'الدور': 'Role',
    'القسم': 'Department',
    'الهاتف': 'Phone',
    'نشط': 'Active',
    'تاريخ الإنشاء': 'Created Date',
    'آخر دخول': 'Last Login',
    'تمت المراجعة من قبل': 'Reviewed By',
    'آخر تحديث': 'Last Updated',
    'نعم': 'Yes',
    'لا': 'No',

    # === CAPTCHA ===
    'تحقق أنك لست روبوت': 'Verify you are not a robot',
    'سؤال جديد': 'New question',
    'الإجابة غير صحيحة، حاول مرة أخرى.': 'Incorrect answer, please try again.',

    # === Login Page ===
    'تسجيل الدخول': 'Login',
    'تسجيل': 'Login',
    'الدخول': 'Access',
    'مخصص لفريق الإدارة والمراجعين فقط.': 'For admin and review team only.',
    'اسم المستخدم أو كلمة المرور غير صحيحة.': 'Invalid username or password.',
    'اسم المستخدم': 'Username',
    'كلمة المرور': 'Password',
    'دخول': 'Sign In',
    'العودة للرئيسية': 'Back to Home',

    # === Dashboard ===
    'لوحة التحكم': 'Dashboard',
    'لوحة تحكم الإدارة': 'Admin Dashboard',
    'عرض كل التسجيلات': 'View All Registrations',
    'إجمالي التسجيلات': 'Total Registrations',
    'الموافق عليها': 'Approved',
    'قيد الانتظار': 'Pending',
    'المرفوضة': 'Rejected',
    'أحدث التسجيلات': 'Recent Registrations',
    'الاسم': 'Name',
    'المنطقة': 'Region',
    'التاريخ': 'Date',
    'الحالة': 'Status',
    'الإجراء': 'Action',
    'موافق عليه': 'Approved',
    'مرفوض': 'Rejected',
    'متراجع': 'Withdrawn',
    'تفاصيل': 'Details',
    'لا توجد تسجيلات بعد': 'No registrations yet',
    'توزيع الفئات': 'Category Distribution',
    'المتسابقون': 'Drivers',
    'الملاحون': 'Navigators',
    'الذكور / الإناث': 'Male / Female',
    'ذكور': 'Males',
    'إناث': 'Females',
    'تحميل Excel': 'Download Excel',

    # === Detail & List Pages ===
    'تفاصيل التسجيل': 'Registration Details',
    'تفاصيل طلب:': 'Application Details:',
    'العودة للقائمة': 'Back to List',
    'العودة للوحة التحكم': 'Back to Dashboard',
    'تاريخ التسجيل:': 'Registration Date:',
    'حالة الطلب:': 'Application Status:',
    'قبول': 'Approve',
    'رفض': 'Reject',
    'انتظار': 'Pending',
    'معلومات شخصية': 'Personal Information',
    'معلومات رياضية وفنية': 'Sports & Technical Info',
    'سنة': 'years',
    'الجوال': 'Phone',
    'التقييم والإجابات': 'Assessment & Answers',
    'ملتزم تماماً': 'Fully Committed',
    'غير ملتزم': 'Not Committed',
    'الهدف من البرنامج': 'Program Goal',
    'لا يوجد': 'None',
    'المرفقات': 'Attachments',
    'تحميل المستند': 'Download Document',
    'صورة شخصية': 'Profile Photo',
    'قائمة التسجيلات': 'Registrations List',
    'السابق': 'Previous',
    'التالي': 'Next',
    'صفحة': 'Page',
}

po = polib.POFile(encoding='utf-8')
po.metadata = {
    'Project-Id-Version': '1.0',
    'Report-Msgid-Bugs-To': '',
    'POT-Creation-Date': '2026-05-13 12:00+0300',
    'PO-Revision-Date': '2026-05-13 12:00+0300',
    'Last-Translator': 'Auto <auto@example.com>',
    'Language-Team': 'English <en@example.com>',
    'MIME-Version': '1.0',
    'Content-Type': 'text/plain; charset=utf-8',
    'Content-Transfer-Encoding': '8bit',
    'Language': 'en',
}

for ar_str, en_str in TRANSLATIONS.items():
    entry = polib.POEntry(msgid=ar_str, msgstr=en_str)
    po.append(entry)

os.makedirs('locale/en/LC_MESSAGES', exist_ok=True)
po.save('locale/en/LC_MESSAGES/django.po')
po.save_as_mofile('locale/en/LC_MESSAGES/django.mo')
print(f'Translation updated: {len(TRANSLATIONS)} entries')
