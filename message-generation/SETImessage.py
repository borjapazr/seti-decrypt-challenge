# 2016 SETIDecrypt Challenge
# by Rene' Heller, heller@mps.mpg.de, Max Planck Institute for Solar System Research, Goettingen, Germany
# created 2016-04-13, last modification 2017-06-02

from pylab import *

#pi       = 3.141592653589793
c        = 299792458.                                      # [m / s], speed of light
G        = 6.673 * 10**(-11.)                              # [m^3 / kg / s^2], Newton's Gravitational constant
h        = 6.626068 * 10.**(-34.)                          # [m^2 * kg / s], Planck constant
yr       = 365.2425 * 24.*60*60                            # [s], yr in seconds (Greogorian calendar)
a_moo    = 384399000.                                      # [m], orbital distance of the Moon around the Earth
Gyr      = 10.**9 * yr                                     # [s], Myr in seconds

wl = 0.2110611405413 * pi                                  # [m], wavelength of hydrogen line divided by pi
nu = c/wl

length = sqrt(G*h/c**3)                                    # [m], Planck length (just without the 2pi scaling for hbar), about 4.05e-35 m
speed = c
time = length/speed

prime_list = []
primes_file = open("input/first_10000_prime_numbers.txt", "r")
primes_lines = primes_file.readlines()
for p in range(757):                                       # read the first 757 prime numbers
    prime_tmp = int(primes_lines[p].split("\n")[0])
    prime_list.append(prime_tmp)
primes = array(prime_list)


# convert PBM image of alien into one long 1-bit string and save in new TXT file
f = open("input/Grey-Alien_359x757.pbm", "r")
l = f.readlines()
f_new = open("output/Grey-Alien_359x757.txt", "w")
for i in range(len(l)):
    l_new = l[i].split("\n")[0]
    f_new.write(l_new)
f.close()
f_new.close()


# convert PBM image of sine wave into one long 1-bit string and save in new TXT file
f = open("input/sine.pbm", "r")
l = f.readlines()
f_new = open("output/sine_359x757.txt", "w")
for i in range(len(l)):
    if i > 2:
        l_new = l[i].split("\n")[0]
        f_new.write(l_new)
f.close()
f_new.close()


# convert PBM image of sine wave into one long 1-bit string and save in new TXT file
f = open("input/Kepler-22b_exomoon.pbm", "r")
l = f.readlines()
f_new = open("output/Kepler-22b_exomoon_359x757.txt", "w")
for i in range(len(l)):
    if i > 2:
        l_new = l[i].split("\n")[0]
        f_new.write(l_new)
f.close()
f_new.close()


# convert PBM image of SKA into one long 1-bit string and save in new TXT file
f = open("input/SKA.pbm", "r")
l = f.readlines()
f_new = open("output/SKA_359x757.txt", "w")
for i in range(len(l)):
    if i > 2:
        l_new = l[i].split("\n")[0]
        f_new.write(l_new)
f.close()
f_new.close()


#### 1st page, define page size
file = open("output/SETImessage.txt", "w")
file.write("%s" % ("1"*359))
for i in range(756):
    file.write("%s" % ("0"*358))
    file.write("1")

#### 2nd page, all numbers from 0 to 757
for i in arange(0,757,1):
    B = bin(i).split("b")[1][::-1]
    Z = 359 - len(B)                                       # number of zeros added to complete the line
    file.write("%s" % ( B ))
    file.write("0"*Z)

#### 3rd page, first 757 prime numbers
for i in arange(0,757,1):
    P = bin(primes[i]).split("b")[1][::-1]
    #    print P
    Z = 359 - len(P)                                       # number of zeros added to complete the line
    file.write("%s" % ( P ))
    file.write("0"*Z)

#### 4th page, image of a sine wave and definition of image scale in units of Planck length
sine = open("output/sine_359x757.txt", "r")
sine_l = sine.readline()
# write spatial dimension (wavelength) of the sine wave in units of the Planck length
L = bin(  int(wl / length)  ).split("b")[1][::-1]          # this binary string is 113 characters long
Z = 359 - len(L)                                           # number of zeros added to complete the line
file.write(L)
file.write("0"*Z)
# write temporal dimension (travel time = 50 years) of the sine wave in units of the Planck time
T = bin(  int(50*yr/time)  ).split("b")[1][::-1]           # this binary string is 173 characters long
Z = 359 - len(T)                                           # number of zeros added to complete the line
file.write(T)
file.write("0"*Z)
file.write(sine_l[(2*359):])                               # complete this page with the rest from the sine wave file

#### 5th page
alien = open("output/Grey-Alien_359x757.txt", "r")
ali_l = alien.readline()
# write spatial dimension (body height) of the alien body in units of the Planck length
H = bin(  int(2.45/length)  ).split("b")[1][::-1]          # this binary string is 116 characters long
Z1 = 359 - len(H)                                          # number of zeros added to complete the line
file.write(H)
file.write("0"*Z1)
# write temporal dimension (life span = 180 years) of the aliens in units of the Planck time
T = bin(  int(180*yr/time)  ).split("b")[1][::-1]          # this binary string is 175 characters long
Z2 = 359 - len(T)                                          # number of zeros added to complete the line
file.write(T)
file.write("0"*Z2)
file.write(ali_l[(2*359):])                                # complete this page with the rest from the alien image file

#### 6th page
SKA = open("output/SKA_359x757.txt", "r")
SKA_l = SKA.readline()
# write spatial dimension (SKA scale, say 100km) in units of the Planck length
S = bin(  int(100000./length)  ).split("b")[1][::-1]       # this binary string is *?* characters long
Z = 359 - len(S)                                           # number of zeros added to complete the line
file.write(S)
file.write("0"*Z)
# write temporal dimension (time since they've started radio broadcasts, say 10,000 years)
T = bin(  int(10000*yr/time)  ).split("b")[1][::-1]        # this binary string is *?* characters long
Z = 359 - len(T)                                           # number of zeros added to complete the line
file.write(T)
file.write("0"*Z)
file.write(SKA_l[(2*359):])                                # complete this page with the rest from the SKA image file

#### 7th page
PLA = open("output/Kepler-22b_exomoon_359x757.txt", "r")
PLA_l = PLA.readline()
# write spatial dimension (planet-moon scale, say 100 a_moo) in units of the Planck length
S = bin(  int(100*a_moo/length)  ).split("b")[1][::-1]     # this binary string is *?* characters long
Z = 359 - len(S)                                           # number of zeros added to complete the line
file.write(S)
file.write("0"*Z)
# write temporal dimension (time since the system formed, say 6 Gyr)
T = bin(  int(6*Gyr/time)  ).split("b")[1][::-1]           # this binary string is *?* characters long
Z = 359 - len(T)                                           # number of zeros added to complete the line
file.write(T)
file.write("0"*Z)
file.write(PLA_l[(2*359):])                                # complete this page with the rest from the SKA image file


file.close()


#### copy TXT file to pixel map PBM file
TXT = open("output/SETImessage.txt", "r")
TXT_lines = TXT.readlines()
n = 7                                                      # number of pages
PBM = open("output/SETImessage.pbm", "w")
PBM.write("P1 359 %i\n" % (n*757))
PBM.write(TXT_lines[0])
TXT.close()
PBM.close()

