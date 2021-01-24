import matplotlib.pyplot as plt
from model import Engine

# load boost map, x=throtle, y=rpm, z=boost
e = Engine()
e.calc_setup()
x = []
y = []
for rpm in range(100, 8000, 100):
    e.rpm = rpm
    e.throttle = (rpm/8000)*100
    e.calc_iterate()
    e.calc_speed()
    print(rpm, e.power, e.throttle)
    x.append(rpm)
    y.append(e.power)
plt.plot(x,y)
plt.xlabel("RPM")
plt.ylabel("kW")
plt.show()
