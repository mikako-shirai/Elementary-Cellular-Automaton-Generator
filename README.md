# Elementary Cellular Automaton Generator
#### Simple code that generates patterns of [elementary cellular automaton](https://en.wikipedia.org/wiki/Elementary_cellular_automaton) using Python.  
  
###  To run the code  
1. move to the directory you want to create outputs in  
```
$ cd [PATH]
```  
2. clone this repository  
```
$ git clone https://github.com/mikako-shirai/Elementary-Cellular-Automaton-Generator.git
```  
4. run the python file  
```
$ python3 main.py
```  
  
### After running the file
By running main.py, it reads the following three inputs from command line
- a decimal number
- a number of rows in the output (optional, default value = 200)
- a number of columns in the output (optional, default value = 400)  

on command line :  
```
rule number (0-255) : [YOUR INPUT] (example : 110)
number of row (hit enter to skip) : 
number of column (hit enter to skip) : 
```  
  
After converting the first input to a binary number, it creates a text file of the pattern consisting of 0s (as white cells) and 1s (as black cells) in the directory you are currently in
```
rule_110.txt
main.py
```  
  
## Examples of outputs
### Rule 90  
![Rule 90](https://github.com/mikako-shirai/Elementary-Cellular-Automaton-Generator/blob/main/images/rule_90.png)  

### Rule 99  
![Rule 99](https://github.com/mikako-shirai/Elementary-Cellular-Automaton-Generator/blob/main/images/rule_99.png)  

### Rule 110  
![Rule 110](https://github.com/mikako-shirai/Elementary-Cellular-Automaton-Generator/blob/main/images/rule_110.png)  

### Rule 150  
![Rule 150](https://github.com/mikako-shirai/Elementary-Cellular-Automaton-Generator/blob/main/images/rule_150.png)  
