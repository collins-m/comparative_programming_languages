class Appointment:

    def __init__(self, name=None, start=None, end=None):
        """ initialized with a name, the time it starts, and the time it
            finishes
        """
        self._id = name
        self._start = self._format_time(start)
        self._end = self._format_time(end)

    def id(self):
        """ returns id
        """
        return self._id

    def start(self):
        """ returns start
        """
        return self._start

    def end(self):
        """ returns end
        """
        return self._end

    def min_conv(self, time):
        """ converts time <hh:mm> to minute integer
        """
        hh, mm = time.split(":")
        minutes = (int(hh) * 60) + int(mm)
        return minutes

    def _format_time(self, time):
        """ foramts the time to a valid <hh:mm>
        """
        mins = self.min_conv(time)
        hh = str(mins//60)
        if len(hh) == 1:
            hh = "0{}".format(hh)
        mm = str(mins%60)
        if len(mm) == 1:
            mm = "0{}".format(mm)
        return ":".join([hh, mm])

    def __str__(self):
        """ printed out all the data it is initialized with
        """
        return "{} from {} until {}.".format(
        self._id.capitalize(), self._start, self._end)
