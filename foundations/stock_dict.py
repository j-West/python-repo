

purchases = [ ( 'GM', 100, '10-sep-2001', 48 ),
              ( 'CAT', 100, '1-apr-1999', 24 ),
              ( 'GM', 200, '1-jul-1998', 56 ),
              ( 'APPL', 300, '2-aug-2002', 46)]


def get_stock_name(symbol):
    """
    Function takes a symbol as args which is compared against the keys of a dict.  If a match is found the corresponding company name is returned
    """
    stock_dict = {'GM': 'General Motors',
                  'CAT': 'Caterpillar',
                  'APPL': 'Apple'
                 }

    for k, v in stock_dict.items():
        if symbol == k:
            return v



def detailed_history_report():
    """
    Function prints a string containing full purchase price, company name, and date of purchase
    """
    for purchase in purchases:
        print('${} of {} stock was bought on {}.'.format(purchase[1] * purchase[3], get_stock_name(purchase[0]), purchase[2]))

def full_history_report():
    """
    Function creates a new dict and prints it after iterating over each purchase in purchases.
    """

    full_report = dict()
    for purchase in purchases:
        if purchase[0] in full_report:
            full_report[purchase[0]] += purchase[1] * purchase[3]
        else:
            full_report[purchase[0]] = purchase[1] * purchase[3]

    print(full_report)




detailed_history_report()
full_history_report()
