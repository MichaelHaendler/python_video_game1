# import urllib2
# f = urllib2.urlopen('http://www.python.org/')
# print f.read(100)

# import urllib2
# req = urllib2.Request(url='https://localhost/cgi-bin/test.cgi', data='This data is passed to stdin of the CGI')
# f = urllib2.urlopen(req)
# print f.read()

# import urllib2
# response = urllib2.urlopen('http://python.org/')
# html = response.read()
# print html

# import urllib2
# req = urllib2.Request('http://www.voidspace.org.uk')
# response = urllib2.urlopen(req)
# the_page = response.read()
# print the_page

# import urllib2

# req = urllib2.Request('ftp://example.com/')
# response = urllib2.urlopen(req)
# the_page = response.read()
# print the_page

import mechanize
import cookielib
import requests

import urllib2
import urllib3


# for control in br.form.controls:
    # print control
    # print "type=%s, name=%s value=%s" % (control.type, control.name, br[control.name])
	
	
r = requests.get('https://api.github.com', auth=('user', 'pass'))
print r.status_code
	
	