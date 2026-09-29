class securitysystem:
      def monitor(self):
            print('Network is monitored')
class IDS(securitysystem):
      def detect(self):
            print('Intrussion detected')  
class IPS(securitysystem):
      def prevent(self):
            print('Threat is prevented')
i=IDS()
p=IPS()
i.monitor()
i.detect()
p.prevent()

