import webbrowser, sys, pyperclip, requests, bs4
if len(sys.argv) > 1:
	term = ' '.join(sys.argv[1:])
else:
	term = pyperclip.paste()


headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}

URL = 'https://www.google.co.in/search?q=' + term

res = requests.get(URL, headers = headers)

try:
	res.raise_for_status()
except Exception as ex:
	print('There was a problem: %s' %(ex), '\nSorry!!')
	
soup = bs4.BeautifulSoup(res.text, "html.parser")

card = soup.select('g-inner-card')

cardNum = len(card)
if cardNum == 0:
	print("There is no news about %s.Try something else."%(term))
	sys.exit(0)

f = '.' + ''.join(card[0].attrs.get('class')) + ' a' 

num = input("OK. So, how many pages you want to open about " + term + ". You can open atmost 3 pages.")
numb = int(num)

while(numb <= 0 or numb > 3):
	num = input("Please act clever where you need to. Enter an appropriate number.")
	numb = int(num)

linkElems = soup.select(f)

numOpen = min(numb, len(linkElems))


for i in range(numOpen):
	webbrowser.open_new_tab(linkElems[i].get('href'))

print("It's open. Don't waste your time looking at this screen.")