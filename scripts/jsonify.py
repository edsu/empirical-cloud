#!/usr/bin/env python

import re
import json
import fileinput

nodes = set()
edges = {}

for line in fileinput.input():
    match = re.match(r'^ +(\d+) (.+) -> (.+)$', line)
    h1, h2 = match.groups()[1:3]
    nodes.add(h1)
    nodes.add(h2)
    edges[h1] = h2

graph = {}
graph['nodes'] = list(nodes)

print json.dumps(graph, indent=2)
