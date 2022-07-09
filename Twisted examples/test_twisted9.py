from twisted.internet.task import Clock
from twisted.internet.defer import Deferred
import time

class controlTime:

    start_time = time.time()
    clock = Clock()
    def end_time(self):
        end_time = time.time()
        print(end_time)
        time.sleep(3)
        return end_time

    def delayTime(self, delay=0):
        #clock = Clock()
        self.clock.callLater(delay, self.end_time)
        self.clock.advance(delay)

    def additionalFunc(self, sec):
        final_time = sec - self.start_time
        print(f'You have delayed for: {final_time} s')
    
    def  finalTime(self, g_delay=0):
        #clock = Clock()
        self.clock.callLater(g_delay, self.additionalFunc, self.end_time())
        self.clock.advance(g_delay)

ctrl = controlTime()

deferred_signal = Deferred()
deferred_signal2 = Deferred()

dl1 = deferred_signal.addCallback(ctrl.delayTime)
dl1.callback(3)

dl2 = deferred_signal2.addCallback(ctrl.finalTime)
dl2.callback(3)
