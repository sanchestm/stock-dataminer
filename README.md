# stock-dataminer
Get quotes from stocks (yahoo finance) to python pandas table

using the program:
  - import `stock_eval.py` in your python code with
  ```
  import stock_eval as stocks
  ```

there are curently 2 functions in `stock_eval.py`:
- quotes()
- sortDF()

The `quotes()` function requires 2 paramentes `stuff` and `companies` and returns a pandas Dataframe with all the parameters you want (check `yahoo_finance_dictionary` to see what it`s able to download) from all the companies symbols given in companies. In both parameters use a list of strings.

`quotes()` examples:
```
>>> import stock_eval as stocks
>>> test = stocks.quotes(stuff = [`a`,`b`], companies = [`AAPL`,`GOOG`, `YHOO`]) #get ask and bid from Apple, Google and Yahoo
>>> test2 = stocks.quotes() # gets all the possible information from the list of companies given in company_symbols.py
>>> test
                  Ask     Bid   timeGMT                 time
Name                                                        
Apple Inc.     112.23  112.22  14:25:34  2016-09-25 11:25:34
Alphabet Inc.  787.31  786.01  14:25:34  2016-09-25 11:25:34
Yahoo! Inc.     42.79   42.70  14:25:34  2016-09-25 11:25:34
```

The `sortDF()` function has 3 parameters: the Dataframe you want to sort, the parameter you want your Dataframe sorted by and the type of sorting you desire (default is descending).

`sortDF` examples:

```
>>> sortedTest = stocks.sortDF(test, `Ask`)
>>> sortedTest
                  Ask     Bid   timeGMT                 time
Name                                                        
Alphabet Inc.  787.31  786.01  14:44:25  2016-09-25 11:44:25
Apple Inc.     112.23  112.22  14:44:25  2016-09-25 11:44:25
Yahoo! Inc.     42.79   42.70  14:44:25  2016-09-25 11:44:25

>>> sortedTest2 = stocks.sortDF(test, `Bid`, True)
>>> sortedTest2
                  Ask     Bid   timeGMT                 time
Name                                                        
Yahoo! Inc.     42.79   42.70  14:44:25  2016-09-25 11:44:25
Apple Inc.     112.23  112.22  14:44:25  2016-09-25 11:44:25
Alphabet Inc.  787.31  786.01  14:44:25  2016-09-25 11:44:25

```
