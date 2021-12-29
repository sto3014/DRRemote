# DRRemote

DRRemote is a python modul which offers access to Davinci Resolve Studio.
At the time the functionality is very basic. DRRemote is used in conjunction with [LRDavinci](https://github.com/sto3014/LRDavinci).
LRDavinci is a Lightroom plug-in for Davinci Resolve Studio

## Features
* Changes the current timeline
* Retrieves the attributes for the current timeline 
  * name, type and ipaddress of database
  * name of project
  * name of timeline

## Requirements
* Python 3.6 (not more, not less due to Davinci Resolve restrictions)  
* Davinci Resolve Studio (license is needed for Davinci Resolve's Python API).

## Installation
1. [Python](https://www.python.org/downloads/)  
    You need to install version 3.6.x.
2. PIP 
   * Windows
        * python -m pip install --upgrade pip
   * macOS
        * curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py  
        * python get-pip.py
3. DRRemote
   * pip install drremote

## Usage
You must execute __DRRemote__ in a Command Prompt (Windows) or Terminal (MacOS).
For instance:
* Start Davinci Resolve Studio, open a project and select a timeline
* Open a Command Prompt/Terminal and type:
```
drremote -m gettimeline -o out.txt
```
If successful you find the gathered information in file out.txt in your current directory:
```
Success
project=Snippets
timeline=2021-12-10-First Snow
database=2021:Disk
```
If you get an error, you may find some more information in the log logfile:
* MacOS  
  * $TMPDIR/drremote.log
* Windows  
  * %USERTEMP%/drremote.log


For the commandline arguments see ```ddremote --help```

###Examples  
#### Set the current timeline in Davinci resolve   
```
drremote -m settimeline -t "2021-12-10-First Snow" -p Snippets -d 2021:disk -o /tmp/out.txt
```  

#### Get the current timeline IDs  
```
drremote -m gettimeline -o /tmp/out.txt
```
The result is written into __/tmp/out.txt__:
```
Success
project=Snippets
timeline=2021-12-10-First Snow
database=2021:Disk
```
