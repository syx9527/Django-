from django.test import TestCase

# Create your tests here.

from bs4 import BeautifulSoup

s = "<h1>hello</h1><span></span><script>1234</script>"
soup = BeautifulSoup(s, "html.parser")
# print(soup.text)
print(soup.find_all())  # 截取所有的标签
for tag in soup.find_all():
    print(tag.name)
    if tag.name == "script":
        tag.decompose()
print(str(soup))
