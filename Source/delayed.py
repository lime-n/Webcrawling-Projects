def type_pause(self, type):
    self.paused = type
    return self.paused

def pause(self, delay=0, bool = True) -> None:
    from twisted.internet import task, reactor
    from twisted.internet import reactor

    delayed = task.Clock()
        
    delayed.callLater(delay, self.type_pause, bool)

    delayed.advance(delay)

    print(delayed.seconds())

    #delayed.pump([4, 6]) --- Still figuring out how to correctly implemen this.

    reactor.callLater(delay, self.type_pause, False)