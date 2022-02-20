import calendarGen

def test_buildRow_1():
  htmlRow ="""    <tr>
      <td class=week-num>1</td>
      <td></td>
      <td></td>
      <td></td>
      <td>1</td>
      <td>2</td>
      <td class=sat>3</td>
      <td class=sun>4</td>
    </tr>
"""
  assert htmlRow == calendarGen.buildRow(["1","","","","1","2","3","4"],[" class=week-num","","","","",""," class=sat"," class=sun"])

def test_buildRow_2():
  htmlRow ="""    <tr>
      <td class=week-num>Wk</td>
      <td class=work-week>Mo</td>
      <td class=work-week>Tu</td>
      <td class=work-week>We</td>
      <td class=work-week>Th</td>
      <td class=work-week>Fr</td>
      <td class=sat>Sa</td>
      <td class=sun>Su</td>
    </tr>
"""
  assert htmlRow == calendarGen.buildRow(["Wk", "Mo", "Tu", "We", "Th", "Fr", "Sa", "Su"], [" class=week-num", " class=work-week", " class=work-week", " class=work-week", " class=work-week", " class=work-week", " class=sat", " class=sun"])

def test_buildMonth_1():
  htmlRow ="""  <table class=month>
    <tr>
      <th colspan=8 class=header>October</th>
  </tr>
    <tr>
      <td class=week-num>Wk</td>
      <td class=work-week>Mo</td>
      <td class=work-week>Tu</td>
      <td class=work-week>We</td>
      <td class=work-week>Th</td>
      <td class=work-week>Fr</td>
      <td class=sat>Sa</td>
      <td class=sun>Su</td>
    </tr>
    <tr>
      <td class=week-num>39</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td class=sat>1</td>
      <td class=sun>2</td>
    </tr>
    <tr>
      <td class=week-num>40</td>
      <td>3</td>
      <td>4</td>
      <td>5</td>
      <td>6</td>
      <td>7</td>
      <td class=sat>8</td>
      <td class=sun>9</td>
    </tr>
    <tr>
      <td class=week-num>41</td>
      <td>10</td>
      <td>11</td>
      <td>12</td>
      <td>13</td>
      <td>14</td>
      <td class=sat>15</td>
      <td class=sun>16</td>
    </tr>
    <tr>
      <td class=week-num>42</td>
      <td>17</td>
      <td>18</td>
      <td>19</td>
      <td>20</td>
      <td>21</td>
      <td class=sat>22</td>
      <td class=sun>23</td>
    </tr>
    <tr>
      <td class=week-num>43</td>
      <td>24</td>
      <td>25</td>
      <td>26</td>
      <td>27</td>
      <td>28</td>
      <td class=sat>29</td>
      <td class=sun>30</td>
    </tr>
    <tr>
      <td class=week-num>41</td>
      <td>31</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td class=sat></td>
      <td class=sun></td>
    </tr>
  </table>
"""

  assert htmlRow == calendarGen.buildMonth("October", [["39","","","","","","1","2"],["40","3","4","5","6","7","8","9"],["41","10","11","12","13","14","15","16"],["42","17","18","19","20","21","22","23"],["43","24","25","26","27","28","29","30"],["41","31","","","","","",""]])

def test_isLeapYear_1():
  assert False == calendarGen.isLeapYear(1900)

def test_isLeapYear_2():
  assert True == calendarGen.isLeapYear(2000)

def test_isLeapYear_3():
  assert True == calendarGen.isLeapYear(1988)

def test_isLeapYear_4():
  assert False == calendarGen.isLeapYear(1987)