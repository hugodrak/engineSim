import math

class Engine:
    def __init__(self):
        self.bore = 96 # mm
        self.stroke = 82.8 # mm
        self.cylinders = 6
        self.top_cavity = 44 # cc
        self.piston_cavity = 7 # cc
        self.headgasket = 1 # mm

        self.max_boost = 0 # bar
        self.air_temp = 25 # C
        self.mos = 0 # meters over sea
        self.injector = 950 # cc/min
        self.throttle = 100 # %

        # non configable
        self.rpm = 6800
        self.af = 14.7
        self.fuel_density = 720 # kg/m3
        self.auto_ign_temp = 280 # c

        self.displacement = 0
        self.over_tdc_vol = 0
        self.compression = 0
        self.intake_air_pressure = 0
        self.imep = 0
        self.bore_area = 0
        self.F_tdc = 0
        self.F_bdc = 0
        self.delta_f = 0
        self.air_density = 0

        self.torque = 0
        self.rps = 0
        self.piston_speed = 0
        self.power = 0

        self.VE_const = 0
        self.VE_inj = 0
        self.inj = 0

        self.af_needed = 0
        self.af_real = 0
        self.ff_real = 0
        self.max_temp = 0
        self.knock_risk = 0

        # travel
        self.fuel_cons = 0
        self.lpkm = 0
        self.speed = 0
        self.gearing = 0.7
        self.diff = 2.3
        self.wheel_diameter = 0
        self.tire_code = [285,40,19]


    def calc_setup(self):
        self.displacement = math.pi/4*((self.bore*0.1)**2)*self.stroke*0.1*self.cylinders*1e-6
        self.over_tdc_vol = (self.top_cavity+self.piston_cavity+((self.bore*0.05)**2)*math.pi*(self.headgasket/10))*1e-6
        self.compression = ((self.displacement/self.cylinders)+self.over_tdc_vol)/self.over_tdc_vol
        self.intake_air_pressure = (101325*(1-(2.25577*1e-5)*self.mos)**5.25588)+(self.max_boost*1e5)
        self.bore_area = (self.bore*1e-3*0.5)**2 * math.pi
        self.air_density = self.intake_air_pressure/(286.9*(273.15+self.air_temp))
        self.max_temp = (self.compression*self.intake_air_pressure*self.air_temp)/self.intake_air_pressure
        self.knock_risk = self.max_temp/self.auto_ign_temp
        self.wheel_diameter = (self.tire_code[0]*(self.tire_code[1]*0.01))*2+(self.tire_code[2]*25.4)

    def calc_iterate(self):
        self.rps = self.rpm/60
        self.af_needed = self.displacement*self.air_density*self.rps
        self.ff_real = (self.fuel_density*(self.injector/60)*1e-6)*(self.throttle/100)*self.cylinders*0.5
        self.af_real = self.af*self.ff_real
        self.VE_inj = self.af_real/self.af_needed

        self.imep = self.intake_air_pressure * self.compression * self.VE_inj
        self.F_tdc = self.imep * self.bore_area
        self.F_bdc = self.intake_air_pressure * self.bore_area
        self.delta_f = (self.F_tdc-self.F_bdc)/2
        self.torque = self.stroke*self.delta_f*1e-3
        self.piston_speed = 2*self.stroke*self.rps*1e-3
        self.power = (self.torque*self.rps*2*math.pi)*1e-3
        self.fuel_cons = self.ff_real*self.fuel_density*1e-3*3600

    def calc_speed(self):
        self.speed = (self.wheel_diameter*1e-3*math.pi)*((self.rps/self.gearing)/self.diff)
        self.lpkm = (self.fuel_cons/self.speed)*100
