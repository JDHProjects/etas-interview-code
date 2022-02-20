import math
import sys

months = [
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


htmlStart="""<!DOCTYPE html>
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

htmlEnd = """</body>
</html>
"""

def buildRow(cellValues, cellClasses):
  htmlString = "          <tr>\n"
  for i in range(0,8):
    htmlString += "            <td"+cellClasses[i]
    htmlString += ">"+cellValues[i]+"</td>\n"
  htmlString += "          </tr>\n"
  return htmlString

def buildMonth(monthName, monthGrid):
  htmlString="        <table class=month>\n          <tr>\n            <th colspan=8 class=month>"+monthName+"</th>\n          </tr>\n"
  htmlString+=buildRow(["Wk", "Mo", "Tu", "We", "Th", "Fr", "Sa", "Su"], [" class=week-num", " class=work-week", " class=work-week", " class=work-week", " class=work-week", " class=work-week", " class=sat", " class=sun"])
  for row in monthGrid:
    htmlString+=buildRow(row, [" class=week-num","","","","",""," class=sat"," class=sun"])
  htmlString+="        </table>\n"
  return htmlString

def getStartOfMonth(year, month):
  # equation modified from code found here: https://cs.uwaterloo.ca/~alopez-o/math-faq/node73.html
  monthOffset=(month+1+10)%12
  if(monthOffset == 0):
    monthOffset = 12
  if(month < 2):
    yearOffset = year-1
  else:
    yearOffset = year
  return ((1 + math.floor(2.6*monthOffset - 0.2) -2*(yearOffset//100) + (yearOffset%100) + (yearOffset%100)//4 + (yearOffset//100)//4-1)%7)


def genMonthGrid(startDay, weekNums, totalDays):
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
  htmlString="  <table class=year>\n    <tr>\n      <th colspan=8 class=year>"+str(year)+"</th>\n    </tr>\n"
  
  month = 0
  leapYear = isLeapYear(year)
  for row in range(0,3):
    htmlString+="    <tr>\n"
    for col in range(0,4):
      startOfMonth = getStartOfMonth(year,month)
      daysInMonth = months[month]["days"]
      if(month == 1 and leapYear):
        daysInMonth += 1
      htmlString+="      <td class=month>\n"
      htmlString+=buildMonth(months[month]["name"],genMonthGrid(startOfMonth, getWeekNums(month, startOfMonth, leapYear), daysInMonth))
      htmlString+="      </td>\n"
      month+=1
    htmlString+="    </tr>\n"
  htmlString+="  </table>\n"
    
  return htmlString

def isLeapYear(year):
  if (year % 4 != 0):
    return False
  if (year % 100 == 0):
    if (year % 400 != 0):
      return False
  return True

def getWeekNums(month, dayOfWeek, leap):
  # formula used found here: https://en.wikipedia.org/wiki/ISO_week_date
  ordinalDate = 0
  for i in range(0, month):
    ordinalDate+=months[i]["days"]
    if (i==1 and leap):
      ordinalDate+=1
  weekNum = (ordinalDate - (dayOfWeek + 1) + 10) // 7
  if (weekNum == 0):
    if((dayOfWeek == 3 and not leap) or (dayOfWeek == 4 and leap)):
      return [53,1,2,3,4,5]
    return [52,1,2,3,4,5]
  return list(range(weekNum,weekNum+6))

def errorAndExit(msg):
  print("ERROR: "+str(msg))
  exit()

def parseYearListFromArgs(args):
  if (len(args) != 2):
    errorAndExit("Exactly one arg (year) must be provided!")

  try:
    year = int(args[1])
  except:
    errorAndExit("Invalid year arg provided!")

  if (year < 1583):
    errorAndExit("Year earlier than 1583")
  
  yearList = []

  if(year != 1583):
    yearList.append(year-1)
  yearList.append(year)
  yearList.append(year+1)
  
  return yearList



if __name__ == "__main__":
  yearList = parseYearListFromArgs(sys.argv)
  htmlString = htmlStart
  for year in yearList:
    htmlString += buildYear(year)
  htmlString += htmlEnd
  
  print(htmlString)