import requests

try:
    res =  requests.get('https://automatetheboringstuff.com/files/rj.txt')
    print(res.status_code)
    res.raise_for_status()

    with open('romeo.txt', 'wb') as playfile:
        for chunk in res.iter_content(100000):
            playfile.write(chunk)

except Exception as e:
    print(e)


