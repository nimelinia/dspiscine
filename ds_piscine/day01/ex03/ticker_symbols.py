import sys

def ticker_symbols():
    companies =    {'Apple' : 'AAPL',
                    'Microsoft' : 'MSFT',
                    'Netflix' : 'NFLX',
                    'Tesla' : 'TSLA',
                    'Nokia' : 'NOK'
                    }
    stocks =       {'AAPL' : 287.73,
                    'MSFT' : 173.79,
                    'NFLX' : 416.90,
                    'TSLA' : 724.88,
                    'NOK' : 3.37
                    }
    if len(sys.argv) != 2:
        return
    else:
        if sys.argv[1].upper() not in stocks:
            print('Unknown ticker')
        else:
            for i in companies.items():
                if i[1] == sys.argv[1].upper():
                    print(i[0], end=' ')
            print(stocks[sys.argv[1].upper()])


if __name__ == '__main__':
    ticker_symbols()