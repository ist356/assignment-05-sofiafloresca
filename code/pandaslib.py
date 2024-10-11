from datetime import datetime

def clean_currency(item: str) -> float:
    '''
    remove anything from the item that prevents it from being converted to a float
    '''    
    newitem = item.replace('$', '')
    newitem = newitem.replace(',', '')
    newitem = float(newitem)
    return newitem

def extract_year_mdy(timestamp):
    '''
    use the datatime.strptime to parse the date and then extract the year
    '''

    date = datetime.strptime(timestamp, '%m/%d/%Y %H:%M:%S')
    year = date.year
    return year

def clean_country_usa(item: str) ->str:
    '''
    This function should replace any combination of 'United States of America', USA' etc.
    with 'United States'
    '''
    possibilities = [
        'united states of america', 'usa', 'us', 'united states', 'u.s.'
    ]
    for possibility in possibilities:
        if possibility in item.lower():
            return 'United States'


if __name__=='__main__':
    print("""
        Add code here if you need to test your functions
        comment out the code below this like before sumbitting
        to improve your code similarity score.""")
    '''print(clean_currency('$3,000'))
    print(extract_year_mdy('12/31/2020'))
    print(clean_country_usa('United States of America'))'''

