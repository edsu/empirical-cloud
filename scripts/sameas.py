#!/usr/bin/env python

import re
import urlparse
import fileinput

def urlize(s):
    return s.lstrip('<').rstrip('>')

for line in fileinput.input():
    line = line.strip()
    if not line: continue

    s, p, o, c = line.split("\t")
    if p == '<http://www.w3.org/2002/07/owl#sameAs>':
        h1 = urlparse.urlparse(urlize(s))
        h2 = urlparse.urlparse(urlize(o))
        if h1.netloc and h2.netloc and h1.netloc != h2.netloc:
            print "%s -> %s" % (h1.netloc, h2.netloc)