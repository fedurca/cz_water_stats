import requests
from bs4 import BeautifulSoup

url = "https://hydro.chmi.cz/hppsoldv/popup_hpps_prfdyn.php?seq=307081"

response = requests.get(url)
i=0
j=0
if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")
    elements = soup.find_all(class_="tborder center_text")
    for element in elements:
        text = element.get_text(strip=True)
        print("CELYTEXT")
        print(text)
        print("CELYTEXT")
        i+=1
else:
    print("Chyba: Nepodařilo se načíst data ze stránky.")
phrase_to_list = text.split(" ")
print(phrase_to_list)
print(phrase_to_list[5])
print(phrase_to_list[6])
print(phrase_to_list[7])
