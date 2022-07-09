    def delay(self, val=0):
        delay = val
    
    def increment(self, inc=0):
        increment = inc

    def _next_request(self) -> None:
        from twisted.internet import task, reactor
        from twisted.internet import reactor
        from itertools import count

        assert self.slot is not None  # typing
        assert self.spider is not None  # typing

        if self.paused:
            return None

        while not self._needs_backout() and self._next_request_from_scheduler() is not None:
            pass

        if self.slot.start_requests is not None and not self._needs_backout():
            try:
                request = next(self.slot.start_requests)
                self.increment += 1
                

                delay = self.delay
                increment = self.increment
                
                #Here we will pause after a particular delay given a condition
                if delay != 0:
                    logger.info("Request number %s" % self.increment)
                    
                    delayed = task.Clock()
                    if self.increment % increment == 0:
                        
                
                        delayed.callLater(5, self.type_pause, True)
        
                        delayed.advance(5)
                        
                        reactor.callLater(5, self.type_pause, False)

            except StopIteration:
                self.slot.start_requests = None
            except Exception:
                self.slot.start_requests = None
                logger.error('Error while obtaining start requests', exc_info=True, extra={'spider': self.spider})
            else:
                self.crawl(request)

        if self.spider_is_idle() and self.slot.close_if_idle:
            self._spider_idle()
