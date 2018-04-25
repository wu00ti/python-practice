import urllib.request
import re

def find_links(website):
    html_content = urllib.request.urlopen(website).read()
    r = re.compile('href="(.*?)"')
    result = r.findall(html_content.decode())
    return result

if __name__ == '__main__':
    print(find_links('http://www.taobao.com/'))
