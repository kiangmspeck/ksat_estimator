# ksat_estimator
A python script that takes user-provided inputs to calculate saturated hydraulic conductivity of a soil sample (ksat).

How to Run: 
This script was written in Python 3, and therefore requires Python 3 be downloaded on your machine before running. Python can be downloaded at https://www.python.org/downloads/ .

This script can be run in any computer by navigating to the folder containing the script (must end in the '.py' extensions) and entering python3 <script_name.py>.

Navigating to the correct folder can by done by using the command 'cd <\Users\your\folder>'.

How to Use:
The script takes three (3) inputs to calculate saturated hydraulic conductivity of soil sample (ksat), namely; bulk density, 33 kPa, and rock fragments by volume. Bulk density values should be derived from oven-dried samples. 33 kPa is considered the suction tension of the soil at 'field capacity' (water content of soil after gravity drainage). If obtaining values from NASIS, 33 kPa is derived by taking .3 bar water content divided by 100 (.3 bar is equivalent to 33 kPa, and water content is represented as a percentage, hence dividing by 100). Rock fragments by volume are inputed as a percentage.

When the user first runs this script, the program will first ask how many samples you wish to calculate. The purpose of this is to ensure that the calculation takes the same amount of values for each required variable.

The program then prompts the user to enter bulk density. The user needs to enter the values for each sample seperated by a space, i.e. '1.6 1.5 1.7'. Future version of this app my allow other entry options, such as inputing an excel sheet. If any other input options are desired, feel free to send me an email with your request at kianspeck@gmail.com. 

The program will then prompt the user for 33 kPa and volume rock fragments in the same manner. If the user does not enter an amount of values that matches the number of samples provided at the beginning, the program will prompt the user again until the user inputs the correct amount. If the soil has no rock fragments, the user must enter 0's.

After the three variable are entered, the program will calculate and then ask the user if they would like to convert the calculated values into the Ksat revised classes, as defined by NRCS (citation needed). A response of 'y' will print the range of low, representative, and high ksat values for each class. This is determined by if the calculated values falls within that current range. A response of 'n' will simply print the calculated ksat values of each sample. 

Future version will add a third option to print both the actual calculated value and the representative classes.

How Ksat is Calculated:
Ksat is first calculated on the soil without the rock fragments using the equation from A. A. Suleiman, J. T. Ritchie, 2001 American Society of Agricultural Engineers.

That ksat value is then adjust for the given fragment volume according to the equation from Peck and Watson 1979.

Credit goes to my supervisor Brian for originally finding and utilizing these equations.

Special considerations:
- If the user enters the wrong number of samples at the start, it may be best to restart the program or enter 0's (if the user entered too many samples). Future updates may provide an option to reset number of samples.
- Ksat calculation result is an estimate. Therefore, it is recommended to use the ksat revised classes when reporting.
- Program will produce an error if user inputs anything other than a numeric (i.e. no strings).


