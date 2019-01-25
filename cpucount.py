#!/usr/bin/python
# by Amador Pahim <apahim AT redhat DOT com>

import glob

cputopology='/sys/devices/system/cpu'

def _getSiblings(sib_file, uniq):
    sib_num = 0
    sib_hexa = []
    sib_dirs = glob.glob('/'.join([cputopology, 'cpu[0-9]*',
                                   'topology', sib_file]))
    for sib_file in sib_dirs:
        with open(sib_file) as f:
            line = f.read().strip()
        values = line.strip().split(",")
        if uniq:
            sib_hexa.extend([f for f in values
                             if f not in sib_hexa])
        else:
            sib_hexa.extend(values)
    for i in sib_hexa:
        sib_dec = int(i, 16)
        while sib_dec:
                sib_num += sib_dec & 1
                sib_dec >>= 1
    return sib_num

def threads():
    cores = _getSiblings('core_siblings', True)
    threads = _getSiblings('thread_siblings', False)
    if threads > cores:
        return threads / 2
    else:
        return threads

def cores():
    cores = _getSiblings('core_siblings', True)
    threads = _getSiblings('thread_siblings', False)
    if threads > cores:
        return cores / 2
    else:
        return cores

def sockets():
    phid = []
    phid_dirs = glob.glob('/'.join([cputopology, 'cpu[0-9]*',
                                    'topology', 'physical_package_id']))
    for phid_file in phid_dirs:
        with open(phid_file) as f:
            value = f.read().strip()
        phid.extend([item for item in value if item not in phid])
    return len(phid)


print "threads: "+str(threads())
print "cores: "+str(cores())
print "sockets: "+str(sockets())
