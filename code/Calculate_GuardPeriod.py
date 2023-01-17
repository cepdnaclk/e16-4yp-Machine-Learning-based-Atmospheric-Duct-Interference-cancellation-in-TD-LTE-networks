# Python 3 program to calculate Distance Between Two Points on Earth
# https://www.geeksforgeeks.org/program-distance-two-points-earth/
from math import radians, cos, sin, asin, sqrt
from Calculate_distance import distance 
from whether_forecasting import getWheather

def guard_period(lat_base, lat_remote, lon_base, lon_remote):
    d = distance(lat_base, lat_remote, lon_base, lon_remote)
    whether = getWheather(lat_base,lon_base)['main']
    #print(whether)
    #Virtual temperature (Tv) = T + (0.0065 * h) + (0.00608 * T * R/P) + (0.00122 * T * R/P)^2
    T = whether['temp'] # In celcius ****
    h = 10.62
    R = whether['humidity']
    P = whether['pressure']
    Tv = (T + (0.0065 * h) + (0.00608 * T * R/P) + (0.00122 * T * R/P)*(0.00122 * T * R/P))

    # Refractive index n(f) = (77.6890 + (103.3 / (f^2)) * Tv) * 10^-8
    f = 2330 #average frequency
    n = (77.6890 + (103.3 / (f*f)) * Tv) / 100000000

    #d_direct = d / n
    d_direct = d / n

    #d_reflect = 2 * h_r * h_e / (d_direct^2)
    h_r = 247
    h_e = 247
    d_reflect = 2 * h_r * h_e / (d_direct*d_direct)

    d_eff = d_direct + d_reflect

    #T = (d_eff * n(f)) / c + (2 * h_e * h_r) / (c * (d_eff ^2))
    c = 299792458 # speed of light
    T = (d_eff * n) / c + (2 * h_e * h_r) / (c * (d_eff*d_eff))

    return T

     
# driver code
lat1 = 53.32055555555556
lat2 = 53.31861111111111
lon1 = -1.7297222222222221
lon2 =  -1.6997222222222223

lat = "6.931824"
lon = "81.470538"

T = guard_period(lat1, lat2, lon1, lon2)
print("Guard Period is ",T)




