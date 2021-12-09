

def domain_name(url):
    url = url.split("//")[-1].split("/")[0]
    url = url.split('.')
    if url[0] == 'www':
        return url[1]
    else:
        return url[0]

print(domain_name("https://youtube.com"))


import re
def domain_name(url):
    return re.search('(https?://)?(www\d?\.)?(?P<name>[\w-]+)\.', url).group('name')