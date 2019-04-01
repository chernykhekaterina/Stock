from flask import Flask, render_template, request

import pandas as pd

from alpha_vantage.timeseries import TimeSeries
import matplotlib.pyplot as plt
import sys

def _iter_loaders(self, template):
        loader = self.app.jinja_loader
        if loader is not None:
            yield self.app, loader
app = Flask("Final_Project")
app.debug = True

@app.route("/numbers", methods=["POST"])
def stockchart():

    print "inside stockchart"
    select = request.form.get("symbol")
    print select

    ts = TimeSeries(key='your_key', output_format='pandas')
    data, meta_data = ts.get_intraday(symbol=symbol,interval='1day', outputsize='full')
    data['close'].plot()
    plt.title('1 day performance of {} stock').format(symbol)
    plt.show()

    symbol=input("Pick a Tech Stock of Your interest:")
    stockchart(symbol)
    return "selected Symbol" + select

@app.route("/")
def dropdown():
    symbol_list = ["GOOGL","MSFT","IBM", "AAPL"]
    return render_template("index.html", symbol_list="symbol_list")




#change raw input to smth else so that choice is in html rather than in terminal
if __name__ == "__main__":
    app.run()

#Please enter sector of interest to get S&P performance - limit it to a list that define in html
