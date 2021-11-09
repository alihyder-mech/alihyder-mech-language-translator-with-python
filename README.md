# Language translator using Python and Google translate API
This is a simple speech translator implemented in python using google translate api
compatible with ```Python 3.9.7``` and ```pip 21.3.1```
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
