import math

# Info for each month, months indexed from 0, includes days in month and text representation of month
MONTHS = [
  {
    "name": "January",
    "days": 31},
  {
    "name": "February",
    "days": 28},
  {
    "name": "March",
    "days": 31},
  {
    "name": "April",
    "days": 30},
  {
    "name": "May",
    "days": 31},
  {
    "name": "June",
    "days": 30},
  {
    "name": "July",
    "days": 31},
  {
    "name": "August",
    "days": 31},
  {
    "name": "September",
    "days": 30},
  {
    "name": "October",
    "days": 31},
  {
    "name": "November",
    "days": 30},
  {
    "name": "December",
    "days": 31},
]

# Header and style sheet
HTML_HEAD="""<!DOCTYPE html>
<html>
<style>
  table, td, th { 
    border: 1px solid black;
    color: black;
    text-align: center;
    border-collapse: collapse;
  }
  th.year {
    background-color: #D6FDD0;
    font-size: large;
    color: black;
    padding: 5px;
    
  }
  table.year {
    margin: 25px auto;
    width: 880px;
  }
  td.month { 
    padding: 10px;
    width: 220px;
  }
  td {
    background-color: #FFFFFF;
    width: 25px;
  }
  th.month {
    background-color: #D6FDD0;
    font-size: medium;
  }
  table.month {
    width: 200px;
    height: 200px;
  }
  td.work-week {
    background-color: #E6E6E6;
  }
  td.week-num {
    font-size: smaller;
    background-color: #E6E6E6;
  }
  td.sat {
    background-color: #FFFED1;
  }
  td.sun {
    background-color: #F7CDA0;
  }
</style>
<body style="background-color:white;">
"""

# End of body and html document
HTML_END = """</body>
</html>
"""


def buildRow(cellValues, cellClasses):
  """
  Generates the HTML required to display a row according to provided args

  args:
    list [8] - cellValues - values to go in each cell of row
    list [8] - cellClasses - class to apply to each cell of row

  return:
    string - HTML representation of row
  """

  htmlString = "          <tr>\n"
  for i in range(0,8):
    htmlString += "            <td"+cellClasses[i]
    htmlString += ">"+cellValues[i]+"</td>\n"
  htmlString += "          </tr>\n"
  return htmlString


def buildMonth(monthName, monthGrid):
  """
  Generates the HTML required to display a month according to provided args

  args:
    string - monthName - name of month to use as table header
    list [6][8] - monthGrid - 2D list of values to go in each cell of the month

  return:
    string - HTML representation of month
  """

  htmlString="        <table class=month>\n          <tr>\n            <th colspan=8 class=month>"+monthName+"</th>\n          </tr>\n"
  htmlString+=buildRow(["Wk", "Mo", "Tu", "We", "Th", "Fr", "Sa", "Su"], [" class=week-num", " class=work-week", " class=work-week", " class=work-week", " class=work-week", " class=work-week", " class=sat", " class=sun"])
  for row in monthGrid:
    htmlString+=buildRow(row, [" class=week-num","","","","",""," class=sat"," class=sun"])
  htmlString+="        </table>\n"
  return htmlString


