import curses

class Satellite:
    """
    Represents a satellite with orientation, solar panel status, and data collection capabilities.

    Attributes:
        orientation (str): Current orientation of the satellite.
        solar_panels (str): Status of the solar panels (Active/Inactive).
        data (int): Amount of data collected by the satellite.

    Methods:
        status(): Prints the current status of the satellite.
        rotate(orientation): Changes the orientation of the satellite.
        activatePanels(): Activates the solar panels.
        deactivatePanels(): Deactivates the solar panels.
        collectData(): Collects data if solar panels are active.

    """
    def __init__(self):
        """
        Initializes a Satellite object with default values.
        """
        self.orientation = "North"
        self.solar_panels = "Inactive"
        self.data = 0

    def status(self):
        """
        Prints the current status of the satellite.
        """
        print(f"\nOrientation: {self.orientation}\nSolar Panels: {self.solar_panels}\nData collected: {self.data}")
    
    def rotate(self, orientation):
        """
        Changes the orientation of the satellite.

        Args:
            orientation (str): The new orientation.

        """
        self.orientation = orientation
        print(self.orientation)
    
    def activatePanels(self):
        """
        Activates the solar panels.
        """
        self.solar_panels = "Active"
        print(self.solar_panels)
    
    def deactivatePanels(self):
        """
        Deactivates the solar panels.
        """
        self.solar_panels = "Inactive"
        print(self.solar_panels)
    
    def collectData(self):
        """
        Collects data if solar panels are active.

        Returns:
            bool: True if data is collected, False otherwise.

        """
        if self.solar_panels == "Active":
            self.data += 10
            print(self.data)
            return True
        else:
            print("Data can't be collected since solar panels are not active")
            return False

def display_menu(menu_win, selected_row_idx):
    """
    Displays the menu in the curses window.

    Args:
        menu_win (curses window): The window where the menu is displayed.
        selected_row_idx (int): The index of the selected row in the menu.

    """
    menu_win.clear()
    menu_win.border()
    h, w = menu_win.getmaxyx()
    for idx, row in enumerate(menu):
        x = w//2 - len(row)//2
        y = h//2 - len(menu)//2 + idx
        if idx == selected_row_idx:
            menu_win.attron(curses.color_pair(1))
            menu_win.addstr(y, x, row)
            menu_win.attroff(curses.color_pair(1))
        else:
            menu_win.addstr(y, x, row)
    menu_win.refresh()

def refresh_dashboard(output_win, satellite):
    """
    Refreshes the dashboard with the current satellite information.

    Args:
        output_win (curses window): The window where the dashboard is displayed.
        satellite (Satellite): The Satellite object containing information.

    """
    output_win.clear()
    output_win.border()
    output_win.addstr(0,int(curses.COLS/2.3), "SATELLITE COMMAND CENTER")
    output_win.addstr(1,1, f"Orientation: {satellite.orientation}")
    output_win.addstr(2,1, f"Panels: {satellite.solar_panels}")
    output_win.addstr(3,1, f"Data collected: {satellite.data}")
    output_win.refresh()

def modify(index, output_win, satellite):
    """
    Modifies the satellite based on the selected menu option.

    Args:
        index (int): The index of the selected menu option.
        output_win (curses window): The window where the dashboard is displayed.
        satellite (Satellite): The Satellite object to be modified.

    """
    if index == 0:
        satellite.rotate("North")
    elif index == 1:
        satellite.rotate("East")
    elif index == 2:
        satellite.rotate("West")
    elif index == 3:
        satellite.rotate("South")
    elif index == 4:
        satellite.activatePanels()
    elif index == 5:
        satellite.deactivatePanels()
    elif index == 6:
        if satellite.collectData() == False:
            output_win.clear()
            output_win.border()
            output_win.addstr(2,int(curses.COLS/2.5), "Satellite needs to be activated to collect data")
            output_win.refresh()
            curses.napms(1000)


def main(stdscr):
    """
    The main function to run the curses-based satellite control program.

    Args:
        stdscr (curses window): The standard screen window.

    """
    satellite = Satellite()

    stdscr.addstr(0,0,"Enter any key to start..")

    curses.curs_set(0)

    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)

    current_row = 0

    width = curses.COLS

    dashboard_win = curses.newwin(6, width, 0, 0)
    menu_win = curses.newwin(len(menu)+2, width, 7, 0)
    menu_win.clear()

    display_menu(menu_win, current_row)
    menu_win.refresh()

    while True:
        refresh_dashboard(dashboard_win, satellite)
        key = stdscr.getch()

        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1
        elif key == curses.KEY_DOWN and current_row < len(menu)-1:
            current_row += 1
        elif key == curses.KEY_ENTER or key in [10,13]:
            modify(current_row, dashboard_win, satellite)
            refresh_dashboard(dashboard_win, satellite)
        elif key == curses.KEY_END:
            satellite.status()
            break

        display_menu(menu_win, current_row)

if __name__ == "__main__" :
    menu = ["Rotate North", "Rotate East", "Rotate West", "Rotate South", "Activate Panel", "Deactivate Panel", "Collect Data"]
    curses.wrapper(main)
