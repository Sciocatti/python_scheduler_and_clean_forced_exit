import signal
import time
import logging

class GracefulKiller:
    kill_now = False
    def __init__(self):
      signal.signal(signal.SIGINT, self.exit_gracefully)
      signal.signal(signal.SIGTERM, self.exit_gracefully)

    def exit_gracefully(self, *args):
        logging.info("Exit signal received. Setting the kill bool to True.")
        self.kill_now = True

if __name__ == '__main__':
    import time
    killer = GracefulKiller()
    while not killer.kill_now:
      time.sleep(1)
      print("doing something in a loop ...")
   
    print("End of the program. I was killed gracefully :)")