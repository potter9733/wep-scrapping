import requests
from bs4 import BeautifulSoup

result = requests.get('https://www.iban.com/currency-codes')
soup = BeautifulSoup(result.text, 'html.parser')
arr = soup.find('table', {'class': 'table'}).find_all('td')

for i in range(len(arr)):
    arr[i] = arr[i].get_text()
    
for i in range(len(arr)):    
    if arr[i] == 'No universal currency':
        arr[i-1],arr[i]= '',''
        
arr = list(filter(None, arr))

print('Hello! Please choose select a country by numeber:')
data = []
for i, nat in enumerate(arr[::4]):
    data.append([arr[4 * i], arr[4 * i + 2]])
    print(f'# {i} {nat}')

while True:
    try:
        n = int(input('#: '))
        if 0 <= n <= i:
            break
        else:
            raise TypeError
    except ValueError:
        print("That wasn't a number.")
    except TypeError:
        print('Choose a number from the list.')
 
print(f'You chose {data[n][0]}')
print(f'The currency code is {data[n][1]}')
    