#!/usr/bin/env perl

# this script reads n-quads on stdin, and writes the same quads separated with tabs to stdout
# the thought being that it is then easier to munge with unix tools like split, grep, etc
# more about n-quads can be found at: http://sw.deri.org/2008/07/n-quads/

use strict;

my $space = qr/ /;
my $uri = qr/<.+?>/;
my $bnode = qr/_:.+?/;
my $langtag = qr/@.+?/;
my $datatype = qr/\^\^$uri/;
my $literal = qr/(?<!\\)".+?(?<!\\)"(?:$langtag|$datatype)?/;

my $nquad = qr/
    ^
    ($uri|$bnode)               # subject
    $space
    ($uri|$bnode)               # predicate
    $space
    ($uri|$bnode|$literal)      # object
    $space
    ($uri)                      # context
    $space
    \.                          # end-of-quad 
    /x;


while (<>) {
    s/\t//;
    my @parts = m/$nquad/;
    print join("\t", @parts), "\n";
}
