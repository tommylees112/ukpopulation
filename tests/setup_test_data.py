#!/usr/bin/env python3

""" 
create a small subset of real data for testing - 3 LADs per country and years up to 2027
test data is under source control - this script only required if the data format changes
NOTE: ensure NOMIS_API_KEY=DUMMY in order to match the cached filenames for England
"""
import pandas as pd

real_data_dir = "~/.ukpopulation/cache/"
test_data_dir = "./tests/raw_data/"

def setup_snpp_data():
  """
  SNPP test data is 3 LADs per country for years 2014-2027
  """
  raw_files = ["NM_2006_1_d9b41c77ffd9da86c7ff40ddedd64fe6.tsv", # England 
              "snpp_w.csv","snpp_s.csv","snpp_ni.csv"]

  for file in raw_files:
    sep = "\t" if file[-4:] == ".tsv" else ","
    df = pd.read_csv(real_data_dir + file, sep=sep)

    geogs = df.GEOGRAPHY_CODE.unique()[:3]
    df = df[(df.GEOGRAPHY_CODE.isin(geogs)) & (df.PROJECTED_YEAR_NAME < 2028)]

    df.to_csv(test_data_dir + file, sep=sep, index=False)

  # NB the file NM_2006_1_80dd181418e34b263810a07ede7655a6.tsv also needs to be in the test data folder,
  # containing column headings only. (This will prevent the data being re-downloaded)

def setup_npp_data():
  """
  NPP test data is 3 variants, all ages, for years 2016-2035
  """
  raw_files = ["NM_2009_1_0bcd330bc936cd7902566cf7198d8868.tsv", # ppp  
              "npp_hhh.csv","npp_lll.csv"]
  
  for file in raw_files:
    sep = "\t" if file[-4:] == ".tsv" else ","
    df = pd.read_csv(real_data_dir + file, sep=sep)
    df = df[(df.PROJECTED_YEAR_NAME < 2036)]
    df.to_csv(test_data_dir + file, sep=sep, index=False)


if __name__ == '__main__':
  setup_npp_data()
