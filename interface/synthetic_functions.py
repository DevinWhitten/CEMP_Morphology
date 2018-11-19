#### Here are the functions for the synthetic minimization
#### Author: Devin Whitten

import numpy as np
import scipy.interpolate as interp
import pandas as pd
from scipy.interpolate import interp1d


def determine_rChi(spec, synth, bounds, caHK_CH):
    ### Just accept dataframes
    ### linearly interpolate the synthetic spectra


    #### Build the synthetic function
    synth_function = interp1d(synth['wave'], synth['norm'], kind='cubic')

    spec_trim = spec[spec['wave'].between(bounds[0], bounds[1], inclusive=True)]

    #residual = spec_trim['norm'] - synth_function(spec_trim['wave'])

    CHI = np.divide(np.square(spec_trim['norm'] - synth_function(spec_trim['wave'])), synth_function(spec_trim['wave']))
    trim = np.concatenate([CHI[spec_trim['wave'].between(3925, 3980, inclusive=True)], CHI[spec_trim['wave'].between(4222, 4322, inclusive=True)]])
    trim1 = CHI[spec_trim['wave'].between(3925, 3980, inclusive=True)]
    trim2 = CHI[spec_trim['wave'].between(4222, 4322, inclusive=True)]
    if caHK_CH:
        #FINAL = np.mean([np.mean(CHI[spec_trim['wave'].between(3925, 3980, inclusive=True)]),
        #        np.mean(CHI[spec_trim['wave'].between(4222, 4322, inclusive=True)])])
        #FINAL = trim1.sum()/len(trim1)
        FINAL = trim.sum()/len(trim)
        #FINAL = np.mean([trim1.sum()/len(trim1), trim2.sum()/len(trim2)])
        #FINAL = np.median(np.concatenate([CHI[spec_trim['wave'].between(3925, 3980, inclusive=True)], CHI[spec_trim['wave'].between(4222, 4322, inclusive=True)]]))
        #FINAL = np.mean(CHI[spec_trim['wave'].between(3925, 3980, inclusive=True)])
        #FINAL = np.median(CHI[spec_trim['wave'].between(4222, 4322, inclusive=True)])

        #print(CHI)
        return FINAL



    else:
        #print(np.mean(CHI))
        return np.mean(CHI)


def determine_rChi_2(spec, synth, bounds, type='both'):
    ### Just accept dataframes
    ### linearly interpolate the synthetic spectra


    #### Build the synthetic function
    synth_function = interp1d(synth['wave'], synth['norm'], kind='cubic')

    spec_trim = spec[spec['wave'].between(bounds[0], bounds[1], inclusive=True)]

    #residual = spec_trim['norm'] - synth_function(spec_trim['wave'])

    CHI = np.divide(np.square(spec_trim['norm'] - synth_function(spec_trim['wave'])), synth_function(spec_trim['wave']))
    trim = np.concatenate([CHI[spec_trim['wave'].between(3925, 3980, inclusive=True)], CHI[spec_trim['wave'].between(4222, 4322, inclusive=True)]])
    trim1 = CHI[spec_trim['wave'].between(3925, 3980, inclusive=True)]
    trim2 = CHI[spec_trim['wave'].between(4222, 4322, inclusive=True)]
    if type=="CAII":
        #FINAL = np.mean([np.mean(CHI[spec_trim['wave'].between(3925, 3980, inclusive=True)]),
        #        np.mean(CHI[spec_trim['wave'].between(4222, 4322, inclusive=True)])])
        FINAL = trim1.sum()/len(trim1)
        #FINAL = trim2.sum()/len(trim2)
        #FINAL = np.mean([trim1.sum()/len(trim1), trim2.sum()/len(trim2)])
        #FINAL = np.median(np.concatenate([CHI[spec_trim['wave'].between(3925, 3980, inclusive=True)], CHI[spec_trim['wave'].between(4222, 4322, inclusive=True)]]))
        #FINAL = np.mean(CHI[spec_trim['wave'].between(3925, 3980, inclusive=True)])
        #FINAL = np.median(CHI[spec_trim['wave'].between(4222, 4322, inclusive=True)])

        #print(CHI)
        return FINAL

    elif type=="both":
        FINAL = trim.sum()/len(trim)
        return FINAL

    elif type=="median":
        FINAL = np.median(trim[np.isfinite(trim)])
        return FINAL

    elif type=="mean":
        FINAL = np.mean(trim[np.isfinite(trim)])
        return FINAL

    elif type=="weight":
        FINAL = np.mean([trim1.sum()/len(trim1), trim2.sum()/len(trim2)])
        return FINAL


    elif type=="CH":


        FINAL = trim2.sum()/len(trim2)
        return FINAL

def compute_synthetic_array(spectrum, synth_array, filenames, bounds, caHK_CH=False):
    ### Store the statistics in a dictionary or something
    temperatures = [float(name.split("T")[1].split("g")[0]) for name in filenames]

    feh = []
    for afile in filenames:
        feh.append(float(afile.split("z")[1].split("c")[0]))


    return pd.DataFrame({"temp": temperatures,
                         "chi2": [determine_rChi_2(spectrum, synth, bounds, caHK_CH) for synth in synth_array],
                         "name":filenames,
                         "feh":feh}).sort_values(by='feh')
