class Engine:
    def __init__(self):
        self.bore = 83 # mm
        self.stroke = 90 # mm
        self.cylinders = 5
        self.top_cavity = 40 # cc
        self.piston_cavity = 7 # cc
        self.headgasket = 1 # mm

        self.max_boost = 0 # bar
        self.air_temp = 25 # C
        self.mos = 0 # meters over sea
        self.injector = 570 # cc/min

        # non configable
        self.rpm = 4400
        self.af = 14.8
        self.fuel_density = 720 # kg/m3
        self.auto_ign_temp = 280 # c

        self.displacement = 0
        self.over_tdc_vol = 0
        self.compression = 0
        self.intake_air_pressure = 0
        self.imep = 0
        self.bore_area = 0
        

    def calc_setup(self):
        pass

    def calc_iterate(self):
        pass
