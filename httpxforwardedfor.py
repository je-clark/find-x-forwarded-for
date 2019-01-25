import re
import sys

def iterate_basic_ip_check(line, target):
    match = re.match('X-Forwarded-For: (\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})',line)
    if match:
        if match.group(1) == target:
            print "Target IP %s found" % target

if __name__ == "__main__":
    pcap_fn = sys.argv[1]
    target_ip = sys.argv[2]
    print "Initiating basic IP check"
    index = 0
    with open(pcap_fn, mode="rb") as pcap:
        print "PCAP Loaded"
        for line in pcap:
            iterate_basic_ip_check(line,target_ip)
