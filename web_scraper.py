import requests,time,csv
from bs4 import BeautifulSoup

# if response.status_code == 200:
#     print("Success!")
# elif response.status_code == 404:
#     print("Not Found.")

books = []
ratings = {"One" : "1","Two" : "2","Three" : "3","Four" : "4","Five" : "5",}

for i in range(1,51):
    response = requests.get(f"https://books.toscrape.com/catalogue/page-{i}.html")
    response.encoding = response.apparent_encoding
    soup =  BeautifulSoup(response.text,'html.parser')


    for item in soup.find_all(class_ ="product_pod"):
        book = {}
        book['Title'] = item.h3.a.get('title')
        book['Price'] = item.find(class_ = "price_color").string
        book['Rating'] = f"{ratings[item.find(class_ = 'star-rating').get('class')[-1]]}/5"

        books.append(book)

    # 0.5 second delay before requesting server again
    time.sleep(0.5)

print(books)

with open('books.csv', 'w', encoding='utf-8-sig', newline='') as output_file:
    fc = csv.DictWriter(output_file, fieldnames=["Title","Price","Rating"])
    fc.writeheader()
    fc.writerows(books)




