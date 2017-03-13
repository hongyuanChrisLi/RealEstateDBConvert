from urlparse import urlparse


def parse_url(url):
    res = urlparse(url)
    net_info = res.netloc.split('@')
    cred = net_info[0].split(':')
    loc = net_info[1].split(':')
    host = loc[0]
    port = loc[1]
    username = cred[0]
    password = cred[1]
    db = str(res.path).lstrip('/')

    print ('Host: ' + host +
           '\nPort: ' + str(port) +
           '\nDB: ' + db +
           '\nUser: ' + username +
           '\nPass: ' + password)

    return host, port, db, username, password
