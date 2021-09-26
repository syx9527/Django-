import re

path_url = '/user/login'
a = re.match(r'(^/user/log)|(^/$)', path_url)
print(a.string)

b = [1, 2, 3, 4]
print(i for i in b)

import csv

c = open('mysite3.csv', 'w', newline='')
writer = csv.writer(c)
writer.writerow(['a', 'b', 'c'])
