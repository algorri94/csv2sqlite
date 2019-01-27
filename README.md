# CSV2SQLite
CSV2SQLite is a simple Python CLI application that reads the CSV file given as a parameter and saves it in a SQLite database.

## Install instructions
In order to install CSV2SQLite first you need to install Python3. Go to https://www.python.org/downloads/ and download the binary files or use your operative system's package manager in case you are in a UNIX environment.

Once installed, you just need to install the app. Go to the application's folder and execute the following command:

    python setup.py install
    
## How to use
Once the application is installed you can execute the application running the following command.

    csv2sqlite [-h] [--rows ROWS] [--delimiter DELIMITER] csvfile
    
Arguments:

&nbsp;&nbsp;&nbsp; csvfile &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  A CSV file to read from.

Optional arguments:

&nbsp;&nbsp;&nbsp; -h --help &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Show the help message and exit
  
&nbsp;&nbsp;&nbsp; --rows ROWS &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Number of rows to process per iteration in case the file does not fit in memory. Default none.
  
&nbsp;&nbsp;&nbsp; --delimiter DELIMITER &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Character that separates the different fields in the CSV. Default ','
