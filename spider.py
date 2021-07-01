import requests
from bs4 import BeautifulSoup

URL = 'https://lpf.ro/liga-1'
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')

stage_tabel = soup.find(class_ = 'clasament_general white-shadow etape_meciuri')
# print(stage_tabel.prettify())

teams_rows = stage_tabel.find_all(class_= 'echipa-etapa-1')
# print(teams_rows)

teams = []

for team in teams_rows:
    team_cell = team.find('a')
    team_name = team_cell.find(class_= 'hiddenMobile').text.strip()
    teams.append(team_name)

print(teams)