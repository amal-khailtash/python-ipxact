#!/usr/bin/env python

import os
import subprocess
import sys

SCRIPT_PATH = os.path.dirname(os.path.realpath(__file__))
PROJ_ROOT = os.path.realpath(os.path.join(SCRIPT_PATH, '..'))

SCHEMA_ROOT = 'http://www.accellera.org/XMLSchema/'

SCHEMA_VERSIONS = {
    '1.0' : 'SPIRIT',
    '1.1' : 'SPIRIT',
    '1.2' : 'SPIRIT',
    '1.4' : 'SPIRIT',
    '1.5' : 'SPIRIT',
  # '1685-2009-VE-1.0' : 'SPIRIT',
    '1685-2009' : 'SPIRIT',
    '1685-2014' : 'IPXACT',
}

for version, path in sorted(SCHEMA_VERSIONS.items()):
    module = 'v' + version.replace('.', '_').replace('-', '_')
    print("Generating class binding for '{}' version '{} ({})'...".format(
        path, version, module))

    output_dir = os.path.join(PROJ_ROOT, 'accellera', path.lower())
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    f = open(os.path.join(output_dir, module+'.log'), 'w')
    command = ['pyxbgen',
            '--binding-root='+output_dir,
            '--schema-location='+SCHEMA_ROOT + path + '/' + version + '/index.xsd',
            '--module', module]
    # print(command)
    subprocess.call(command, stdout=f, stderr=f)
