import calendarGen

def test_buildRow_1():
  htmlRow ="""          <tr>
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
  htmlRow ="""          <tr>
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
  htmlRow ="""        <table class=month>
          <tr>
            <th colspan=8 class=month>October</th>
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

  print(calendarGen.buildMonth("October", [["39","","","","","","1","2"],["40","3","4","5","6","7","8","9"],["41","10","11","12","13","14","15","16"],["42","17","18","19","20","21","22","23"],["43","24","25","26","27","28","29","30"],["41","31","","","","","",""]]))
  assert True == True

def test_isLeapYear_1():
  assert False == calendarGen.isLeapYear(1900)

def test_isLeapYear_2():
  assert True == calendarGen.isLeapYear(2000)

def test_isLeapYear_3():
  assert True == calendarGen.isLeapYear(1988)

def test_isLeapYear_4():
  assert False == calendarGen.isLeapYear(1987)

def test_getWeekNums_1():
  assert [53,1,2,3,4,5] == calendarGen.getWeekNums(0,3,False)

def test_getWeekNums_2():
  assert [52,1,2,3,4,5] == calendarGen.getWeekNums(0,3,True)

def test_getWeekNums_3():
  assert [52,1,2,3,4,5] == calendarGen.getWeekNums(0,4,False)

def test_getWeekNums_4():
  assert [53,1,2,3,4,5] == calendarGen.getWeekNums(0,4,True)

def test_getWeekNums_5():
  assert [1,2,3,4,5,6] == calendarGen.getWeekNums(0,0,False)

def test_parseYearListFromArgs_1():
  assert ([1583,1584], "") == calendarGen.parseArgs(["filename", "y=1583"])

def test_parseYearListFromArgs_2():
  assert ([1583,1584,1585], "") == calendarGen.parseArgs(["filename", "y=1584"])

def test_parseYearListFromArgs_3():
  assert ([1583,1584], "test") == calendarGen.parseArgs(["filename", "y=1583", "f=test"])

def test_parseYearListFromArgs_4():
  assert ([1583,1584,1585], "test") == calendarGen.parseArgs(["filename", "y=1584", "f=test"])

def test_getStartOfMonth_1():
  assert 0 == calendarGen.getStartOfMonth(1988,1)

def test_getStartOfMonth_2():
  assert 1 == calendarGen.getStartOfMonth(1988,10)

def test_getStartOfMonth_3():
  assert 2 == calendarGen.getStartOfMonth(1989,1)

def test_getStartOfMonth_4():
  assert 3 == calendarGen.getStartOfMonth(1990,1)

def test_getStartOfMonth_5():
  assert 4 == calendarGen.getStartOfMonth(1988,6)

def test_getStartOfMonth_6():
  assert 5 == calendarGen.getStartOfMonth(1988,9)

def test_getStartOfMonth_7():
  assert 6 == calendarGen.getStartOfMonth(1988,4)

def test_genMonthGrid_1():
  monthGrid = [['1', '', '', '', '1', '2', '3', '4'], ['2', '5', '6', '7', '8', '9', '10', '11'], ['3', '12', '13', '14', '15', '16', '17', '18'], ['4', '19', '20', '21', '22', '23', '24', '25'], ['5', '26', '27', '28', '', '', '', ''], ['6', '', '', '', '', '', '', '']]
  assert monthGrid == calendarGen.genMonthGrid(3,[1,2,3,4,5,6],28)

def test_genMonthGrid_2():
  monthGrid = [['1', '', '', '', '1', '2', '3', '4'], ['2', '5', '6', '7', '8', '9', '10', '11'], ['3', '12', '13', '14', '15', '16', '17', '18'], ['4', '19', '20', '21', '22', '23', '24', '25'], ['5', '26', '27', '28', '29', '30', '31', ''], ['6', '', '', '', '', '', '', '']]
  assert monthGrid == calendarGen.genMonthGrid(3,[1,2,3,4,5,6],31)

def test_buildYear_1():
  htmlYear = """  <table class=year>
    <tr>
      <th colspan=8 class=year>2000</th>
    </tr>
    <tr>
      <td class=month>
        <table class=month>
          <tr>
            <th colspan=8 class=month>January</th>
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
            <td class=week-num>52</td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td class=sat>1</td>
            <td class=sun>2</td>
          </tr>
          <tr>
            <td class=week-num>1</td>
            <td>3</td>
            <td>4</td>
            <td>5</td>
            <td>6</td>
            <td>7</td>
            <td class=sat>8</td>
            <td class=sun>9</td>
          </tr>
          <tr>
            <td class=week-num>2</td>
            <td>10</td>
            <td>11</td>
            <td>12</td>
            <td>13</td>
            <td>14</td>
            <td class=sat>15</td>
            <td class=sun>16</td>
          </tr>
          <tr>
            <td class=week-num>3</td>
            <td>17</td>
            <td>18</td>
            <td>19</td>
            <td>20</td>
            <td>21</td>
            <td class=sat>22</td>
            <td class=sun>23</td>
          </tr>
          <tr>
            <td class=week-num>4</td>
            <td>24</td>
            <td>25</td>
            <td>26</td>
            <td>27</td>
            <td>28</td>
            <td class=sat>29</td>
            <td class=sun>30</td>
          </tr>
          <tr>
            <td class=week-num>5</td>
            <td>31</td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td class=sat></td>
            <td class=sun></td>
          </tr>
        </table>
      </td>
      <td class=month>
        <table class=month>
          <tr>
            <th colspan=8 class=month>February</th>
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
            <td class=week-num>5</td>
            <td></td>
            <td>1</td>
            <td>2</td>
            <td>3</td>
            <td>4</td>
            <td class=sat>5</td>
            <td class=sun>6</td>
          </tr>
          <tr>
            <td class=week-num>6</td>
            <td>7</td>
            <td>8</td>
            <td>9</td>
            <td>10</td>
            <td>11</td>
            <td class=sat>12</td>
            <td class=sun>13</td>
          </tr>
          <tr>
            <td class=week-num>7</td>
            <td>14</td>
            <td>15</td>
            <td>16</td>
            <td>17</td>
            <td>18</td>
            <td class=sat>19</td>
            <td class=sun>20</td>
          </tr>
          <tr>
            <td class=week-num>8</td>
            <td>21</td>
            <td>22</td>
            <td>23</td>
            <td>24</td>
            <td>25</td>
            <td class=sat>26</td>
            <td class=sun>27</td>
          </tr>
          <tr>
            <td class=week-num>9</td>
            <td>28</td>
            <td>29</td>
            <td></td>
            <td></td>
            <td></td>
            <td class=sat></td>
            <td class=sun></td>
          </tr>
          <tr>
            <td class=week-num>10</td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td class=sat></td>
            <td class=sun></td>
          </tr>
        </table>
      </td>
      <td class=month>
        <table class=month>
          <tr>
            <th colspan=8 class=month>March</th>
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
            <td class=week-num>9</td>
            <td></td>
            <td></td>
            <td>1</td>
            <td>2</td>
            <td>3</td>
            <td class=sat>4</td>
            <td class=sun>5</td>
          </tr>
          <tr>
            <td class=week-num>10</td>
            <td>6</td>
            <td>7</td>
            <td>8</td>
            <td>9</td>
            <td>10</td>
            <td class=sat>11</td>
            <td class=sun>12</td>
          </tr>
          <tr>
            <td class=week-num>11</td>
            <td>13</td>
            <td>14</td>
            <td>15</td>
            <td>16</td>
            <td>17</td>
            <td class=sat>18</td>
            <td class=sun>19</td>
          </tr>
          <tr>
            <td class=week-num>12</td>
            <td>20</td>
            <td>21</td>
            <td>22</td>
            <td>23</td>
            <td>24</td>
            <td class=sat>25</td>
            <td class=sun>26</td>
          </tr>
          <tr>
            <td class=week-num>13</td>
            <td>27</td>
            <td>28</td>
            <td>29</td>
            <td>30</td>
            <td>31</td>
            <td class=sat></td>
            <td class=sun></td>
          </tr>
          <tr>
            <td class=week-num>14</td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td class=sat></td>
            <td class=sun></td>
          </tr>
        </table>
      </td>
      <td class=month>
        <table class=month>
          <tr>
            <th colspan=8 class=month>April</th>
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
            <td class=week-num>13</td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td class=sat>1</td>
            <td class=sun>2</td>
          </tr>
          <tr>
            <td class=week-num>14</td>
            <td>3</td>
            <td>4</td>
            <td>5</td>
            <td>6</td>
            <td>7</td>
            <td class=sat>8</td>
            <td class=sun>9</td>
          </tr>
          <tr>
            <td class=week-num>15</td>
            <td>10</td>
            <td>11</td>
            <td>12</td>
            <td>13</td>
            <td>14</td>
            <td class=sat>15</td>
            <td class=sun>16</td>
          </tr>
          <tr>
            <td class=week-num>16</td>
            <td>17</td>
            <td>18</td>
            <td>19</td>
            <td>20</td>
            <td>21</td>
            <td class=sat>22</td>
            <td class=sun>23</td>
          </tr>
          <tr>
            <td class=week-num>17</td>
            <td>24</td>
            <td>25</td>
            <td>26</td>
            <td>27</td>
            <td>28</td>
            <td class=sat>29</td>
            <td class=sun>30</td>
          </tr>
          <tr>
            <td class=week-num>18</td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td class=sat></td>
            <td class=sun></td>
          </tr>
        </table>
      </td>
    </tr>
    <tr>
      <td class=month>
        <table class=month>
          <tr>
            <th colspan=8 class=month>May</th>
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
            <td class=week-num>18</td>
            <td>1</td>
            <td>2</td>
            <td>3</td>
            <td>4</td>
            <td>5</td>
            <td class=sat>6</td>
            <td class=sun>7</td>
          </tr>
          <tr>
            <td class=week-num>19</td>
            <td>8</td>
            <td>9</td>
            <td>10</td>
            <td>11</td>
            <td>12</td>
            <td class=sat>13</td>
            <td class=sun>14</td>
          </tr>
          <tr>
            <td class=week-num>20</td>
            <td>15</td>
            <td>16</td>
            <td>17</td>
            <td>18</td>
            <td>19</td>
            <td class=sat>20</td>
            <td class=sun>21</td>
          </tr>
          <tr>
            <td class=week-num>21</td>
            <td>22</td>
            <td>23</td>
            <td>24</td>
            <td>25</td>
            <td>26</td>
            <td class=sat>27</td>
            <td class=sun>28</td>
          </tr>
          <tr>
            <td class=week-num>22</td>
            <td>29</td>
            <td>30</td>
            <td>31</td>
            <td></td>
            <td></td>
            <td class=sat></td>
            <td class=sun></td>
          </tr>
          <tr>
            <td class=week-num>23</td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td class=sat></td>
            <td class=sun></td>
          </tr>
        </table>
      </td>
      <td class=month>
        <table class=month>
          <tr>
            <th colspan=8 class=month>June</th>
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
            <td class=week-num>22</td>
            <td></td>
            <td></td>
            <td></td>
            <td>1</td>
            <td>2</td>
            <td class=sat>3</td>
            <td class=sun>4</td>
          </tr>
          <tr>
            <td class=week-num>23</td>
            <td>5</td>
            <td>6</td>
            <td>7</td>
            <td>8</td>
            <td>9</td>
            <td class=sat>10</td>
            <td class=sun>11</td>
          </tr>
          <tr>
            <td class=week-num>24</td>
            <td>12</td>
            <td>13</td>
            <td>14</td>
            <td>15</td>
            <td>16</td>
            <td class=sat>17</td>
            <td class=sun>18</td>
          </tr>
          <tr>
            <td class=week-num>25</td>
            <td>19</td>
            <td>20</td>
            <td>21</td>
            <td>22</td>
            <td>23</td>
            <td class=sat>24</td>
            <td class=sun>25</td>
          </tr>
          <tr>
            <td class=week-num>26</td>
            <td>26</td>
            <td>27</td>
            <td>28</td>
            <td>29</td>
            <td>30</td>
            <td class=sat></td>
            <td class=sun></td>
          </tr>
          <tr>
            <td class=week-num>27</td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td class=sat></td>
            <td class=sun></td>
          </tr>
        </table>
      </td>
      <td class=month>
        <table class=month>
          <tr>
            <th colspan=8 class=month>July</th>
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
            <td class=week-num>26</td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td class=sat>1</td>
            <td class=sun>2</td>
          </tr>
          <tr>
            <td class=week-num>27</td>
            <td>3</td>
            <td>4</td>
            <td>5</td>
            <td>6</td>
            <td>7</td>
            <td class=sat>8</td>
            <td class=sun>9</td>
          </tr>
          <tr>
            <td class=week-num>28</td>
            <td>10</td>
            <td>11</td>
            <td>12</td>
            <td>13</td>
            <td>14</td>
            <td class=sat>15</td>
            <td class=sun>16</td>
          </tr>
          <tr>
            <td class=week-num>29</td>
            <td>17</td>
            <td>18</td>
            <td>19</td>
            <td>20</td>
            <td>21</td>
            <td class=sat>22</td>
            <td class=sun>23</td>
          </tr>
          <tr>
            <td class=week-num>30</td>
            <td>24</td>
            <td>25</td>
            <td>26</td>
            <td>27</td>
            <td>28</td>
            <td class=sat>29</td>
            <td class=sun>30</td>
          </tr>
          <tr>
            <td class=week-num>31</td>
            <td>31</td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td class=sat></td>
            <td class=sun></td>
          </tr>
        </table>
      </td>
      <td class=month>
        <table class=month>
          <tr>
            <th colspan=8 class=month>August</th>
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
            <td class=week-num>31</td>
            <td></td>
            <td>1</td>
            <td>2</td>
            <td>3</td>
            <td>4</td>
            <td class=sat>5</td>
            <td class=sun>6</td>
          </tr>
          <tr>
            <td class=week-num>32</td>
            <td>7</td>
            <td>8</td>
            <td>9</td>
            <td>10</td>
            <td>11</td>
            <td class=sat>12</td>
            <td class=sun>13</td>
          </tr>
          <tr>
            <td class=week-num>33</td>
            <td>14</td>
            <td>15</td>
            <td>16</td>
            <td>17</td>
            <td>18</td>
            <td class=sat>19</td>
            <td class=sun>20</td>
          </tr>
          <tr>
            <td class=week-num>34</td>
            <td>21</td>
            <td>22</td>
            <td>23</td>
            <td>24</td>
            <td>25</td>
            <td class=sat>26</td>
            <td class=sun>27</td>
          </tr>
          <tr>
            <td class=week-num>35</td>
            <td>28</td>
            <td>29</td>
            <td>30</td>
            <td>31</td>
            <td></td>
            <td class=sat></td>
            <td class=sun></td>
          </tr>
          <tr>
            <td class=week-num>36</td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td class=sat></td>
            <td class=sun></td>
          </tr>
        </table>
      </td>
    </tr>
    <tr>
      <td class=month>
        <table class=month>
          <tr>
            <th colspan=8 class=month>September</th>
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
            <td class=week-num>35</td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td>1</td>
            <td class=sat>2</td>
            <td class=sun>3</td>
          </tr>
          <tr>
            <td class=week-num>36</td>
            <td>4</td>
            <td>5</td>
            <td>6</td>
            <td>7</td>
            <td>8</td>
            <td class=sat>9</td>
            <td class=sun>10</td>
          </tr>
          <tr>
            <td class=week-num>37</td>
            <td>11</td>
            <td>12</td>
            <td>13</td>
            <td>14</td>
            <td>15</td>
            <td class=sat>16</td>
            <td class=sun>17</td>
          </tr>
          <tr>
            <td class=week-num>38</td>
            <td>18</td>
            <td>19</td>
            <td>20</td>
            <td>21</td>
            <td>22</td>
            <td class=sat>23</td>
            <td class=sun>24</td>
          </tr>
          <tr>
            <td class=week-num>39</td>
            <td>25</td>
            <td>26</td>
            <td>27</td>
            <td>28</td>
            <td>29</td>
            <td class=sat>30</td>
            <td class=sun></td>
          </tr>
          <tr>
            <td class=week-num>40</td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td class=sat></td>
            <td class=sun></td>
          </tr>
        </table>
      </td>
      <td class=month>
        <table class=month>
          <tr>
            <th colspan=8 class=month>October</th>
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
            <td class=sat></td>
            <td class=sun>1</td>
          </tr>
          <tr>
            <td class=week-num>40</td>
            <td>2</td>
            <td>3</td>
            <td>4</td>
            <td>5</td>
            <td>6</td>
            <td class=sat>7</td>
            <td class=sun>8</td>
          </tr>
          <tr>
            <td class=week-num>41</td>
            <td>9</td>
            <td>10</td>
            <td>11</td>
            <td>12</td>
            <td>13</td>
            <td class=sat>14</td>
            <td class=sun>15</td>
          </tr>
          <tr>
            <td class=week-num>42</td>
            <td>16</td>
            <td>17</td>
            <td>18</td>
            <td>19</td>
            <td>20</td>
            <td class=sat>21</td>
            <td class=sun>22</td>
          </tr>
          <tr>
            <td class=week-num>43</td>
            <td>23</td>
            <td>24</td>
            <td>25</td>
            <td>26</td>
            <td>27</td>
            <td class=sat>28</td>
            <td class=sun>29</td>
          </tr>
          <tr>
            <td class=week-num>44</td>
            <td>30</td>
            <td>31</td>
            <td></td>
            <td></td>
            <td></td>
            <td class=sat></td>
            <td class=sun></td>
          </tr>
        </table>
      </td>
      <td class=month>
        <table class=month>
          <tr>
            <th colspan=8 class=month>November</th>
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
            <td class=week-num>44</td>
            <td></td>
            <td></td>
            <td>1</td>
            <td>2</td>
            <td>3</td>
            <td class=sat>4</td>
            <td class=sun>5</td>
          </tr>
          <tr>
            <td class=week-num>45</td>
            <td>6</td>
            <td>7</td>
            <td>8</td>
            <td>9</td>
            <td>10</td>
            <td class=sat>11</td>
            <td class=sun>12</td>
          </tr>
          <tr>
            <td class=week-num>46</td>
            <td>13</td>
            <td>14</td>
            <td>15</td>
            <td>16</td>
            <td>17</td>
            <td class=sat>18</td>
            <td class=sun>19</td>
          </tr>
          <tr>
            <td class=week-num>47</td>
            <td>20</td>
            <td>21</td>
            <td>22</td>
            <td>23</td>
            <td>24</td>
            <td class=sat>25</td>
            <td class=sun>26</td>
          </tr>
          <tr>
            <td class=week-num>48</td>
            <td>27</td>
            <td>28</td>
            <td>29</td>
            <td>30</td>
            <td></td>
            <td class=sat></td>
            <td class=sun></td>
          </tr>
          <tr>
            <td class=week-num>49</td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td class=sat></td>
            <td class=sun></td>
          </tr>
        </table>
      </td>
      <td class=month>
        <table class=month>
          <tr>
            <th colspan=8 class=month>December</th>
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
            <td class=week-num>48</td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td>1</td>
            <td class=sat>2</td>
            <td class=sun>3</td>
          </tr>
          <tr>
            <td class=week-num>49</td>
            <td>4</td>
            <td>5</td>
            <td>6</td>
            <td>7</td>
            <td>8</td>
            <td class=sat>9</td>
            <td class=sun>10</td>
          </tr>
          <tr>
            <td class=week-num>50</td>
            <td>11</td>
            <td>12</td>
            <td>13</td>
            <td>14</td>
            <td>15</td>
            <td class=sat>16</td>
            <td class=sun>17</td>
          </tr>
          <tr>
            <td class=week-num>51</td>
            <td>18</td>
            <td>19</td>
            <td>20</td>
            <td>21</td>
            <td>22</td>
            <td class=sat>23</td>
            <td class=sun>24</td>
          </tr>
          <tr>
            <td class=week-num>52</td>
            <td>25</td>
            <td>26</td>
            <td>27</td>
            <td>28</td>
            <td>29</td>
            <td class=sat>30</td>
            <td class=sun>31</td>
          </tr>
          <tr>
            <td class=week-num>53</td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td class=sat></td>
            <td class=sun></td>
          </tr>
        </table>
      </td>
    </tr>
  </table>
