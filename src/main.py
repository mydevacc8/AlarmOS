from apscheduler.schedulers.background import BackgroundScheduler

class Time():
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def updateTime(self):
        self.seconds +=1
        if self.seconds == 60:
            self.seconds = 0
            self.minutes += 1
        if self.minutes == 60:
            self.minutes = 0
            self.hours += 1
        if self.hours == 24:
            self.hours = 0

    def getHours(self):
        return str(self.hours)

    def getMinutes(self):
        return str(self.minutes)

    def getSeconds(self):
        return str(self.seconds)

time = Time(0,0,0)
#Print current time
def printTime():
    print("%2s:%2s:%2s"% (time.getHours().zfill(2), time.getMinutes().zfill(2), time.getSeconds().zfill(2)))
    time.updateTime()

#Set up scheduler to run every second
sched = BackgroundScheduler()
sched.add_job(printTime, 'interval', seconds=1)
sched.start()


#Live loop
while(True):
    pass
