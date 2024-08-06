import requests

url = "https://api.gurusensei.workers.dev/dream"

params = {
  'prompt': "Wolf"
}

headers = {
  'User-Agent': "Mozilla/5.0 (Linux; Android 13; Pixel 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36",
  'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
  'Accept-Encoding': "gzip, deflate",
  'cache-control': "max-age=0",
  'upgrade-insecure-requests': "1",
  'sec-gpc': "1",
  'dnt': "1",
  'accept-language': "en;q=0.9,en-US;q=0.8",
  'save-data': "on",
  'x-requested-with': "mark.via.gp",
  'sec-fetch-site': "none",
  'sec-fetch-mode': "navigate",
  'sec-fetch-user': "?1",
  'sec-fetch-dest': "document",
  'referer': "https://gpt4.guruapi.tech/"
}

response = requests.get(url, params=params, headers=headers)

print(response.text)