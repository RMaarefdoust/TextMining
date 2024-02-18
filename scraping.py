import requests
from bs4 import BeautifulSoup


godFather_link = "https://www.dailyscript.com/scripts/The_Godfather.html"
godFather2_link = "https://www.scripts.com/script.php?id=the_godfather_71&p=4"


html_gf1 = requests.get(godFather_link)
html_gf2 = requests.get(godFather2_link)
bs_gf1 = BeautifulSoup(html_gf1.text)
bs_gf1 = BeautifulSoup(html_gf2.text)

print(html_gf1.text)
print(html_gf2.text)
