# for knowing more on the YAHOO finance API visit http://www.jarloo.com/yahoo_finance/
# yahoo finance package for python https://pypi.python.org/pypi/yahoo-finance
# pandas package for yahoo finance http://pandas.pydata.org/pandas-docs/version/0.16.2/remote_data.html#yahoo-finance
#getting all  comapnie names http://query.yahooapis.com/v1/public/yql?q=select%20
#*%20from%20yahoo.finance.industry%20where%20id%20in%20(select%20industry.id%20from%
#20yahoo.finance.sectors)&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys
import pandas as  pd
basename  = "http://finance.yahoo.com/d/quotes.csv?s="
glue = "&f="

APIdict = {
"n":  "Name",
"a":  "Ask",
"y":  "Dividend Yield",
"b":  "Bid",
"d":  "Dividend per Share",
"b2": "Ask (Realtime)",
"r1": "Dividend Pay Date",
"b3": "Bid (Realtime)",
"q":  "Ex-Dividend Date",
"p":  "Previous Close",
"o":  "Open",
"c1": "Change",
"d1": "Last Trade Date",
"c":  "Change & Percent Change",
"d2": "Trade Date",
"c6": "Change (Realtime)",
"t1": "Last Trade Time",
"k2": "Change Percent (Realtime)",
"p2": "Change in Percent",
"c8": "After Hours Change (Realtime)",
"m5": "Change From 200 Day Moving Average",
"c3": "Commission",
"m6": "Percent Change From 200 Day Moving Average",
"g" :  "Day’s Low",
"m7": "Change From 50 Day Moving Average",
"h" :  "Day’s High",
"m8": "Percent Change From 50 Day Moving Average",
"k1": "Last Trade (Realtime) With Time",
"m3": "50 Day Moving Average",
"l" :  "Last Trade (With Time)",
"m4": "200 Day Moving Average",
"l1": "Last Trade (Price Only)",
"t8": "1 yr Target Price",
"w1": "Day’s Value Change",
"g1": "Holdings Gain Percent",
"w4": "Day’s Value Change (Realtime)",
"g3": "Annualized Gain",
"p1": "Price Paid",
"g4": "Holdings Gain",
"m" :  "Day’s Range",
"g5": "Holdings Gain Percent (Realtime)",
"m2": "Day’s Range (Realtime)",
"g6": "Holdings Gain (Realtime)",
"k" :  "52 Week High",
"i" :  "More Info",
"j" :  "52 week Low",
"j1": "Market Capitalization",
"j5": "Change From 52 Week Low",
"j3": "Market Cap (Realtime)",
"k4": "Change From 52 week High",
"f6": "Float Shares",
"j6": "Percent Change From 52 week Low",
"k5": "Percent Change From 52 week High",
"n4": "Notes",
"w" :  "52 week Range",
"s" :  "Symbol",
"s1": "Shares Owned",
"x" :  "Stock Exchange",
"j2": "Shares Outstanding",
"v" :  "Volume",
"a5": "Ask Size",
"b6": "Bid Size",
"k3": "Last Trade Size",
"t7": "Ticker Trend",
"a2": "Average Daily Volume",
"t6": "Trade Links",
"i5": "Order Book (Realtime)",
"l2": "High Limit",
"e" :  "Earnings per Share",
"l3": "Low Limit",
"e7": "EPS Estimate Current Year",
"v1": "Holdings Value",
"e8": "EPS Estimate Next Year",
"v7": "Holdings Value (Realtime)",
"e9": "EPS Estimate Next Quarter",
"s6": "Revenue",
"b4": "Book Value",
"j4": "EBITDA",
"p5": "Price/Sales",
"p6": "Price/Book",
"r" : "P/E Ratio",
"r2": "P/E Ratio (Realtime)",
"r5": "PEG Ratio",
"r6": "Price/EPS Estimate Current Year",
"r7": "Price/EPS Estimate Next Year",
"s7": "Short Ratio"}

AllAPIdict = []
for i in APIdict:
    if i != "n":AllAPIdict += [i]

AllNASDAQ = pd.read_csv("NASDAQsym.csv")
AllNASDAQsymbols = AllNASDAQ["Symbol"].values.tolist()

#def get_csv(stuff = "nab", companies = company_symbols):
#    pass
