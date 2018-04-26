import requests
import lxml.html

page = requests.get('http://tieba.baidu.com/p/5664377714').text
doc = lxml.html.document_fromstring(page)
for idx,el in enumerate(doc.cssselect('img.BDE_Image')):
    with open('%03d.jpg' % idx, 'wb') as f:
        f.write(requests.get(el.attrib['src']).content)
