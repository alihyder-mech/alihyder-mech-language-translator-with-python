# Language translator using Python and Google translate API
This is a simple speech translator implemented in python using google translate api
compatible with ```Python 3.9.7``` and ```pip 21.3.1```
To run on a windows machine, delete the virtual environment i.e ```venv``` folder and create virtual environment on windows
with ```virutalenv```
do  
```bash
pip install virtualenv
```
To install the ```virtualenv```, after this navigate inside the cloned repo and do
```bash
virtualenv venv
```
Now to navigate into virtual environment, run the bat file in this format inside powershell or cmd prompt
```bash
C:\Users\'Username'\venv\Scripts\activate.bat
```
To install all dependicies do
```bash
pip install -r requirements.txt
```
On linux, if  Virtual environment is installed on your pc
Navigate into virtual environment with
```bash
source venv/bin/activate
```

run the app with
```bash
python app.py
```
Set appropitate ```device_index``` in ```app.py``` to select system default microphone if not selected automatically.
To find the ```device_index```, print available microphone indices with 
```python 
print(spr.Microphone.list_microphone_names())
```
Note the ```device_index``` of ```sysdefault``` and assign the value in ```device_index``` of ```spr.Microphone``` object
