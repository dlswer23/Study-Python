from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError

html = urlopen("http://www.pythonscraping.com/pages/error.html")
print(html.read())