# -*- coding: cp1252 -*-

#
# Copyright (c) 2014-2019 R.Pissardini <rodrigo AT pissardini DOT com>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
#The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.



####General functions

#convert day-int to day-str with 3 char

def day_of_year_int2string(day):

    """Convert from day of year in int format to string format with three chars.

        Keyword arguments:

        day  -- day in int format

        Output:
        
        day  -- day in char format
    """


    if day <10:
        day = "00"+ str(day)
    elif day <100:
        day = "0"+ str(day)
    else:
        day = str(day)
    return day

def fixed_int2string(number,size):
    if len(str(number))<size:
        diff = size - len(str(number))
        str_number=""
        for i in range(0,diff):
            str_number +="0"
        return str_number+ str(number)
    elif len(str(number))== size:
        return str(number)
    else:
        print("Error: Size must be lower than the number of digits in the number")
        return False

#Download zip file from stations

import urllib.request, urllib.error
import shutil
import os

def download_zipfile_station(url="http://geoftp.ibge.gov.br/informacoes_sobre_posicionamento_geodesico/rbmc/dados/",
                             year = 2019,
                             day_year = 1,
                             station  = "poli",
                             target=""):
    
    """Download a zipfile from a station for processing.

    Keyword arguments:

    url  -- url of zipfile (default: IBGE)
    year -- year of zipfile
    station -- abbreviation of station (4 chars)(default: poli)
    target  -- directory of downloaded file.

    """
    try:
        
        url = url + str(year)+ "/"+ day_of_year_int2string(day_year) + "/" + station + day_of_year_int2string(day_year)+"1.zip"
        
        print("Downloading: " + url)
        with urllib.request.urlopen(url) as response, open(target + os.path.basename(url), 'wb') as out_file:
            shutil.copyfileobj(response, out_file)
        print("Completed. Target : " + target + os.path.basename(url))

    except urllib.error.HTTPError as e:
        print ("HTTP Error:", e.code, url)
    except urllib.error.URLError as e:
        print ("URL Error:", e.reason, url)

from datetime import date,timedelta
from .ptr_lib.general.datetime import *

def download_zipfile_station_range(day_start   =1,
                                   month_start =1,
                                   year_start  =2019,
                                   day_end     =3,
                                   month_end   =1,
                                   year_end    = 2019,
                                   url         ="http://geoftp.ibge.gov.br/informacoes_sobre_posicionamento_geodesico/rbmc/dados/",
                                   station     = "poli",
                                   target      =""):

    """Download zipfiles from a station in a range of two dates.

    Keyword arguments:

    day_start -- day of first date
    month_start -- month of first date
    year_start -- year of first date
    day_end -- day of second date
    month_end -- month of second date
    year_end -- year of second date
    url  -- url of zipfile (default: IBGE)
    year -- year of zipfile
    station -- abbreviation of station (4 chars) (default: poli)
    target  -- directory of downloaded files.

    """
    
    d0 = date(year_start, month_start, day_start)
    d1 = date(year_end, month_end, day_end)

    if d0<=d1:
        year_control = year_start
        while d0<d1:
            if d0 == 1:
                year_control +=1
            try:
                print("Ok")
                download_zipfile_station(url=url,
                                 year = year_control,
                                 day_year = day_of_year(d0.year,d0.month,d0.day),
                                 station  = station,
                                 target= target)
            except:
                print("Could not download file from day "+ str(d0)+" from station "+ station)
            d0 += timedelta(days=1)

    else:
        print("The first date is greater than the second date.")


#downloading observations files

def get_observations_files(week,
                    day,
                    products = 'F',
                    target = '',
                    url ='ftp://gssc.esa.int/gnss/products/'):

    """Download observations files from IGS 

    Keyword arguments:

    week  -- GPS Week
    day   -- day of week (0-6)
    products   -- type of products (F- final) 
    target -- directory of downloaded files
    url -- url of observations files
    """
    
    try:
        url += fixed_int2string(week,4)+"/"

        if obs in ['F','f']:
            print(url)
            url = url +'igs'+ fixed_int2string(week,4)+ str(day)
            clock = url + '.clk.Z'
            sp3 = url + '.sp3.Z'

        print("Downloading: " + clock)
        
        with urllib.request.urlopen(clock) as response, open(target + os.path.basename(clock), 'wb') as out_file:
            shutil.copyfileobj(response, out_file)
        print("Completed. Target : " + target + os.path.basename(clock))

        print("Downloading: " + sp3)
        
        with urllib.request.urlopen(sp3) as response, open(target + os.path.basename(sp3), 'wb') as out_file:
            shutil.copyfileobj(response, out_file)
        print("Completed. Target : " + target + os.path.basename(sp3))


    except urllib.error.HTTPError as e:

        print ("HTTP Error:", e.code, url)

    except urllib.error.URLError as e:

        print ("URL Error:", e.reason, url)
        
    
#extracting files from zip file 

import zipfile
import glob


def extracting_zipfile(origin,target): 

    """Extract content of zipfile 

    Keyword arguments:

    origin  -- original path  of zip(s) file(s)
    target  -- target path of uncompressed file 

    """

    for zfile in glob.glob(origin + "/*.zip"):
        try:
            with zipfile.ZipFile(zfile,"r") as zip_ref:
                nfile = target + os.path.basename(zfile)
                nfile = nfile.replace(".zip","/")
                zip_ref.extractall(nfile)
                
            print ( "Extraction Completed. File  " + zfile + " [OK]")
        except:
            print ( "Error in file: " + zfile)
            pass

