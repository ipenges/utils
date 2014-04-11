'''
Created on Mar 20, 2014

@author: peng
'''
import socket
import commands


# http://goo.gl/wAFjgA
def get_internal_ipaddr():
    '''get internal ip address
    '''
    return commands.getoutput("/sbin/ifconfig").split("\n")[1].split()[1][5:]


# http://goo.gl/wAFjgA
def get_internal_ipaddr2():
    '''get internal ip address
    '''
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("gmail.com", 80))
    ipaddr = s.getsockname()[0]
    s.close()
    return ipaddr
