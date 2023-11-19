import requests
from datetime import datetime as dt


def request_day():
    r = requests.post('http://localhost:5000/get_day',
                      json={'day': dt.now().strftime("%Y-%m-%d")})
    if r.status_code == 200:
        print(f"answer from  query day: {r.json()['answer']}")
    else:
        print(r.text)


def request_like():
    r = requests.post('http://localhost:5000/get_like',
                      json={'word': "Чиновник"})
    if r.status_code == 200:
        print(f"answer from like query: {r.json()['answer']}")
    else:
        print(r.text)


def main():
    request_like()
    request_day()


if __name__ == '__main__':
    main()
