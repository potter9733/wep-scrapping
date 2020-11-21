# import os
import requests
from bs4 import BeautifulSoup
from babel.numbers import format_currency
# os.system("clear")
url = "https://www.iban.com/currency-codes"

result = requests.get(url)
soup = BeautifulSoup(result.text, 'html.parser')
arr = soup.find('table', {'class': 'table'}).find_all('td')

for i in range(len(arr)):
    arr[i] = arr[i].get_text()
    
for i in range(len(arr)):    
    if arr[i] == 'No universal currency':
        arr[i-1],arr[i]= '',''
        
arr = list(filter(None, arr))


def transfer(nat_1, nat_2, amount):
    url = f'https://transferwise.com/gb/currency-converter/{nat_1}-to-{nat_2}-rate?amount={amount}'
    result = requests.get(url)
    soup = BeautifulSoup(result.text, 'html.parser')
    money = soup.find('span', {'class': 'text-success'}).get_text()
    money = float(money) * amount
    money = format_currency(money, nat_2, locale="ko_KR")
    print(f'{nat_1}{amount} is {money}')

print('Where are you from? Choose a country by number.')

#print('Hello! Please choose select a country by numeber:')
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

# print(f'You chose {data[n][0]}')
# print(f'The currency code is {data[n][1]}')
nat_1 = data[n][1]
print(f'{data[n][0]}')
print()
print('Now choose another country.')

while True:
    try:
        m = int(input('#: '))
        if 0 <= m <= i:
            break
        else:
            raise TypeError
    except ValueError:
        print("That wasn't a number.")
    except TypeError:
        print('Choose a number from the list.')
        
nat_2 = data[m][1]
print(f'{data[m][0]}')


while True:
    print(f'How many {data[n][1]} do you want to convert to {data[m][1]}?')
    
    try:
        l = int(input())
        break
    except:
        print("That wasn't a number.")
        
transfer(nat_1, nat_2, l)