# Elementary-Cellular-Automaton-Generator
A simple [elementary cellular automaton](https://en.wikipedia.org/wiki/Elementary_cellular_automaton) generator  
  
This program generates patterns of elementary cellular automaton using Python  
By running main.py, it reads the following three inputs from command line
- a decimal number
- a number of rows in output (optional, default value = 200)
- a number of columns in output (optional, default value = 400)
  
```
> rule number (0-255) : 110
> number of row (hit enter to skip) : 
> number of column (hit enter to skip) : 
```
After converting the first input to binary number, it creates a text file of the pattern consisting of 0s (as white cells) and 1s (as black cells) in the directory you are currently in
```
rule_110.txt
main.py
```

