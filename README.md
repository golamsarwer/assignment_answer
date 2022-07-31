# Anser of Assignment for a Software Engineer position July 2022
## Installations:
Install python
1. Dowload Python latest version
2. Open installation file
3. Click checkbox "ADD Python to PATH" at below of popup
4. Click Customize installation
5. Click all checkbox of Optional Feature and then click install
6. Click first five checkbox of advanced option
7. Install location should be as C:\Program Files\Python_vesion* and then click install. 
8. Now python successfully installed 

Install Pandas. It's a python library
1. Open Command Line
2. Type as: `py -m pip install pandas`
3. Pandas will be installed in machine

Install IDE:
1. Install Pycham/ Jupiter/ any other python supported IDE
2. To explore the code of program open `all.py` in IDE

## How to navigate to run program
Open cmd. Then navigate to program folder. Example- `C:\Users\Desktop\program\all.py` or open folder that contain program file and then run cmd here.



## How to run program
1. Type: `py all.py` in CMD
2. its will ask for 3 input to give. 
3. Enter arguments in CMD as given below:
   1. argument1 : `data_cases_1.csv`
   2. argument2: `disease_list.csv`
   3. argument3: `indicators_1.json`
4. Now press enter and program will run
5. If corrupted data inserted as argument1 like `data_cases_corrupted.csv`. then program will fix it by eliminating "ABB from program. and all column will be shifted to right column
6. Argument serial have to be follow to run program properly.
7. After program run, this program will analyse both csv file and find summery as requiremnt.
8. Its will generate two json file with summery from csv files.
9. As output specified in cmd, as like `indicators_1.json` json file will be generated with summery
10. Another json file `indicators_advanced_1.json` will be generated as well.


## Requiement of assignment:
There are five main tasks A-E. Even if you are not able to complete all the tasks, make sure your program is functioning and well documented. You can use any technology stack you prefer, however you need to provide clear instructions on how to deploy your program.

A. Your program reads in two input csv files, `data_cases_1.csv` with records of cases of animal diseases, and `disease_list.csv` that contains names of the diseases. Your first task is to extract some summary statistics from those files to produce the output in a valid json file. See provided example `indicators_1.json` ). Make sure your output matches the example, and your program works correctly on `data_cases_2.csv` as well. 
Answer: My program taking two input csv files and one output json files

B. Names of input and output files should be specified as command line arguments.
Answer: Name of input and output can specified as cmd command line arguments

C. Provide a README file explaining how to deploy and use the program
Answer: This file is readme file for guidence

D. Sometimes the input file is corrupted. Analyse the problem with the file and enhance your program so that it can correctly analyse `data_cases_corrupted.csv` (output as per `indicators_corrupted.json`)
Answer: Corrupted file can take as input and my program will fix it to find summery

E. Enhance your program to output more advanced indicators as in the `advanced_indicators_1.json` example file.
Answer: My program genartes this advanced indicators as advanced indicators1.json file
