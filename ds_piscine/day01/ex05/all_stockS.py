import sys
def dic_comp():
    companies = {'Apple': 'AAPL',
                 'Microsoft': 'MSFT',
                 'Netflix': 'NFLX',
                 'Tesla': 'TSLA',
                 'Nokia': 'NOK'
                 }
    low_comp = { k.lower() : companies[k] for k in companies.keys()}
    return low_comp


def dic_stocks():
    stocks = {'AAPL': 287.73,
              'MSFT': 173.79,
              'NFLX': 416.90,
              'TSLA': 724.88,
              'NOK': 3.37
              }
    return stocks


def find_comp_by_ticker(query, companies):
    for i in companies.items():
        if i[1] == query:
            return i[0].capitalize()


def print_info(query, stocks, companies):
    if query.upper() not in stocks and query.lower() not in companies:
        print(f'{query} is an unknown company or an unknown ticker symbol')
    elif query.lower() in companies:
        print(f'{query.capitalize()} stock price is {stocks[companies[query.lower()]]}')
    else:
        print(f'{query} is a ticker symbol for {find_comp_by_ticker(query.upper(), companies)}')



def all_stocks():
    stocks = dic_stocks()
    companies = dic_comp()
    if len(sys.argv) != 2:
        return
    lst_of_query_r = sys.argv[1].split(',')
    lst_of_query = []
    for query in lst_of_query_r:
        query = query.strip(' ')
        if len(query) == 0:
            print()
            return
        lst_of_query.append(query)
    for query in lst_of_query:
        print_info(query, stocks, companies)


if __name__ == '__main__':
    all_stocks()