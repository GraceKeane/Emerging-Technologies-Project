## Emerging Technologies project 2020
### Wind turbine power output
### Grace Keane - G00359990

### Repository contents
<b>Img - </b> contains images of a linear and sigmoid model to be used in Model.ipynb<br>
<b>static -</b> holds index.html which contains all the design for the web-service.py.<br>
<b>.dockerignore - </b> specifies files and folders that should be ignored by the Docker client when generating a build context.<br>
<b>0ValuesDeleted.csv - </b> data set that has all 0 values removed.<br>
<b>Dockerfile - </b> Dockerfile contains all the commands a user could call on the command line to assemble an image.<br>
<b>Model.ipynb -  </b> Holds 3 models (linear, sigmoid and 0 values deleted sigmoid) to demonstrate power predictions based on the data set powerproduction.csv.<br>
<b>README.md - </b>Specifies whats contained in the repo, how to run web-service, how to run the model and what to expect once all are ran. <br>
<b>powerproduction.csv -</b> contains all original speed and power values.<br> 
<b>savedValues.h5 - </b> h5 file containing data to be used in web-service.py. <br>
<b>web-service.py - </b> holds savedValues.h5 and python code to run the web service.  <br>

### Run model
1) Clone repo
2) Copy URL
3) Create blank folder
4) Type "git clone (URL here)"
5) Type "jupyter notebook" into cmder
6) Click into Model.ipynb and "Restart and run all" - model should run all cells after a few minutes
7) Press control c in cmder to shut down jupyter notebook when finished

### What to expect once the model is ran
Once "Restart and run all" is pressed the program should then run all cells and output the result of each code cell. For this model I focused on analysing the data using graphs first, then getting loss values and printing out power predictions using linear, sigmoid and sigmoid 0 value models.

### Run web-service
1) cd into project directory
2) Type "set FLASK_APP=web-service.py"
3) Type "python -m flask run"
4) Web app will then be accessable on chrome once http://127.0.0.1:5000/ is pasted into search engine

### What to expect once web-service is ran
Once http://127.0.0.1:5000/ is pasted into the search bar my web service should appear almost immediately. It asks the used to input a speed value and press submit. Once the submit button in pressed the program sends a GET request to analyse the model and the contents of savedValues.h5. Then a POST request is sent back to the web-service with the correct power output in watts.

### Run web service commands

```bash
$ set FLASK_APP=web-service.py
$ python -m flask run
 * Running on http://127.0.0.1:5000/
 ```
 
 ### Software requirements
 - Anaconda
 - Python 3.8
 - Keras
 - Docker
 - WSL2
 
 ### Model requirements
- numpy==1.19.2
- tensorflow==2.3.0
- Flask==1.1.2
- matplotlib==3.3.2
- pandas==1.1.5
- seaborn==0.11.1
