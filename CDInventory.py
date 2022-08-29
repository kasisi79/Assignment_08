#------------------------------------------#
# Title: CDInventory.py
# Desc: Assignnment 08 - Working with classes
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, created file
# DBiesinger, 2030-Jan-01, added pseudocode to complete assignment 08
# KHarris, 2022-Aug-28, complete tasks in pseudocode
#------------------------------------------#

# -- DATA -- #
strFileName = 'cdInventory.txt'
lstOfCDObjects = []

class CD(object):
    """Stores data about a CD:

    properties:
        cd_id: (int) with CD ID
        cd_title: (string) with the title of the CD
        cd_artist: (string) with the artist of the CD
    methods:

    """
    def __init__(self, cd_id, cd_title, cd_artist):
        # -- Attributes -- #
        self.cd_id = cd_id
        self.cd_title = cd_title
        self.cd_artist = cd_artist

    # -- Properties -- #
    @property
    def cd_id(self):
        return self.__cd_id.title()

    @cd_id.setter
    def cd_id(self, value):
        self.__cd_id = value

    @property
    def cd_title(self):
        return self.__cd_title.title()

    @cd_title.setter
    def cd_title(self, cdname):
        self.__cd_title = cdname

    @property
    def cd_artist(self):
        return self.__cd_artist.title()

    @cd_artist.setter
    def cd_artist(self, artist):
        self.__cd_artist = artist

# -- PROCESSING -- #
class FileIO(object):
    """Processes data to and from file:

    properties:

    methods:
        save_inventory(file_name, lst_Inventory): -> None
        load_inventory(file_name): -> (a list of CD objects)

    """
    def __init__(self,file_name):
       self.file_name = file_name

    @property
    def file_name(self):
        return self.__file_name.title

    @file_name.setter
    def file_name(self, readfile):
        self.__file_name = readfile
        try:
            objFile = open(file_name, 'r')
        except FileNotFoundError:
            print('Please check file name.  It should be CDInventory.txt >>> Custom Response')
            print()
        for line in objFile:
            data = line.strip().split(',')
            dicRow = {'ID': int(data[0]), 'Title': data[1], 'Artist': data[2]}
            lst_Inventory.append(dicRow)
        objFile.close()

    def __init__(self,file_name, lst_Inventory):
        self.file_name = file_name
        self.lst_inventory = lst_Inventory

    @property
    def file_name(self):
        return self.__file_name.title()

    @file_name.setter
    def file_name(self, writefile):
        self.__file_name = writefile
    try:
        objFile = open(file_name, 'w')
    except FileNotFoundError:
        print('Please check file name.  It should be CDInventory.txt >>> Custom Response')
        print()

    @property
    def lst_Inventory(self):
        return self.__lst_Inventory.title()

    def lst_Inventory(self, table):

        for row in lst_Inventory:
            lstValues = list(row.values())
            lstValues[0] = str(lstValues[0])
            objFile.write(','.join(lstValues) + '\n')
        objFile.close()



# -- PRESENTATION (Input/Output) -- #

class IO(object):
    """Displays a menu of choices to the user

          Args:
              None.

          Returns:
              None.
        """

    @staticmethod.menu
    def __init__(self, menu1, menu2):
        # --Attributes-- #
        self.menu1 = menu1
        self.menu2 = menu2

    # --Properties-- #
    @property
    def menu1(self):
        return self.__menu1.title

    @menu1.setter
    def menu1(self, first):
        self.__menu1 = first

    @property
    def menu2(self):
        return self.__menu1.title

    @menu2.setter
    def menu2(self, second):
        self.__menu2 = second

    # --methods -- #
    objMenu = IO.menu1('Menu\n\n[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
    objMenu = IO.menu2('[d] delete CD from Inventory\n[s] Save Inventory to file\n[x] exit\n')

    # @staticmethod.choice
    def menu_choice():
        """Gets user input for menu selection
        Args:
            None.
        Returns:
            Return choice
            choice (string): a lower case sting of the users input out of the choices l, a, i, d, s or x
        """
    def __init__(self, choice):
        # --Attributes-- #
        self.choice = choice
        # choice = ' '
        while choice not in ['l', 'a', 'i', 'd', 's', 'x']:
            choice = input('Which operation would you like to perform? [l, a, i, d, s or x]: ').lower().strip()
        print()  # Add extra space for layout

    @property
    def choice(self):
        return self.__choice.title()

    @choice.setter
    def choice(self, schoice):
        self.__choice = schoice
objChoice = input(IO.menu_choice('Which operation would you like to perform? [l, a, i, d, s, or x]: ').lower().strip())


    # @staticmethod.show
    def __init__(self,lst_Inventory):
        self.lst_table = lst_Inventory

    @property
    def lst_Inventory(self):
        return self.__lst_Inventory.title[]

    @lst_Inventory.setter
    def lst_Inventory(self, inventory):
        self.__lst_Inventory.title[] = inventory
        for row in lst_Inventory:
            print('{}\t{} (by:{})'.format(*row.values()))
        """Displays current inventory table
        
        Args:
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime.

        Returns:
            None.

        """
        print('======= The Current Inventory: =======')
        print('ID\tCD Title (by: Artist)\n')
        for row in lst_Inventory:
            print('{}\t{} (by:{})'.format(*row.values()))
        print('======================================')

    @property
    def lst_Inventory(self):
        print('======= The Current Inventory: =======')
        print('ID\tCD Title (by: Artist)\n')
        for row in lst_Inventory:
            print('{}\t{} (by:{})'.format(*row.values()))
        print('======================================')

# -- Main Body of Script -- #
# Load data from file into a list of CD objects on script start

    while True:
        IO.print_menu()
        user_choice = IO.menu_choice()
        if user_choice == 'x':
            break
        if user_choice == 'l':
            print('WARNING: If you continue, all unsaved data will be lost and the Inventory re-loaded from file.')
            strYesNo = input('type \'yes\' to continue and reload from file. otherwise reload will be canceled')
            if strYesNo.lower() == 'yes':
                print('reloading...')
                FileIO.read_file(strFileName, lst_Inventory)
                IO.show_inventory(lst_Inventory)
            else:
                input('canceling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu.')
                IO.show_inventory(lst_Inventory)
            continue  # start loop back at top.

        elif user_choice == 'a':

            IO.show_inventory(lst_Inventory)

            continue  # start loop back at top.

        elif user_choice == 'i':
            IO.show_inventory(lst_Inventory)
            continue  # start loop back at top.

        elif user_choice == 'd':

            IO.show_inventory(lst_Inventory)

            try:
                intIDDel = int(input('Which ID would you like to delete? ').strip())
            except ValueError:
                print('The value entered is not an integer.  Please try again later. >>> Custom Response')
                break

            DataProcessor.DeleteEntry(intIDDel)
            IO.show_inventory(lst_Inventory)
            continue  # start loop back at top.
        elif user_choice == 's':

    IO.show_inventory(lst_Inventory)
    strYesNo = input('Save this inventory to file? [y/n] ').strip().lower()
    # 3.6.2 Process choice
    if strYesNo == 'y':
       FileIO.write_file(strFileName, lst_Inventory)
    else:
        input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')
    continue  # start loop back at top.

else:
print('General Error')
    # let user load inventory from file
    # let user exit program

