import requests

my_url = str(input("Enter the link: "))
r = requests.head(my_url, allow_redirects  =  True)

def downloadable(url):
    header = r.headers
    type = header.get('content-type')
    if 'html' in type.lower() or 'text' in type.lower():
        return False
    return True

while downloadable(my_url):
    n = str(input("Enter file name with extension: "))
    open(n, 'wb').write(r.content)
    break