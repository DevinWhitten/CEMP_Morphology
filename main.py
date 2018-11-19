### Author: Devin Whitten
### Main driver for normalization routine, intended for SEGUE medium-resolution spectra.

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import sys, os
sys.path.append("interface")
from spectrum import Spectrum
from astropy.io import fits
import norm_functions

#plt.ion()
### Needs to work for a directory of spectra, later.
#files = os.listdir(os.getcwd() + "/Spectra/")


### Custom file input for HESCAR
#files = ['AAT_0254.fits', '6df_6495.fits', 'KPNO21_1375.fits', 'KPNO21_1456.fits', 'KPNO21_2100.fits']
#path = "obs/"
#arg0 = sys.argv[0]
#arg1 = sys.argv[1]
#print(arg1)
path = "synthetic/dwarf/GII/"
output_directory= "output/dwarf/GII/"
plot_directory = "plots/dwarf/GII/"


#z-3.0c+2.25
#path = "obs/"
#output_directory= "output/G77/"
#plot_directory = "plots/G77/"

files = os.listdir(path)
#files = [path + "T4000g5.00z-2.50c+2.00.dat", path + "T5500g5.00z-2.50c+2.00.dat"]
# 4000, 3924, 42703
# 4250, 3924.0, 85509
# 4500, 3924, 192944
# 4750, 3924, 345418
#files = ["CVn_blue_may1b2b_jun1b.fits"]
#files = ['g77-61_blue_sum.fits']


print("Files in directory:  ", files)

for filename in files:
    print("Current file:  ", filename)
    #filename = "spSpec-2371-53762-261.fit"
    #input_file = pd.read_csv(path + filename, header=None, sep="\s+")
    input_file = pd.read_csv(path + filename)
    #input_file = fits.open(path + filename)
    ### Create Spectrum object
    spec = Spectrum(input_file, filename, fits=False)

    ### generate segments
    #spec.generate_segments(15)
    spec.generate_inflection_segments(sigma=25, cahk=True)
    spec.assess_segment_variation()
    spec.define_cont_points()

    spec.set_segment_continuum()
    spec.set_segment_midpoints()


    spec.get_continuum_points()
    #spec.remove_point(8)
    #spec.remove_point([11,17])


    ####
    #spec.remove_point([19,20])

    #spec.add_continuum_point((4438.9, 706.02))
    #spec.add_continuum_point((4547.34, 648.371))
    #spec.add_continuum_point((4444.9, 314235))
    ###

    #spec.add_continuum_point((4444.9, 560.))
    #spec.add_continuum_point((4444, 217840))
    #spec.add_continuum_point((4556, 267644))

    #spec.remove_point([9])
    ####dwarf/z-4.00c+3.00/ -----------------------------------------------
    #spec.add_continuum_point((3917.57, 37732.5))
    #spec.add_continuum_point((3925, 40393.2))
    #spec.add_continuum_point((3956.9, 45304.4))
    #-----------------------------------------------
    ### G77 -----------------------------------------------
    #spec.remove_point([10, 11, 12, 13, 14, 15, 16, 17, 18, 20, 21])
    #spec.add_continuum_point((4444, 54950))
    #spec.add_continuum_point((3886, 4730))
    #spec.add_continuum_point((3925.2, 6648))
    #spec.add_continuum_point((3950.2, 7320))
    #spec.add_continuum_point((3957.5, 7856))
    #spec.add_continuum_point((3997.1, 9632.7))
    #spec.add_continuum_point((4089, 13125))
    ### G77 -----------------------------------------------
    #spec.add_continuum_point((3918, 1.41508e+06))
    #spec.set_wavelength(None)
    #spec.set_fluxpoints(None)

    print("Define the spline")
    k=1
    s=2
    print("\torder = ", k)
    print("\tSmoothing = ", s)
    spec.spline_continuum(k=k, s=s)

    print("Normalize")
    spec.normalize()

    norm_functions.plot(spec, plot_directory)

    print("Update fits")
    output_file = norm_functions.update_fits(spec, input_file)

    print("Writing")
    print(output_file.norm)
    output_file.to_csv(output_directory + filename.split(".dat")[0] + "norm_new.dat", index=False)
    #output_file.writeto("output/" + filename.split(".")[0] + "_pynorm.fits")

    print("Done")
