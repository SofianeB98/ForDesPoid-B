import enum
import threading
import time

class ThreadState(str, enum.Enum):
    IDLE = "IDLE",
    RUNNING = "RUNNING",
    FINISH = "FINISH"

class BaseThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.threadState = ThreadState.IDLE
        self.pauseEvent = threading.Event()
        self.pauseEvent.clear()
        self.startTime = 0.0
        self.elapsedTime = 0.0


    def Sleep(self, t):
        time.sleep(t)
    

    def Wait(self, oth):
        waitingTime = 1.0 / 30.0 #Wait a time based on 30FPS and check between each if other thread is running.
        while(oth.threadState == ThreadState.RUNNING):
            self.Sleep(waitingTime)
    

    def StartTimer(self):
        self.startTime = time.time()
        self.elapsedTime = 0.0


    def PauseTimer(self):
        if self.startTime > 0:
            self.startTime = 0
            self.elapsedTime = time.time() - self.startTime


    def ResumeTimer(self):
        if self.startTime <= 0:
            self.startTime = time.time()
    

    def StartThread(self):
        self.threadState = ThreadState.RUNNING
        self.pauseEvent.set()
        self.StartTimer()
        self.start()
        print("Thread Running")


    def PauseThread(self):
        self.PauseTimer()
        self.pauseEvent.clear()
        print("Pause Thread triggered")
    

    def ResumeThread(self):
        self.ResumeTimer()
        self.pauseEvent.set()
        print("Resume Thread triggered")
    

    def StopThread(self):
        self.PauseThread()
        self.threadState = ThreadState.FINISH