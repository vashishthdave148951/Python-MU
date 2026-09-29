#multilvl inheritance : security ->networksecurity->firewall

class security:
     def protect(self):
        print ('system protection is enabled')
class networksecurity(security):
     def monitor_network(self):
         print('network traffic is monitored')

class firewall (networksecurity):
     def block_traffic(self):
         print('malicious traffic is blocked')

f=firewall()
f.protect()
f.monitor_network()
f.block_traffic()