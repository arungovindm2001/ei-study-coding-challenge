class Satellite:
    def __init__(self):
        self.orientation = "North"
        self.solar_panels = "Inactive"
        self.data = 0

    def status(self):
        print(f"Orientation: {self.orientation}")
        print(f"Solar panels: {self.solar_panels}")
        print(f"Data collected: {self.data}")
    
    def rotate(self, orientation):
        self.orientation = orientation
        print(self.orientation)
    
    def activatePanels(self):
        self.solar_panels = "Active"
        print(self.solar_panels)
    
    def deactivatePanels(self):
        self.solar_panels = "Inactive"
        print(self.solar_panels)
    
    def collectData(self):
        if self.solar_panels == "Active":
            self.data += 10
            print(self.data)
        else:
            print("Data can't be collected since solar panels are not active")

def main():
    satellite = Satellite()
    satellite.status()

if __name__ == "__main__" :
    main()
