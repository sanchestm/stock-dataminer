from  yahoo_finance_dictionary import *
from company_symbols import *
import pandas as pd
import urllib
import io
from time import gmtime, strftime
import time

# example of finding index df[df.index == "Apple Inc."] || a.

def quotes(stuff = AllAPIdict, companies = company_symbols):
    site_sufix = "n"
    for i in stuff: site_sufix += i
    site_prefix = ""
    for i in companies: site_prefix += i+ "+"
    File = urllib.request.urlopen(basename+ site_prefix[:-1]+ glue+ site_sufix)
    head = ["Name"]+[APIdict[x] for x in stuff]
    table = pd.read_csv(io.TextIOWrapper(File), names = head, header=None)
    table =table.set_index(table.Name)
    table = table.drop("Name", 1)
    table = table.dropna(axis ="index", how = "all")
    table = table.dropna(axis ="columns", how = "all")
    table = table.fillna(value = "0")
    table["timeGMT"] = strftime("%H:%M:%S", gmtime())
    table["time"] = strftime("%Y-%m-%d %H:%M:%S")
    return table

def sortDF(df, col, ascend = False ):
    return df.sort_values(by=[col], ascending = ascend)
