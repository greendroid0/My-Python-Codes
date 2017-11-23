from urllib import request
import re

site = request.urlopen("http://cs.furkan.space/")
page_source = site.read()
text = page_source.decode()

match = re.findall(r'(SIFRE:\w.*)', text)[0].strip(" -->")

print ("%s" % match)
