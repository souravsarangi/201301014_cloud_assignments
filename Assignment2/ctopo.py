
import sys

from mininet.net import Mininet
from mininet.node import Controller
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.link import TCLink

from mininet.topo import Topo
def ctopo():

    self = Mininet( controller=Controller , link=TCLink)
    self.addController( 'c0' )
    print "enter Hosts"
    x=int(raw_input())
    print "enter switches"
    y=int(raw_input())
    print x,y
    hosts=[]
    switches=[]

    # Add hosts and switches
    evenip="10.0.1."
    oddip="10.0.2."
    for i in range(x):
        if i%2==0:
            hosts.append(self.addHost('h'+str(i+1),ip=evenip+str(i/2+1)+"/24"))
            print evenip+str(i/2)+"/24"
        if i%2==1:
            hosts.append(self.addHost('h'+str(i+1),ip=oddip+str(((i-1)/2)+1)+"/24"))
            print oddip+str((i-1)/2)+"/24"

    for i in range(y):
        switches.append(self.addSwitch('s'+str(i+1)))
    
    # Add links
    k=0
    if x%y==0:
        p=y
    else:
        p=y-1
    for i in range(p):
        for j in range(x/y):
            if k%2==0:
                self.addLink(hosts[i*(x/y)+j],switches[i], bw=2)
            if k%2==1:
                self.addLink(hosts[i*(x/y)+j],switches[i], bw=1)
            k+=1

    p=x-(y-1)*(x/y)
    for i in range(p):
        if k%2==0:
            self.addLink(hosts[((y-1)*(x/y))+i],switches[y-1],bw=2)
        if k%2==1:
            self.addLink(hosts[((y-1)*(x/y))+i],switches[y-1],bw=1)
        k+=1

    for i in range(y-1):
            self.addLink(switches[i],switches[i+1],bw=2)

    self.start()


    CLI( self )

    self.stop()



if __name__ == '__main__':
    ctopo()
