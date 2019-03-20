# LuccaDevises

https://www.lucca.fr/societe/recrutement/test-technique-back-end

## PREREQUISITES

You must have python3 install on your os and an package installer.
I recommend you to use pip3: https://docs.python.org/3/installing/index.html

```
pip3 install networkx
```
For running our program, you must create a file with specifics data inside

On the first line you must have:
```
CURRENCY YOU HAVE;AMOUNT;CURRENCY TO CONVERTED
```

On the second
```
NUMBER OF DATA PROVIDED
```

On the third and next (depending on how much data you provide)

```
CURRENCY A;CURRENCY B;RATE
```

An example
```
EUR;550;JPY
6
AUD;CHF;0.9661
JPY;KRW;13.1151
EUR;CHF;1.2053
AUD;JPY;86.0305
EUR;USD;1.2989
JPY;INR;0.6571
```

## RUNNING

Command line:

```
python3 srcs/LuccaDevises.py -f <YOUR FILE PREVIOUSLY CREATED>
```
Output:

```
You have 550 EUR and want to have JPY
EUR -> CHF = 550.0 * 1.2053 = 662.915
CHF -> AUD = 662.915 * 1.0351 = 686.1833
AUD -> JPY = 686.1833 * 86.0305 = 59032.6924
You have 59033 JPY
```
Enjoy!
