#!/usr/bin/env python

import re
import json
import fileinput

import pygraph

g = pygraph.graph()

for line in fileinput.input():
    match = re.match(r'^ +(\d+) (.+) -> (.+)$', line)
    h1, h2 = match.groups()[1:3]
    num_links = int(match.group(1))
    if num_links > 13:
        g.add_nodes([h1, h2])
        g.add_edge(h1, h2, wt=num_links)

sameas = {'nodes': [], 'links': []}
node_ids = {}
i = 0

for node in g.nodes():
    sameas['nodes'].append({'nodeName': node})
    node_ids[node] = i
    i += 1

for source, target in g.edges():
    e = {'source': node_ids[source], 'target': node_ids[target]}
    sameas['links'].append(e)

print "var sameas = ",
print json.dumps(sameas, indent=2)

