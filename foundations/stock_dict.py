

purchases = [ ( 'GM', 100, '10-sep-2001', 48 ),
              ( 'CAT', 100, '1-apr-1999', 24 ),
              ( 'GM', 200, '1-jul-1998', 56 ),
              ( 'APPL', 300, '2-aug-2002', 46)]


def get_stock_name(symbol):
    stock_dict = {'GM': 'General Motors',
                  'CAT': 'Caterpillar',
                  'APPL': 'Apple'
                 }

    for k, v in stock_dict.items():
        if symbol == k:
            return v
