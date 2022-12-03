from urllib.request import Request, urlopen

req = Request('https://leetcode.com/explore/featured/card/dynamic-programming/', headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()