# comparative_programming_languages

### Imperative

​	I will start by outlining the imperative implementation of the calendar. Imperative programming is a paradigm of programming wherein you describe how a program should operate with a set of statements. I chose to write this in python.

##### _The calendar itself:_

​	I initiated the calendar as a dictionary, this was due to a dictionary’s constant search speed. If I were to scale the program up, for perhaps a year or several, this would more heavily impact the search speed of the data; however it has little effect at such a small scale.

##### _The user interface:_

Upon entering the environment, the user is prompted to type __help__. Doing so will give them a list of commands and the correct format to enter them. This was implemented as a function __help()__, and was a series of print statements. The whole program is a command line interface, with commands being read in as a string and dealt with appropriately.

- I chose to write several functions as opposed to not simply for a layer of abstraction. While this is more commonly seen as an attribute of object oriented programming, it is a helpful habit in all areas of programming.

##### _The functions:_

​	The more basic of the functions would be “view()”. The user is given two options, “view week”, and “view <day>” _(where_ <day> _is one of the days of the week)_. Viewing the day will print out the attributes of the day - being appointments and their respective times - and viewing the week is a loop, viewing each day within the week.

​	Apart from this, users may add appointments. After entering the appropriate details, the program first checks to see if the appointment overlaps with any existing appointments. This is done by a function called __no_overlap(params)__. It takes both the start-time and end-time of the requested appointment and compares them to the start and end times of all existing appointments for a given day. This function makes use of another function: __min_conv(param)__, which converts a time into minutes. If there is no overlap, the time is correctly formatted - using the __format_time(param)__ function. This is simply string reformatting and ensuring the time is a valid one. Finally, the function sorts the appointments based on their start times. The key for this sorting makes use of __take_start_time(param)__ function. This returns the start time of an appointment.

​	Furthermore, a user may remove an appointment. This is much simpler, it looks for an appointment in the list of appointments in a given day with the same name as the one provided, and removes it from the list.In addition to this, a user may exit the program by calling the __exit()__ function, this breaks the loop and the process ends.

​	This illustrates imperative programming as the program is told exactly how to do everything, and makes use of functions simply for a layer of abstraction.

___

### Object Oriented

​	The OO approach to this solution was also written in python. This was mainly due to the ease of comparing paradigms when everything else _(the syntax etc.)_ is largely the same. While features such as polymorphism were not used - due to there being no need - the principals are present and I will explain this implementation with regards to the fundamentals of OO design.

​

##### _The Main class:_

​	The main class is initiated with one parameter: __self.week__, which is a __Week__ object. I chose to make a week object instead of letting the main class act as the week because I valued an additional layer of abstraction. This was one of my core aims with this implementation. Design-wise, this let all methods that directly impact the Week object itself be self contained and any other method could be left inside the Main class.

​	The class itself contained two methods: __help()__ and __main()__. The help function printed a list of commands the user could call for the program, and the main method was where our program ran.

##### _The Week class:_

​	This was comprised of a __self._a_days__ parameter and a __self._days__ parameter. The former being an array of strings - for ease of printing in sequence - and the latter being a dictionary mapping the name of the day to a __Day__ object. A getter was provided as is custom in OO design, this is due to Encapsulation, a fundamental principle of OO programming. __add()__ and __remove()__ methods were also provided, functioning similarly to the imperative implementation. These both called methods in the given Day object to carry out their respective methods. A __str()__ method was also provided for print formatting.

##### _The Day class:_

​	This class was initialized with an id - its name - and an array of appointments - initially empty. Adding an appointment initialized a new Appointment object. It first checked for no overlap, using the ___no_overlap(param)__ method, and if this checked out, it would append it to the list and then sort the list with respect to the start time - using __self._take_start_time(param)__. Again, removing an appointment was simpler, and functioned the same as in the imperative. A __str()__ method was again written.

##### _The Appointment class:_

​	Finally, this class had three parameters. An id, a start, and an end. The times were formatted using the __self._format_time(param)__ method. Getters were added also, as well as a __min_conv(param)__ method, to be used outside the class. There is also a __str()__ method for ease of printing.

​	Encapsulation was a priority and the highest degree I could think of was attained, with getters and setters being used liberally. Abstraction was kept to a maximum, not only for readability, but for illustrating OO design also. Polymorphism could not really be attained in a traditional sense, as neither could Inheritance; A soft form of these was achieved with certain classes being comprised of other classes, yet an extension would not be a sufficient implementation.

___

### To compare

​	If you were to look at both implementations at the output level, they are essentially identical. This is also similar on the function/method level. The imperative however, holds everything as standard python data types i.e. strings and tuples. Whereas the OO creates new objects for things such as appointments.

​	While both have abstraction to some degree, the OO has many more layers, and this improves readability of the code, as well as keeping things encapsulated, and easy to maintain should that be required. They both make use of not repeating code, but again, the OO implementation is superior, but this is due to design. It’s drawback being that it is more memory intensive than the imperative.

​	Furthering this, the imperative is self contained in one file, while the OO is spread across multiples files and directories. They have both been given a Batch script to allow them to be ran with “run” executed in the parent directory.

___