#### Conversion files


import subprocess

def hatakana2rinex(rnxcmp,  #path of rnxcmp program 
                   file_d): #path of .d file
        
    """Convert from Hatakana to Rinex - RNXCMP is required - http://terras.gsi.go.jp/ja/crx2rnx.html 

    Keyword arguments:

    rnxcmp  -- path of rnxcmp executable 
    file_d  -- path of .d file for conversion 

    """
    
    cmd = rnxcmp+ " "+ file_d
    subprocess.call(cmd, shell=True)


### Analysis and processing RINEX


from subprocess import check_output


def rinex_metadata(teqc,file_o):
    
    """Get Rinex Metadata
        Teqc is required for processing - https://www.unavco.org/software/data-processing/teqc/teqc.html

        Keyword arguments:

        teqc    -- path of teqc executable 
        file_d  -- path of .d file for conversion

        Output:
        out     -- metadata with \r\n 
    """
    
    out = check_output([teqc,"+meta",file_o])
    return out


def rinex_summary(teqc,file_o): 

    """Get Rinex Summary
        Teqc is required for processing - https://www.unavco.org/software/data-processing/teqc/teqc.html

        Keyword arguments:

        teqc    -- path of teqc executable 
        file_o  -- path of .o file

        Output:
        out     -- summary with \r\n 
    """

    
    out = check_output([teqc,"-O.sum",".",file_o])
    return out

# Get quality from rinex files

def rinex_quality(teqc,file_o):  # tecq - path of TEQC   file_o - observable file 
    out = check_output([teqc,"+qc",file_o])
    return out

#Exclude constellations

import subprocess

def rinex_exclude_constellations(teqc,
                                 file_o,
                                 target,
                                 gps     = True,
                                 glonass = True,
                                 sbas    = True,
                                 galileo = True,
                                 beidou  = True,
                                 qzss    = True
                                 ):
    constellations =""
    if gps is False:
        constellations = constellations + "-G "
    if glonass is False:
        constellations = constellations + "-R "
    if sbas is False:
        constellations = constellations + "-S "
    if galileo is False:
        constellations = constellations + "-E "
    if beidou is False:
        constellations = constellations + "-C "
    if qzss is False:
        constellations = constellations + "-J "

    try:
        cmd = teqc + " " +constellations[:-1] +" "+ file_o + " > " + target + os.path.basename(file_o)+".PROCESSED"
        subprocess.call(cmd, shell=True)
        print("Conversion RINEX terminated : " + target + os.path.basename(file_o)+".PROCESSED")
    except:
        print("Error in RINEX.")
        
#Transform output of tecq in a human readable text

def rinex_human_readable(out):
    ls =[]
    ls = out.decode("utf-8").split("\r\n")
    for i in ls:
        print(i)

#Exclude satellites from file .o 

def rinex_exclude_satellites(teqc,
                             file_o,
                             target,
                             satellites): #input: list of satellites and number ['G01,G02,...]'

    print("Excluding: "+ str(satellites))
    sats ="-"
    for i in satellites:
        if i[0] in ['G','R','S','E','C','J']:
            sats = sats + i + ","
    print(sats)
    try:
        cmd = teqc + " " + sats[:-1] + " " + file_o + " > " + target + os.path.basename(file_o)+".PROCESSED"
        subprocess.call(cmd, shell=True)
        print("Conversion RINEX terminated : " + target + os.path.basename(file_o)+".PROCESSED")
    except:
        print("Error in RINEX.")

# Set mask of elevation from file .o

def rinex_mask( teqc,
                file_o,
                target,
                mask):
    if mask>=0.0 and mask<=90.0:
        try:
            cmd = teqc + "  -set_mask " + str(mask)  + " " + file_o + " > " + target + os.path.basename(file_o)+".PROCESSED"
            print(cmd)
            subprocess.call(cmd, shell=True)
            print("Conversion RINEX terminated : " + target + os.path.basename(file_o)+".PROCESSED")
        except:
            print("Error in RINEX.")

# Set mask of datetime limits from file .o

def rinex_datetime( teqc,
                    file_o,
                    target,
                    datetime_start = "2016_01_01:01:00:00",
                    datetime_end = "2016_01_01:23:59:59"):
    try:
        cmd = teqc + " -st " + str(datetime_start)  + " -e " + str(datetime_end)+ " " + file_o + " > " + target + os.path.basename(file_o)+".PROCESSED"
        print(cmd)
        subprocess.call(cmd, shell=True)
        print("Conversion RINEX terminated : " + target + os.path.basename(file_o)+".PROCESSED")
    except:
        print("Error in RINEX.")

# Set interval in seconds from file .o

def rinex_interval( teqc,
                    file_o,
                    target,
                    interval=1.0):
    if interval >= 1.0:
        try:
            cmd = teqc + " -O.dec " + str(interval)  + " " + file_o + " > " + target + os.path.basename(file_o)+".PROCESSED"
            print(cmd)
            subprocess.call(cmd, shell=True)
            print("Conversion RINEX terminated : " + target + os.path.basename(file_o)+".PROCESSED")
        except:
            print("Error in RINEX.")
    else:
        print("Use interval >=1.0")

