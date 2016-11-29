# -*- coding:utf-8 -*-
import web
import urllib,urllib2
import json

urls=(
    '/','Index',
    '/s','So'
    )
render=web.template.render('templates')
def geturl(name):
 html=urllib.urlopen('http://s.music.163.com/search/get/?type=1&s=%s&limit=1' %name).read()
 js=json.loads(html)
 return js["result"]['songs'][0]['audio']
class Index(object):
def GET(self):
return render.music()
class So(object):
def GET(self):
name=geturl(web.input().get('name').encode('utf-8'))
print name
url=geturl(urllib.quote(name))
print url
return render.music(url)
if _name_=='_main_':
web.application(urls,globals()).run()

