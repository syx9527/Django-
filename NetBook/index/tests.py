from django.test import TestCase

# Create your tests here.
from django.core import mail

print('-------------')
a = mail.send_mail(subject="老鼠爱吃鱼sss", message="老鼠爱吃鱼,大象爱吃虾米", from_email='1276034292@qq.com',
                   recipient_list=['1276034292@qq.com'])
print(a)
print('-------------')
