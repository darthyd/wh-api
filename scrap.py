from requests_html import HTMLSession

url = 'https://sports.williamhill.com/betting/en-gb/football/matches/competition/today/match-betting'
s = HTMLSession()
r = s.get(url)

r.html.render(sleep=1, scrolldown=10, timeout=20, wait=5)

games = r.html.find('.sp-o-market__title > a')

gamelist = []

for item in games:
    home = item.text.split(' v ')[0]
    away = item.text.split(' v ')[1]
    link = item.attrs['href']
    id = item.attrs['href'].split('OB_EV')[1].split('/')[0]
    print('home:', home, 'away:', away, 'id:', id)
    gamelist.append({'home': home, 'away': away, 'id': id, 'link': link})