def getStartOfMonth(year, month):
  """
  Calculates the day of the week for the 1st day of specified month and year.
  Equation modified from code found here: https://cs.uwaterloo.ca/~alopez-o/math-faq/node73.html

  args:
    int - year - year the month is contained within
    int - month - 0 index month to calculate start day of week for

  return:
    int - index of day of the week, 0 index, monday = 0
  """

  # offsets required as algorithm requires 1 index month where march = 1 and feb treated as previous year month 12
  monthOffset=(month+1+10)%12
  if(monthOffset == 0):
    monthOffset = 12
  if(month < 2):
    yearOffset = year-1
  else:
    yearOffset = year
  return ((1 + math.floor(2.6*monthOffset - 0.2) -2*(yearOffset//100) + (yearOffset%100) + (yearOffset%100)//4 + (yearOffset//100)//4-1)%7)


def genMonthGrid(startDay, weekNums, totalDays):
  """
  Generates 2D list representation of month excluding headers

  args:
    int - startDay - 0 index day of the week the month starts on
    list [8] - weekNums - week numbers as int
    int - totalDays - total amount of days in the month

  return:
    list [6][8] - 2D list of cell values for month 
  """

  month = []
  dayCounter = 1 - startDay
  for col in range(0,6):
    week = [str(weekNums[col])]
    for row in range(1,8):
      if(dayCounter > 0 and dayCounter <= totalDays):
        week.append(str(dayCounter))
      else:
        week.append("")
      dayCounter+=1
    month.append(week)
  return month


def buildYear(year):
  """
  Generates the HTML required to display specified year

  args:
    int - year - year to generate calendar for

  return:
    string - HTML representation of year
  """

  htmlString="  <table class=year>\n    <tr>\n      <th colspan=8 class=year>"+str(year)+"</th>\n    </tr>\n"
  
  month = 0
  leapYear = isLeapYear(year)
  for row in range(0,3):
    htmlString+="    <tr>\n"
    for col in range(0,4):
      startOfMonth = getStartOfMonth(year,month)
      daysInMonth = MONTHS[month]["days"]
      if(month == 1 and leapYear):
        daysInMonth += 1
      htmlString+="      <td class=month>\n"
      htmlString+=buildMonth(MONTHS[month]["name"],genMonthGrid(startOfMonth, getWeekNums(month, startOfMonth, leapYear), daysInMonth))
      htmlString+="      </td>\n"
      month+=1
    htmlString+="    </tr>\n"
  htmlString+="  </table>\n"
    
  return htmlString


def isLeapYear(year):
  """
  Calculates if specified year is a leap year

  args:
    int - year - year to check if leap

  return:
    bool - True if leap year
  """

  if (year % 4 != 0):
    return False
  if (year % 100 == 0):
    if (year % 400 != 0):
      return False
  return True


def getWeekNums(month, dayOfWeek, leap):
  """
  Calculates week numbers required for specific month according to ISO 8601 standard
  Formula used found here: https://en.wikipedia.org/wiki/ISO_week_date

  args:
    int - month - 0 indexed index of month to calculate week numbers for
    int - dayOfWeek - 0 indexed index of day of week, 0 = monday
    bool - leap - if month is part of a leap year

  return:
    list [6] - list of int week indexes for whole month
  """

  ordinalDate = 0
  for i in range(0, month):
    ordinalDate+=MONTHS[i]["days"]
    if (i==1 and leap):
      ordinalDate+=1
  weekNum = (ordinalDate - (dayOfWeek + 1) + 10) // 7
  if (weekNum == 0):
    if((dayOfWeek == 3 and not leap) or (dayOfWeek == 4 and leap)):
      return [53,1,2,3,4,5]
    return [52,1,2,3,4,5]
  return list(range(weekNum,weekNum+6))


def errorAndExit(msg):
  """
  Outputs an error to the user before exiting

  args:
    string - msg - error message to output

  return:
    none
  """

  print("ERROR: "+str(msg))
  exit()


def parseArgs(args):
  """
  Retrieves the year input by user, verifies output and quits if invalid
  Creates list of years to generate calendars for: [year-1, year, year+1]
  Minimum year 1583, if 1583 provided only 2 years will be generated
  Gets filename if provided

  args:
    list [] - args - list of args provided to script

  return:
    list [2-3] - list of years to generate calendars for
    string - filename (empty string if no filename provided)
  """

  year = None
  filename=""

  for arg in args:
    if (len(arg) > 2):
      if (arg[0:2].lower() == "y="):
        try:
          year = int(arg[2:])
        except:
          errorAndExit("Invalid year arg provided")
      elif (arg[0:2].lower() == "f="):
        filename = arg[2:]
  if (year == None):
    errorAndExit("No year arg provided")

  if (year < 1583):
    errorAndExit("Year earlier than 1583")
  
  yearList = []

  if(year != 1583):
    yearList.append(year-1)
  yearList.append(year)
  yearList.append(year+1)
  
  return (yearList, filename)


def output(htmlString, filename):
  """
  Output HTML to file specified with filename
  If filename not specified, print HTML to console

  args:
    string - htmlString - calendar HTML file as string
    string - filename - filename to use to save HTML

  return:
    None
  """
  if (filename == ""):
    print(htmlString)
    return
  
  with open(filename, "w") as openFile:
    openFile.write(htmlString)

if (__name__ == "__main__"):
  import sys

  # Gen yearlist from provided user input
  (yearList, filename) = parseArgs(sys.argv)

  # Gen HTML according to yearlist
  htmlString = HTML_HEAD
  for year in yearList:
    htmlString += buildYear(year)
  htmlString += HTML_END

  # Output HTML
  output(htmlString, filename)