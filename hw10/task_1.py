"""
### Homework
Ваша задача спарсить информацию о компаниях, находящихся в индексе S&P 500 с данного сайта: <br>
https://markets.businessinsider.com/index/components/s&p_500

Для каждой компании собрать следующую информацию:
* Текущая стоимость в рублях (конвертацию производить по текущему курсу, взятому с сайта [центробанка РФ](http://www.cbr.ru/development/sxml/))
* Код компании (справа от названия компании на странице компании)
* P/E компании (информация находится справа от графика на странице компании)
* Годовой рост/падение компании в процентах (основная таблица)
* Высчитать какую прибыль принесли бы акции компании (в процентах), если бы они были куплены на уровне 52 Week Low и проданы на уровне 52 Week High (справа от графика на странице компании)

Сохранить итоговую информацию в 4 JSON файла:
1. Топ 10 компаний с самими дорогими акциями в рублях.
2. Топ 10 компаний с самым низким показателем P/E.
3. Топ 10 компаний, которые показали самый высокий рост за последний год
4. Топ 10 комппаний, которые принесли бы наибольшую прибыль, если бы были куплены на самом минимуме и проданы на самом максимуме за последний год.
<br>Пример формата:
```
[
{
    "code": "MMM",
    "name": "3M CO.",
    "price" | "P/E" | "growth" | "potential profit" : value,
},
...
]
```
For scrapping you cans use `beautifulsoup4` <br>
For requesting `aiohttp`
"""


from bs4 import BeautifulSoup
import aiohttp
import asyncio
import requests
import lxml
import re


# res = requests.get("https://markets.businessinsider.com/index/components/s&p_500")
# # res = requests.get("https://markets.businessinsider.com/index/components/s&p_500?p=2")
#
# soup = BeautifulSoup(res.content, "lxml")
#
# for i in soup.find_all("a", class_=None, href=re.compile('stocks'), title=re.compile(''), text=True):
#     print(i.text)
# ---------------------------------------
# res = requests.get("https://markets.businessinsider.com/stocks/mmm-stock")
# # res = requests.get("https://markets.businessinsider.com/stocks/acn-stock")
#
# soup = BeautifulSoup(res.content, "lxml")
# # Company_Name = soup.find("span", class_="price-section__label")
# Company_Name = soup.find(class_="price-section__label")
# print("Company_Name", Company_Name.text)
# # Company_Label = soup.find("span", class_="price-section__category")
# Company_Label = soup.find(class_="price-section__category")
# # print("Company_Label", Company_Label)
# Company_Label = Company_Label.find("span")
# print("Company_Label", Company_Label.text.replace(", ", ""))
# ---------------------------------------
# res = requests.get("https://markets.businessinsider.com/index/components/s&p_500")
# soup = BeautifulSoup(res.content, "lxml")
#
# Companies = {}
#
# href="https://markets.businessinsider.com/"
#
# for link in soup.find_all("a", class_=None, href=re.compile('stocks'), title=re.compile(''), text=True):
#     ref = link.get('href')
#     res_1 = requests.get(href+ref)
#     soup_1 = BeautifulSoup(res_1.content, "lxml")
#     Company_Name = soup_1.find(class_="price-section__label")
#     Company_Label = soup_1.find(class_="price-section__category")
#     Company_Label = Company_Label.find("span")
#     Companies[Company_Name.text] = Company_Label.text.replace(", ", "")
#
# for i in Companies:
#     print(i, Companies[i])
# ---------------------------------------
res = requests.get("https://markets.businessinsider.com/index/components/s&p_500")
soup = BeautifulSoup(res.content, "lxml")

Companies = {}

href="https://markets.businessinsider.com/"

for link in soup.find_all("a", class_=None, href=re.compile('stocks'), title=re.compile(''), text=True):
    ref = link.get('href')
    res_1 = requests.get(href+ref)
    soup_1 = BeautifulSoup(res_1.content, "lxml")
    Company_Name = soup_1.find(class_="price-section__label")
    Company_Label = soup_1.find(class_="price-section__category")
    Company_Label = Company_Label.find("span")
    Companies[Company_Name.text] = Company_Label.text.replace(", ", "")

    # print(type(soup_1))     # <class 'bs4.BeautifulSoup'>

    nn = soup_1.find_all(class_="snapshot__data-item")

    # print(type(nn))     # <class 'bs4.element.ResultSet'>

    # print(nn)

    for i in nn:
        print(i.text)




    # for i in nn:
    #     print(i)
    #     # print(type(i))      # <class 'bs4.element.Tag'>
    #     g = i.find_all()
    #     print(g)
    #     # n = g.find()
    #     # print(n)


        # if str(i) == re.compile('P/E Ratio'):
        #     print('!!!!!!!!!!!!!!!!')

        # if 'Prev' in i:
        #     print('!!!!!!!!!!!!!!!!')




    # nn = soup_1.find(class_="snapshot__data-item")

    # text = nn.get_text(strip=True)

    # print(text)


    # print(nn)

    # g = []

    # for i in nn:
    #     g.append(i.text)



        # print(i)
        # print(i.text)
        # if i.text == re.compile('P/E Ratio'):
        # if i.text == re.compile('P/E Ratio'):
        #     print('___________________________ok_____________________________')


    # print(g)


    # for i in nn:
    #     print(i)

        # print(i.text)
        # if i.text == re.compile('P/E Ratio'):
        #     print('ok')
        #     break

    # print(soup_1.find_all(class_="snapshot__data-item"))

    break


# q = 'qwerty'

# q = re.compile('q')
# print(q)




# for i in Companies:
#     print(i, Companies[i])















# for sub_heading in soup.find_all('h5'):
#     print(sub_heading.text)



# print(soup.prettify())

# print(soup.get_attribute_list)








# print(soup)
# print(soup.prettify())

# print(soup.title)

# for link in soup.find_all('a'):
#     print(link.get('href'))


# with open("res.text", "r") as fp:
#     soup = BeautifulSoup(fp)







"""
Метод recursiveChildGenerator() позволяет перебрать содержимое HTML-документа.
При помощи атрибута children можно вывести все дочерние теги.
При помощи атрибута descendants можно получить список всех потомков (дочерних элементов всех уровней) рассматриваемого тега.
При помощи метода prettify() можно добиться того, чтобы HTML-код выглядел аккуратнее.
При помощи метода find() можно найти элементы страницы, используя различные опорные параметры, id в том числе.


for link in soup.find_all('a'):     # Поиск всех ссылок
    print(link.get('href'))
    
text        # Текст


вы можете перебирать все ссылки или подзаголовки в документе, используя следующий код:
for sub_heading in soup.find_all('h2'):
    print(sub_heading.text)


Вложенные подзаголовки    
for sub_heading in soup.find_all('h3'):
    print(sub_heading.text)


При оформлении текста с помощью css чаще всего используют тег <span>. 
Он обозначает «просто текстовый блок». То есть особенного собственного смысла он не имеет. 
Также этот тег никак не изменяет отображение текста.


for i in soup.find_all('a', string='3M'):
    print(i)            # <a href="/stocks/mmm-stock" title="3M">3M</a>
    
    
for i in soup.find_all('a', title="3M"):
    print(i)            # <a href="/stocks/mmm-stock" title="3M">3M</a>
    
    
for i in soup.find_all("a", href="/stocks/mmm-stock"):
    print(i)            # <a href="/stocks/mmm-stock" title="3M">3M</a>
"""









