import os
import requests
import urllib
from dotenv import load_dotenv
import argparse

def ShortenLink(token, url):
  headers = {
    "Authorization": f"Bearer {token}"
  }

  payload = {
    "long_url": url
  }

  url = "https://api-ssl.bitly.com/v4/bitlinks"

  response = requests.post(url, headers=headers, json=payload)
  response.raise_for_status()

  return response.json()["id"]


def CountClicks(token, url):
  headers = {
    "Authorization": f"Bearer {token}"
  }

  payload = {
    "unit": "day"
  }

  parsed = urllib.parse.urlparse(url)

  url = f"https://api-ssl.bitly.com/v4/bitlinks/{parsed.netloc}{parsed.path}/clicks/summary"
  response = requests.get(url, headers=headers, params=payload)
  response.raise_for_status()

  clicks_count = response.json()["total_clicks"]

  return clicks_count


def IsBitlink(token, url):
  headers = {
    "Authorization": f"Bearer {token}"
  }

  parsed = urllib.parse.urlparse(url)

  url = f"https://api-ssl.bitly.com/v4/bitlinks/{parsed.netloc}{parsed.path}"

  response = requests.get(url, headers=headers)
  return response.ok


def CreateParser():
  parser = argparse.ArgumentParser()
  parser.add_argument("name")

  return parser


def main():
  load_dotenv()
  bitly_token = os.environ["BITLY_OAUTHACCESSTOKEN"]

  parser = CreateParser()
  args = parser.parse_args()

  source_url = args.name

  try:
    if IsBitlink(bitly_token, source_url):
      print("Количество переходов по ссылке битли", CountClicks(bitly_token, source_url))
    else:
      shortened_link = ShortenLink(bitly_token, source_url)
      print(shortened_link)
  except requests.exceptions.HTTPError:
    print("Ссылка введена неверно")


if __name__ == "__main__":
  main()