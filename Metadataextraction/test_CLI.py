import click, shapefile, json, sqlite3, csv, pygeoj
from osgeo import gdal
import pandas as pd
import numpy as np
import xarray as xr
import os

import extractTool
import getShapefileInfo, getGeoTiffInfo, getCSVInfo, getGeoJsonInfo, getNetCDFInfo, getGeoPackageInfo, getIsoInfo, openFolder

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

#--detail=bboxSingle
def test_bboxSingleShapefile():

def test_bboxSingleGeoJson():

def test_bboxSingleNetCDF():

def test_bboxSingleCSV():

def test_Geopackage