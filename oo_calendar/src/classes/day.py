from classes.appointment import Appointment

class Day:

    def __init__(self, name=None):
        """ initialized with a name, and a list of appointments
            """
        self._id = name
        self._appointments = []

    def id(self):
        """ returns id
        """
        return self._id

    def appointments(self):
        """ returns appointemnts
        """
        return self._appointments

    def _no_overlap(self, new_app):
        """ check if appointment overlaps with another appointment in the
            given day, returns true if no overlap
        """
        for app in self._appointments:

            na_start = new_app.min_conv(new_app.start())
            na_end = new_app.min_conv(new_app.end())
            app_start = app.min_conv(app.start())
            app_end = app.min_conv(app.end())

            if (na_start < app_start < na_end) or (na_start < app_end < na_end):
                return False
        return True

    def _take_start_time(self, element):
        """ helper function to return start-time for sorting lists
        """
        return element.min_conv(element.start())

    def add_appointment(self, name, start, end):
        """ using the appointment class, we append an appointment object
            to the list, it keeps them in chronological order as well
        """
        name = Appointment(name, start, end)
        if self._no_overlap(name):
            self._appointments.append(name)
            self._appointments.sort(key=self._take_start_time)
        else:
            print("Appointment overlaps with another, cannot reserve time.")

    def remove_appointment(self, name):
        """ removes the selected appointment from the object
        """
        for i in self._appointments:
            if i.id() == name:
                self._appointments.remove(i)
                break

    def __str__(self):
        """ prints the day, and its list of appointments
        """
        apps = []
        if not len(self._appointments):
            return self._id.capitalize()+"\n\n"+"No appointments for this day."+"\n"+"-"*76
            return "{}\n\nNo appointments for this day\n{}".format(
            self._id.capitalize(), "-"*76)
        else:
            for app in self._appointments:
                apps.append(str(app))
            apps.append("-"*76)
            apps = "\n".join(apps)
            return "Appointments for {}\n\n{}".format(
            self._id.capitalize(), apps)
