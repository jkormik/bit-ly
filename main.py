import os
import requests
import urllib
from dotenv import load_dotenv
import argparse


def shorten_link(token, url):
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


def count_clicks(token, url):
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


def is_bitlink(token, url):
  headers = {
    "Authorization": f"Bearer {token}"
  }

  parsed = urllib.parse.urlparse(url)

  url = f"https://api-ssl.bitly.com/v4/bitlinks/{parsed.netloc}{parsed.path}"

  response = requests.get(url, headers=headers)
  return response.ok


def create_parser():
  parser = argparse.ArgumentParser(prog="Bitly shorterer",
                                  description="It is a console \
                                  programm for fast shortening of \
                                  long knotty urls based on a Bitly \
                                  API, which also can give you an \
                                  information about a sum of clicks \
                                  on your bitlinks.")
  parser.add_argument("name", help="Link to shorten or bitlink \
                              to get sum of clicks")

  return parser


def main():
  load_dotenv()
  bitly_token = os.environ["BITLY_OAUTHACCESSTOKEN"]

  parser = create_parser()
  args = parser.parse_args()

  source_url = args.name

  try:
    if is_bitlink(bitly_token, source_url):
      print("Количество переходов по ссылке битли", count_clicks(bitly_token, source_url))
    else:
      shortened_link = shorten_link(bitly_token, source_url)
      print(shortened_link)
  except requests.exceptions.HTTPError:
    print("Ссылка введена неверно")


if __name__ == "__main__":
  main()