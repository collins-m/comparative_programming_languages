from classes.week import Week

class Main:

    def __init__(self):
        self._week = Week()

    def _help(self):
        """ prints the user manual
        """
        print("-"*76)
        print("Add an appointment:")
        print("add <day> <name of appointment> start-time <hh:mm> finish-time <hh:mm> -24hr")
        print("-"*76)
        print("Remove an appointment:")
        print("remove <day> <name of appointment>")
        print("-"*76)
        print("View appointments for whole week:")
        print("view week")
        print("-"*76)
        print("View appointments for given day:")
        print("view <day>")
        print("-"*76)
        print("To exit program:")
        print("exit")
        print("-"*76)


    def main(self):
        """ Runs the program and initializes the environment
        """
        print("Welcome to OO Calendar in python.")
        print("Type \"help\" for a list of commands.")
        print("-"*76)
        while 1:
            command = input().split()
            print()

            if command[0] == "exit":
                print("Goodbye.")
                break

            elif command[0] == "help":
                self._help()

            elif command[0] == "view":
                if command[1] == "week":
                    print(str(self._week))
                else:
                    print(str(self._week.get()[command[1]]))

            elif command[0] == "add":
                self._week.add(command[1:])

            elif command[0] == "remove":
                self._week.remove(command[1:])
                
if __name__ == "__main__":
    main = Main()
    main.main()
