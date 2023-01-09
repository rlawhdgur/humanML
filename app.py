import requests
from bs4 import BeautifulSoup

def crawling(soup):
  result = []

  div = soup.find('div', class_ = 'best-list')
  print(div)

  for a in div.find_all('a', class_ = 'itemname'):
    # print(a.get_text())
    result.append(a.get_text())
  return result


def main():
  coustom_header = {
      'referer' : 'https://www.gmarket.co.kr/',
      'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
                      (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
  }
  url = 'https://corners.gmarket.co.kr/Bestsellers'
  req = requests.get(url, headers = coustom_header)
  # print(req.status_code)
  # print(req.text)

  soup = BeautifulSoup(req.text, "html.parser")
  result = crawling(soup)
  print(result)



if __name__ == "__main__":
  main()
