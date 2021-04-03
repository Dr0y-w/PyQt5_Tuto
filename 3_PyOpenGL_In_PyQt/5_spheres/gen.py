from math import sqrt,cos, sin, pi, fabs


def cercle(rayon, precision, centre):
    precision = precision*pi/180
    lx = [centre[0]+rayon*cos(i*precision) for i in range(int(360/precision))]
    ly = [centre[1]+rayon*sin(i*precision) for i in range(int(360/precision))]
    lz = [centre[2] for i in range(len(lx))]
    return lx, ly, lz


def sphere(rayon, precision,centre):
    lx, ly, lz = cercle(rayon, precision, centre)
    precision_rad = precision*pi/180
    for i in range(int((pi/2)/(precision_rad))):
        nv_centre = (centre[0], centre[1], centre[2] + rayon*sin(precision_rad*i))
        nv_rayon = rayon*cos(precision_rad*i)
        lx_1, ly_1, lz_1 = cercle(nv_rayon, precision, nv_centre)
        lx += lx_1
        ly += ly_1
        lz += lz_1
    lx += lx
    ly += ly
    for i in range(len(lz)) :
        lz.append(-lz[i])

    return lx, ly, lz


def gen_sphere(centre, radius, precision):
    lx = [x for x in range(-radius, radius+1)]
    ly = [sqrt((radius**2) - (lx[i]**2)) for i in range(int((len(lx)+1)/2))]
    for i in range(len(ly)-2, -1, -1):
        ly.append(ly[i])
    lx2 = [x for x in range(-radius+1, radius)]
    lx += lx2
    ly2 = [-e for e in ly[1:-2]]
    ly += ly2
    return lx, ly


