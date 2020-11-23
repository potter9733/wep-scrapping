import requests
from bs4 import BeautifulSoup


def extract_link_and_company():
    url = "https://www.alba.co.kr"
    
    result = requests.get(url)
    soup = BeautifulSoup(result.text, 'html.parser')
    extract = soup.find('div', {'id': 'MainSuperBrand'}).find_all('a', {'class':'goodsBox-info'})
    
    link_and_company = [ [0, 0] for _ in range(len(extract))]
    
    for i in range(len(extract)):
        link_and_company[i][0] = extract[i].attrs['href']
        link_and_company[i][1] = extract[i].find('span',{'class':'company'}).get_text()

    return link_and_company


def is_none(a):
    if a != None:
        return a.get_text().strip('\xa0')
    else:
        return 'None'


def job_info(arr):
    
    job_info = [ [0,0,0,0,0,0] for _ in range(len(arr)) ]
    for i in range(len(arr)):
            
        job_info[i][0] = arr[i][1]
        url = arr[i][0]
        print(f'{arr[i][1]}, page {i+1}/{len(arr)}')
        result = requests.get(url)
        soup = BeautifulSoup(result.text, 'html.parser')
        
        extract = soup.find('div', {'class': 'goodsJob'}).find_all('tr')
        
        extract = extract[1::2]
        
        place, title, time, pay, date = [], [], [], [], []
        
        for j in range(len(extract)):
            place.append(is_none(extract[j].find('td', {'class' : 'local first'})))
            title.append(is_none(extract[j].find('span', {'class' : 'company'})))
            time.append(is_none(extract[j].find('span', {'class' : 'time'})))
            pay.append(is_none(extract[j].find('span', {'class' : 'number'})))
            date.append(is_none(extract[j].find('td',{'class' : 'regDate last'})))
    
        job_info[i][1] = place
        job_info[i][2] = title
        job_info[i][3] = time
        job_info[i][4] = pay
        job_info[i][5] = date

    return job_info


def save_to_file(arr):
    import csv
    for j in range(len(arr)):
        file = open(f'{arr[j][0]}.csv', mode='w',buffering = -1, encoding ='utf-8')
        writer = csv.writer(file)
        writer.writerow(['place', 'title', 'time', 'pay', 'date'])
        for k in range(len(arr[j][1])):
            writer.writerow([arr[j][1][k], arr[j][2][k], arr[j][3][k], arr[j][4][k], arr[j][5][k]])
    return

result = job_info(extract_link_and_company())
save_to_file(result)