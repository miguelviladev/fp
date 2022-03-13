# Constantes para indexar os tuplos:
NAME,DATE,OPEN,MAX,MIN,CLOSE,VOLUME = 0,1,2,3,4,5,6

def main():
    lst = loadStockFile("nasdaq.csv")

    print("First:", lst[1])
    print(" Last:", lst[-1])
    
    print("a) totVol=", totalVolume(lst))

    print("b) maxVal=", maxValorization(lst))
    
    stocksDic = stocksByDateByName(lst)
    print("c) CSCO@11:", stocksDic['2020-10-12']['CSCO'])
    print("c) AMZN@22:", stocksDic['2020-10-22']['AMZN'])

    port = {'NFLX': 100, 'CSCO': 80}
    portfolioValue(stocksDic, port, "2020-10-01")
    print("d) portfolio@01:", portfolioValue(stocksDic, port, "2020-10-01"))
    print("d) portfolio@30:", portfolioValue(stocksDic, port, "2020-10-30"))

def loadStockFile(filename):
    lst = []
    with open(filename) as f:
        for line in f:
            parts = line.strip().split('\t')
            name = parts[NAME]
            date = parts[DATE]
            tup = (name, date, float(parts[OPEN]), float(parts[MAX]),
                float(parts[MIN]), float(parts[CLOSE]), int(parts[VOLUME]))
            lst.append(tup)
    return lst

def totalVolume(lst):
    totVol = {}
    for stock_record in lst:
        totVol[stock_record[NAME]] = totVol.get(stock_record[NAME], 0) + stock_record[VOLUME]
    return totVol

def calValorization(open_val, close_val):
    return ((close_val*100)/open_val)-100

def maxValorization(lst):
    vMax = {}
    for stock_record in lst:
        valorization = calValorization(stock_record[OPEN],stock_record[CLOSE])
        if stock_record[DATE] in vMax:
            if vMax[stock_record[DATE]][1] < valorization:
                vMax[stock_record[DATE]] = (stock_record[NAME], valorization)
        else:
            vMax[stock_record[DATE]] = (stock_record[NAME], valorization)
    return vMax

def stocksByDateByName(lst):
    dic = {}
    for stock_record in lst:
        dic[stock_record[DATE]] = {}
    for stock_record in lst:
        dic[stock_record[DATE]][stock_record[NAME]] = (stock_record[OPEN],stock_record[MAX],stock_record[MIN],stock_record[CLOSE],stock_record[VOLUME])
    return dic

def portfolioValue(stocks, portfolio, date):
    assert date in stocks
    val = 0.0
    for stock in portfolio:
        quantity = portfolio[stock]
        close_val= stocks[date][stock][3]
        val += quantity*close_val
    return val

if __name__ == "__main__":
    main()