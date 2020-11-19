import requests
#import os

def change_to_url(urls):
    for i in range(len(urls)):
        if '.com' not in urls[i]:
            print(f'{urls[i]} is not a valid URL')
            return -1
        
        if 'http://' in urls[i]:
            urls[i] = urls[i].lower().strip()
        else:
            urls[i] = 'http://'+ urls[i].lower().strip()
        
    return urls    

def requests_url(urls):
    for url in urls:
        try:
            requests.get(url)
            print(f'{url} is up!')
        except:
            print(f'{url} is down!')

def keep_going():
    while True:
        print('Do you want to start over? [y/n]', end=' ')
        answer = input()
        if answer == 'y':
            # os.system('clear')
            # print('Welcome!')
            # print('Please write a URL or URLs you want to check. (separated by comma)')
            return 1
            break
        elif answer == 'n':
            print('k.bye')
            break
        else:
            print('That not a valid answer')
        
def start():
    print('Welcome!')
    print('Please write a URL or URLs you want to check. (separated by comma)')
    while True:
        while True:
            urls = change_to_url(input().split(','))
            if urls == -1:
                break
            else:
                requests_url(urls)
                break
        
        if keep_going() != 1:
            break

start()
