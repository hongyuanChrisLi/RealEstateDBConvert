from urlparse import urlparse


def parse_url(url):
    res = urlparse(url)
    net_info = res.netloc.split('@')
    cred = net_info[0].split(':')
    loc = net_info[1]
    username = cred[0]
    password = cred[1]
    db = res.path

    print ("jdbc:mysql://" + loc + db)
    print (username + ":" + password)




str = "postgres://kbobzbuqvykwac:9c05185f1fdbc4cc531876ce74051398f3c67d4069a5901adf2b10ad04c412c2@ec2-54-235-245-255.compute-1.amazonaws.com:5432/dfdk8anbam7jf1"

parse_url(str)
