def _iter_loaders(self, template):
        loader = self.app.jinja_loader
        if loader is not None:
            yield self.app, loader

from flask import Flask, render_template, request

import pandas as pd

from alpha_vantage.timeseries import TimeSeries
import matplotlib.pyplot as plt
import sys



app = Flask("Final_Project")
app.debug = True

@app.route("/numbers", methods=["POST"])
def stockchart():

    print "inside stockchart"
    symbol = request.form.get("symbol")
    print symbol

    ts = TimeSeries(key='your_key', output_format='pandas')
    data, meta_data = ts.get_intraday(symbol=symbol,interval='1day', outputsize='full')
    data['close'].plot()
    plt.title('1 day performance of {} stock').format(symbol)
    plt.show()
    print data
    print meta_datae
    symbol=input("Pick a Tech Stock of Your interest:")
    stockchart(symbol)
    return "selected Symbol" + symbol

@app.route("/")
def dropdown():
    symbol_list = ["GOOGL","MSFT","IBM", "AAPL"]
    return render_template("index.html", symbol_list=symbol_list)


if __name__ == "__main__":
    app.run()
