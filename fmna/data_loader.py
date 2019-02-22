from yahoo_quote_download import yqd

def add_suffix(l, suffix):
    return list(map(lambda s: '%s.%s' % (s, suffix), l))

def load_data(tickers, start, end):
    x = {}
    for idx, t in enumerate(tickers):
        try:
            prices = yqd.load_yahoo_quote(t, start, end)
            for row in prices[1:]:
                if len(row) > 0:
                    s = row.split(",")
                    date = s[0]
                    adj_close = float(s[5])
                    if not date in x.keys():
                        x[date] = [-1] * len(tickers)
                    x[date][idx] = adj_close
        except(BaseException):
            print("Can't find %s!" % t)
    return x

def yields(prices):
    num_dates = len(prices.keys())
