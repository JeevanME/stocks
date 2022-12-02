
// Python Visual Display using Data Frames
/*
This code runs in a Zepl notebook.  We will publish the SHARE to the notebook when the US_Stocks database is available in the Snowflake Data Marketplace
*/
See Data Output (PDF)

http://cdn-north-america.s3.amazonaws.com/Example_of_US_Stocks%20Visualization_Zepl_Data_Marketplace_Stocks_Database.pdf

Notebook:
https://www.zepl.com/viewer/notebooks/bm90ZTovL2dyb3ZlckB6ZXBsLmNvbS8zMTg2ZWZmMzI0N2I0ZjE4OGY5YTFkZjRkYzY1NzdmOS9ub3RlLmpzb24

/// NOTEBOOK CODE EXAMPLE - PYTHON3 INTERPRETER

connect = z.getDatasource("Stocks")

import pandas as pd
res = connect.execute(f"select * from stock_history where symbol='{symbol}' and date > '2020-01-01' order by date")
data = pd.DataFrame(res)
data.columns = [f"{symbol}_"+item[0] if item[0]!="DATE" else "DATE" for item in res.description]

z.show(data)

symbol1 = "SPY"
res = connect.execute(f"select * from stock_history where symbol='{symbol1}' and date > '2020-01-01' order by date")
data1 = pd.DataFrame(res)
data1.columns = [f"{symbol1}_"+item[0] if item[0]!="DATE" else "DATE" for item in res.description]

joined_result = pd.merge(data, data1, on='DATE')
