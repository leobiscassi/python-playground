def add_time(t1, t2):
    secs = t1.to_seconds() + t2.to_seconds()

    return MyTime(secs=secs)

def increment(t, secs):
    t.seconds += secs

    while t.seconds >= 60:
        t.seconds -= 60
        t.minutes += 1

    while t.minutes >= 60:
        t.minutes -= 60
        t.hours += 1

class MyTime:
    def __init__(self, hrs=0, mins=0, secs=0):
        """ Create a new MyTime object initialized to hrs, mins, secs.
            The values of mins and secs may be outside the range 0-59,
            but the resulting MyTime objects will be normalized.
        """
        totalsecs = hrs*3600 + mins*60 + secs
        self.hours = totalsecs // 3600
        leftoversecs = totalsecs % 3600
        self.minutes = leftoversecs // 60
        self.seconds = leftoversecs % 60

    def __str__(self):
        return f"{self.hours:02}:{self.minutes:02}:{self.seconds:02}"

    def __add__(self, other):
        return MyTime(secs=self.to_seconds() + other.to_seconds())

    def __sub__(self, other):
        return MyTime(secs=self.to_seconds() - other.to_seconds())

    def increment(self, seconds):
        self.seconds += seconds

        while self.seconds >= 60:
            self.seconds -= 60
            self.minutes += 1

        while self.minutes >= 60:
            self.minutes -= 60
            self.hours += 1

    def to_seconds(self):
        """ Return the number of seconds represented
            by this instance
        """
        return self.hours * 3600 + self.minutes * 60 + self.seconds

    def after(self, time2):
        """Return True if I am strictly greater than time2"""
        return self.to_seconds() > time2.to_seconds()