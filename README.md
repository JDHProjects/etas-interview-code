# ETAS Calendar Coding Exercise
### By Joshua Purdy
Script name: `calendarGen.py`

## How To Use
Script can be provided year and filename as args:
* year specified with `y=<YEAR>`
  * Year must be 1583 or higher
  * If 1583 selected no previous year calendar will be generated, otherwise a calender will be generated for `YEAR-1`, `YEAR` and `YEAR+1`.
* filename specified with `f=<FILENAME>`
  * If filename is not provided, HTML will be output to terminal. 

## Further Info
Methods in code are all docstring commented. 

Script ran with Python 3.7

## Testing
All methods unit tested, unit tests can be found in file `test_calendarGen.py`

tests ran with command `pytest`