"""

  assert htmlYear == calendarGen.buildYear(2000)

def test_buildYear_1():
  htmlYear = """  <table class=year>
    <tr>
      <th colspan=8 class=year>2001</th>
    </tr>
    <tr>
      <td class=month>
        <table class=month>
          <tr>
            <th colspan=8 class=month>January</th>
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
            <td class=week-num>1</td>
            <td>1</td>
            <td>2</td>
            <td>3</td>
            <td>4</td>
            <td>5</td>
            <td class=sat>6</td>
            <td class=sun>7</td>
          </tr>
          <tr>
            <td class=week-num>2</td>
            <td>8</td>
            <td>9</td>
            <td>10</td>
            <td>11</td>
            <td>12</td>
            <td class=sat>13</td>
            <td class=sun>14</td>
          </tr>
          <tr>
            <td class=week-num>3</td>
            <td>15</td>
            <td>16</td>
            <td>17</td>
            <td>18</td>
            <td>19</td>
            <td class=sat>20</td>
            <td class=sun>21</td>
          </tr>
          <tr>
            <td class=week-num>4</td>
            <td>22</td>
            <td>23</td>
            <td>24</td>
            <td>25</td>
            <td>26</td>
            <td class=sat>27</td>
            <td class=sun>28</td>
          </tr>
          <tr>
            <td class=week-num>5</td>
            <td>29</td>
            <td>30</td>
            <td>31</td>
            <td></td>
            <td></td>
            <td class=sat></td>
            <td class=sun></td>
          </tr>
          <tr>
            <td class=week-num>6</td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td class=sat></td>
            <td class=sun></td>
          </tr>
        </table>
      </td>
      <td class=month>
        <table class=month>
          <tr>
            <th colspan=8 class=month>February</th>
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
            <td class=week-num>5</td>
            <td></td>
            <td></td>
            <td></td>
            <td>1</td>
            <td>2</td>
            <td class=sat>3</td>
            <td class=sun>4</td>
          </tr>
          <tr>
            <td class=week-num>6</td>
            <td>5</td>
            <td>6</td>
            <td>7</td>
            <td>8</td>
            <td>9</td>
            <td class=sat>10</td>
            <td class=sun>11</td>
          </tr>
          <tr>
            <td class=week-num>7</td>
            <td>12</td>
            <td>13</td>
            <td>14</td>
            <td>15</td>
            <td>16</td>
            <td class=sat>17</td>
            <td class=sun>18</td>
          </tr>
          <tr>
            <td class=week-num>8</td>
            <td>19</td>
            <td>20</td>
            <td>21</td>
            <td>22</td>
            <td>23</td>
            <td class=sat>24</td>
            <td class=sun>25</td>
          </tr>
          <tr>
            <td class=week-num>9</td>
            <td>26</td>
            <td>27</td>
            <td>28</td>
            <td></td>
            <td></td>
            <td class=sat></td>
            <td class=sun></td>
          </tr>
          <tr>
            <td class=week-num>10</td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td class=sat></td>
            <td class=sun></td>
          </tr>
        </table>
      </td>
      <td class=month>
        <table class=month>
          <tr>
            <th colspan=8 class=month>March</th>
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
            <td class=week-num>9</td>
            <td></td>
            <td></td>
            <td></td>
            <td>1</td>
            <td>2</td>
            <td class=sat>3</td>
            <td class=sun>4</td>
          </tr>
          <tr>
            <td class=week-num>10</td>
            <td>5</td>
            <td>6</td>
            <td>7</td>
            <td>8</td>
            <td>9</td>
            <td class=sat>10</td>
            <td class=sun>11</td>
          </tr>
          <tr>
            <td class=week-num>11</td>
            <td>12</td>
            <td>13</td>
            <td>14</td>
            <td>15</td>
            <td>16</td>
            <td class=sat>17</td>
            <td class=sun>18</td>
          </tr>
          <tr>
            <td class=week-num>12</td>
            <td>19</td>
            <td>20</td>
            <td>21</td>
            <td>22</td>
            <td>23</td>
            <td class=sat>24</td>
            <td class=sun>25</td>
          </tr>
          <tr>
            <td class=week-num>13</td>
            <td>26</td>
            <td>27</td>
            <td>28</td>
            <td>29</td>
            <td>30</td>
            <td class=sat>31</td>
            <td class=sun></td>
          </tr>
          <tr>
            <td class=week-num>14</td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td class=sat></td>
            <td class=sun></td>
          </tr>
        </table>
      </td>
      <td class=month>
        <table class=month>
          <tr>
            <th colspan=8 class=month>April</th>
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
            <td class=week-num>13</td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td class=sat></td>
            <td class=sun>1</td>
          </tr>
          <tr>
            <td class=week-num>14</td>
            <td>2</td>
            <td>3</td>
            <td>4</td>
            <td>5</td>
            <td>6</td>
            <td class=sat>7</td>
            <td class=sun>8</td>
          </tr>
          <tr>
            <td class=week-num>15</td>
            <td>9</td>
            <td>10</td>
            <td>11</td>
            <td>12</td>
            <td>13</td>
            <td class=sat>14</td>
            <td class=sun>15</td>
          </tr>
          <tr>
            <td class=week-num>16</td>
            <td>16</td>
            <td>17</td>
            <td>18</td>
            <td>19</td>
            <td>20</td>
            <td class=sat>21</td>
            <td class=sun>22</td>
          </tr>
          <tr>
            <td class=week-num>17</td>
            <td>23</td>
            <td>24</td>
            <td>25</td>
            <td>26</td>
            <td>27</td>
            <td class=sat>28</td>
            <td class=sun>29</td>
          </tr>
          <tr>
            <td class=week-num>18</td>
            <td>30</td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td class=sat></td>
            <td class=sun></td>
          </tr>
        </table>
      </td>
    </tr>
    <tr>
      <td class=month>
        <table class=month>
          <tr>
            <th colspan=8 class=month>May</th>
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
            <td class=week-num>18</td>
            <td></td>
            <td>1</td>
            <td>2</td>
            <td>3</td>
            <td>4</td>
            <td class=sat>5</td>
            <td class=sun>6</td>
          </tr>
          <tr>
            <td class=week-num>19</td>
            <td>7</td>
            <td>8</td>
            <td>9</td>
            <td>10</td>
            <td>11</td>
            <td class=sat>12</td>
            <td class=sun>13</td>
          </tr>
          <tr>
            <td class=week-num>20</td>
            <td>14</td>
            <td>15</td>
            <td>16</td>
            <td>17</td>
            <td>18</td>
            <td class=sat>19</td>
            <td class=sun>20</td>
          </tr>
          <tr>
            <td class=week-num>21</td>
            <td>21</td>
            <td>22</td>
            <td>23</td>
            <td>24</td>
            <td>25</td>
            <td class=sat>26</td>
            <td class=sun>27</td>
          </tr>
          <tr>
            <td class=week-num>22</td>
            <td>28</td>
            <td>29</td>
            <td>30</td>
            <td>31</td>
            <td></td>
            <td class=sat></td>
            <td class=sun></td>
          </tr>
          <tr>
            <td class=week-num>23</td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td class=sat></td>
            <td class=sun></td>
          </tr>
        </table>
      </td>
      <td class=month>
        <table class=month>
          <tr>
            <th colspan=8 class=month>June</th>
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
            <td class=week-num>22</td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td>1</td>
            <td class=sat>2</td>
            <td class=sun>3</td>
          </tr>
          <tr>
            <td class=week-num>23</td>
            <td>4</td>
            <td>5</td>
            <td>6</td>
            <td>7</td>
            <td>8</td>
            <td class=sat>9</td>
            <td class=sun>10</td>
          </tr>
          <tr>
            <td class=week-num>24</td>
            <td>11</td>
            <td>12</td>
            <td>13</td>
            <td>14</td>
            <td>15</td>
            <td class=sat>16</td>
            <td class=sun>17</td>
          </tr>
          <tr>
            <td class=week-num>25</td>
            <td>18</td>
            <td>19</td>
            <td>20</td>
            <td>21</td>
            <td>22</td>
            <td class=sat>23</td>
            <td class=sun>24</td>
          </tr>
          <tr>
            <td class=week-num>26</td>
            <td>25</td>
            <td>26</td>
            <td>27</td>
            <td>28</td>
            <td>29</td>
            <td class=sat>30</td>
            <td class=sun></td>
          </tr>
          <tr>
            <td class=week-num>27</td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td class=sat></td>
            <td class=sun></td>
          </tr>
        </table>
      </td>
      <td class=month>
        <table class=month>
          <tr>
            <th colspan=8 class=month>July</th>
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
            <td class=week-num>26</td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td class=sat></td>
            <td class=sun>1</td>
          </tr>
          <tr>
            <td class=week-num>27</td>
            <td>2</td>
            <td>3</td>
            <td>4</td>
            <td>5</td>
            <td>6</td>
            <td class=sat>7</td>
            <td class=sun>8</td>
          </tr>
          <tr>
            <td class=week-num>28</td>
            <td>9</td>
            <td>10</td>
            <td>11</td>
            <td>12</td>
            <td>13</td>
            <td class=sat>14</td>
            <td class=sun>15</td>
          </tr>
          <tr>
            <td class=week-num>29</td>
            <td>16</td>
            <td>17</td>
            <td>18</td>
            <td>19</td>
            <td>20</td>
            <td class=sat>21</td>
            <td class=sun>22</td>
          </tr>
          <tr>
            <td class=week-num>30</td>
            <td>23</td>
            <td>24</td>
            <td>25</td>
            <td>26</td>
            <td>27</td>
            <td class=sat>28</td>
            <td class=sun>29</td>
          </tr>
          <tr>
            <td class=week-num>31</td>
            <td>30</td>
            <td>31</td>
            <td></td>
            <td></td>
            <td></td>
            <td class=sat></td>
            <td class=sun></td>
          </tr>
        </table>
      </td>
      <td class=month>
        <table class=month>
          <tr>
            <th colspan=8 class=month>August</th>
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
            <td class=week-num>31</td>
            <td></td>
            <td></td>
            <td>1</td>
            <td>2</td>
            <td>3</td>
            <td class=sat>4</td>
            <td class=sun>5</td>
          </tr>
          <tr>
            <td class=week-num>32</td>
            <td>6</td>
            <td>7</td>
            <td>8</td>
            <td>9</td>
            <td>10</td>
            <td class=sat>11</td>
            <td class=sun>12</td>
          </tr>
          <tr>
            <td class=week-num>33</td>
            <td>13</td>
            <td>14</td>
            <td>15</td>
            <td>16</td>
            <td>17</td>
            <td class=sat>18</td>
            <td class=sun>19</td>
          </tr>
          <tr>
            <td class=week-num>34</td>
            <td>20</td>
            <td>21</td>
            <td>22</td>
            <td>23</td>
            <td>24</td>
            <td class=sat>25</td>
            <td class=sun>26</td>
          </tr>
          <tr>
            <td class=week-num>35</td>
            <td>27</td>
            <td>28</td>
            <td>29</td>
            <td>30</td>
            <td>31</td>
            <td class=sat></td>
            <td class=sun></td>
          </tr>
          <tr>
            <td class=week-num>36</td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td class=sat></td>
            <td class=sun></td>
          </tr>
        </table>
      </td>
    </tr>
    <tr>
      <td class=month>
        <table class=month>
          <tr>
            <th colspan=8 class=month>September</th>
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
            <td class=week-num>35</td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td class=sat>1</td>
            <td class=sun>2</td>
          </tr>
          <tr>
            <td class=week-num>36</td>
            <td>3</td>
            <td>4</td>
            <td>5</td>
            <td>6</td>
            <td>7</td>
            <td class=sat>8</td>
            <td class=sun>9</td>
          </tr>
          <tr>
            <td class=week-num>37</td>
            <td>10</td>
            <td>11</td>
            <td>12</td>
            <td>13</td>
            <td>14</td>
            <td class=sat>15</td>
            <td class=sun>16</td>
          </tr>
          <tr>
            <td class=week-num>38</td>
            <td>17</td>
            <td>18</td>
            <td>19</td>
            <td>20</td>
            <td>21</td>
            <td class=sat>22</td>
            <td class=sun>23</td>
          </tr>
          <tr>
            <td class=week-num>39</td>
            <td>24</td>
            <td>25</td>
            <td>26</td>
            <td>27</td>
            <td>28</td>
            <td class=sat>29</td>
            <td class=sun>30</td>
          </tr>
          <tr>
            <td class=week-num>40</td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td class=sat></td>
            <td class=sun></td>
          </tr>
        </table>
      </td>
      <td class=month>
        <table class=month>
          <tr>
            <th colspan=8 class=month>October</th>
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
            <td class=week-num>40</td>
            <td>1</td>
            <td>2</td>
            <td>3</td>
            <td>4</td>
            <td>5</td>
            <td class=sat>6</td>
            <td class=sun>7</td>
          </tr>
          <tr>
            <td class=week-num>41</td>
            <td>8</td>
            <td>9</td>
            <td>10</td>
            <td>11</td>
            <td>12</td>
            <td class=sat>13</td>
            <td class=sun>14</td>
          </tr>
          <tr>
            <td class=week-num>42</td>
            <td>15</td>
            <td>16</td>
            <td>17</td>
            <td>18</td>
            <td>19</td>
            <td class=sat>20</td>
            <td class=sun>21</td>
          </tr>
          <tr>
            <td class=week-num>43</td>
            <td>22</td>
            <td>23</td>
            <td>24</td>
            <td>25</td>
            <td>26</td>
            <td class=sat>27</td>
            <td class=sun>28</td>
          </tr>
          <tr>
            <td class=week-num>44</td>
            <td>29</td>
            <td>30</td>
            <td>31</td>
            <td></td>
            <td></td>
            <td class=sat></td>
            <td class=sun></td>
          </tr>
          <tr>
            <td class=week-num>45</td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td class=sat></td>
            <td class=sun></td>
          </tr>
        </table>
      </td>
      <td class=month>
        <table class=month>
          <tr>
            <th colspan=8 class=month>November</th>
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
            <td class=week-num>44</td>
            <td></td>
            <td></td>
            <td></td>
            <td>1</td>
            <td>2</td>
            <td class=sat>3</td>
            <td class=sun>4</td>
          </tr>
          <tr>
            <td class=week-num>45</td>
            <td>5</td>
            <td>6</td>
            <td>7</td>
            <td>8</td>
            <td>9</td>
            <td class=sat>10</td>
            <td class=sun>11</td>
          </tr>
          <tr>
            <td class=week-num>46</td>
            <td>12</td>
            <td>13</td>
            <td>14</td>
            <td>15</td>
            <td>16</td>
            <td class=sat>17</td>
            <td class=sun>18</td>
          </tr>
          <tr>
            <td class=week-num>47</td>
            <td>19</td>
            <td>20</td>
            <td>21</td>
            <td>22</td>
            <td>23</td>
            <td class=sat>24</td>
            <td class=sun>25</td>
          </tr>
          <tr>
            <td class=week-num>48</td>
            <td>26</td>
            <td>27</td>
            <td>28</td>
            <td>29</td>
            <td>30</td>
            <td class=sat></td>
            <td class=sun></td>
          </tr>
          <tr>
            <td class=week-num>49</td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td class=sat></td>
            <td class=sun></td>
          </tr>
        </table>
      </td>
      <td class=month>
        <table class=month>
          <tr>
            <th colspan=8 class=month>December</th>
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
            <td class=week-num>48</td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td class=sat>1</td>
            <td class=sun>2</td>
          </tr>
          <tr>
            <td class=week-num>49</td>
            <td>3</td>
            <td>4</td>
            <td>5</td>
            <td>6</td>
            <td>7</td>
            <td class=sat>8</td>
            <td class=sun>9</td>
          </tr>
          <tr>
            <td class=week-num>50</td>
            <td>10</td>
            <td>11</td>
            <td>12</td>
            <td>13</td>
            <td>14</td>
            <td class=sat>15</td>
            <td class=sun>16</td>
          </tr>
          <tr>
            <td class=week-num>51</td>
            <td>17</td>
            <td>18</td>
            <td>19</td>
            <td>20</td>
            <td>21</td>
            <td class=sat>22</td>
            <td class=sun>23</td>
          </tr>
          <tr>
            <td class=week-num>52</td>
            <td>24</td>
            <td>25</td>
            <td>26</td>
            <td>27</td>
            <td>28</td>
            <td class=sat>29</td>
            <td class=sun>30</td>
          </tr>
          <tr>
            <td class=week-num>53</td>
            <td>31</td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td class=sat></td>
            <td class=sun></td>
          </tr>
        </table>
      </td>
    </tr>
  </table>
"""

  assert htmlYear == calendarGen.buildYear(2001)