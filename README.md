# Geosoftware II - WiSe 2018/19 - :arrow_forward: Die Gruppe :one: 
## Enhancing discovery of geospatial datasets in data repositories

## Project Goal
This project closes the gap between geospatial data formats and repositories and similarity measurements.
Or group extended an existing Free and Open Source Software (FOSS) - Zenodo - with the functionality to retrieve and view similar records. This comprises both the API and UI, namely providing an HTTP endpoint to retrieve an
ordered list of records based on a provided record and displaying similar records.     
   
For all installationsteps we presuppose [pip](https://pip.pypa.io/en/stable/installing/) and [python](https://www.python.org/) :exclamation:
  
# Zenodo - Installation:      
Here you can find our Zenodo-Repository:   
*https://github.com/corneliazy/zenodo*   

For Zenodo installation, please follow the instructions below:    
*https://github.com/corneliazy/zenodo/blob/master/INSTALL.rst*   
(Who wants to save time, should not try it under Windows. On Linux its much faster and easier :wink: )
 
After installation execute:
```bat 
pip install -e .
```
Now you can open `http://localhost:5000/`. There you can create your own profile and upload files.

If you have installed our version of zenodo you can find the integrated extractTool in your virtual enviroment in */Envs/zenodo/lib/python2.7/site-packages/extractTool* 


# CLI-Tool   
This installation was previously tested only with Linux, but should also work under Windows.  

## Installation Description (PyPi)  
https://pypi.org/project/extractTool/  
```bat 
pip install extractTool
```  
   
(you can write this command in your console and follow the installation description on the webside OR    you can download the file and install the CLI tool local: )   
## Installation Description (local)
 
pip for pip install is required.   

**After downloading our Tool from PyPi** 
To run our CLI tool, the following file must be executed in the project folder:   
     
```bat 
pip install -r requirements.txt --user (or sudo pip install -r requirements.txt) 
```
   
In this file all required plugins are listed, which we use in our tool.      

In addition, the following commands must be executed (if necessary with sudo):   
```bat 
apt-get install python-gdal    
apt-get install gdal-bin 
```
```bat 
pip install pytest   
```      
Then you can navigate in any common console in the folder of the tool (*"extractTool"*) and
there, the following command must be executed   

```bat 
python extractTool.py --path='[filepath]' --detail=[bbox|concexHull] --folder=[single|whole] --time
```
 for `filepath` you must insert a filepath to your testdata
 
`--bbox` &larr; for the bounding box of the file/folder   
`--convexHull` &larr; to get all the covexHull of the file/folder   
`--single` &larr; to extract the bbox/covexHull of a single file   
`--whole` &larr; to extract the bbox/convexHull of a whole dictionary   
`--time` &larr; (optionally) You can add this parameter to get additionally the timeextend   

### some examples
```bat
python extractTool.py --path='/home/maxmusterman/test1.geojson' --detail=bbox --folder=single --time   
python extractTool.py --path='/home/maxmusterman/test2.nc' --detail=convexHull --folder=single 
python extractTool.py --path='/home/maxmusterman/testdict' --detail=bbox --folder=whole --time
```
# similarity calculation

Our similarity calculation code can be found in the `similar.py`file.   
The associated tests are in the `test_similar.py` file.

# Tests

Our tests can be executed with the command 
```bat 
pytest
```

# Problems?
If problems or questions arise during installation, create an issue directly so we can help you and correct mistakes :blush:
