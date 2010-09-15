#!/usr/bin/env python

import re
import json
import fileinput

from rdflib import Graph, URIRef, BNode, Literal
from rdflib import Namespace
from rdflib.namespace import RDF

g = Graph()
VOID = Namespace("http://rdfs.org/ns/void#")
DCTERMS = Namespace("http://purl.org/dc/terms/")
FOAF = Namespace("http://xmlns.com/foaf/0.1/")
OWL = Namespace("http://www.w3.org/2002/07/owl#")


def get_dataset(hostname):
    # returns existing bnode for dataset associated with hostname or a new bnode
    for s in g.subjects(DCTERMS.title, Literal(hostname)):
        return s
    return BNode()


for line in fileinput.input():
    match = re.match(r'^ *(\d+) (.+) -> (.+)$', line)

    num_links = int(match.group(1))
    h1 = match.group(2)
    h2 = match.group(3)

    dataset1 = get_dataset(h1)
    dataset2 = get_dataset(h2)
    linkset = BNode()

    if num_links > 13:
        g.add((dataset1, RDF.type, VOID.Dataset))
        g.add((dataset1, DCTERMS.title, Literal(h1)))
        g.add((dataset1, FOAF.homepage, URIRef("http://%s" % h1)))
        g.add((dataset2, RDF.type, VOID.Dataset))
        g.add((dataset2, DCTERMS.title, Literal(h2)))
        g.add((dataset2, FOAF.homepage, URIRef("http://%s" % h2)))
        g.add((linkset, RDF.type, VOID.LinkSet))
        g.add((linkset, VOID.subjectsTarget, dataset1))
        g.add((linkset, VOID.objectsTarget, dataset2))
        g.add((linkset, VOID.numberOfTriples, Literal(num_links)))
        g.add((linkset, VOID.linkPredicate, OWL.sameAs))

g.bind('dcterms', DCTERMS)
g.bind('void', VOID)
g.bind('foaf', FOAF)
g.bind('owl', OWL)
print g.serialize()
