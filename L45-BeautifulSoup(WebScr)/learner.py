from bs4 import BeautifulSoup
import requests

website="https://news.ycombinator.com"

response = requests.get(website)
contents = response.text

soup = BeautifulSoup(contents, "html.parser")

article_texts=[]
article_links=[]

lead_news = soup.find_all(name="a", class_="titlelink")
for news in lead_news:
    text = news.getText()
    article_texts.append(text)
    link = news.get("href")
    article_links.append(link)

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

print(article_upvotes)
# print(article_links)
# print(article_texts)

max_index = article_upvotes.index(max(article_upvotes))

print(article_upvotes[max_index])
print(article_texts[max_index])
print(article_links[max_index])

# print(int(article_upvotes[0].split()[0]))






# p = BeautifulSoup(contents, "html.parser")
# # print(soup.title.string)
# # print(soup.title)
#
# all_para_tags = soup.find_all(name="p")
# # print(all_para_tags)
#
# # for tag in all_para_tags:
# #     print(tag.getText())
# #     print(tag.get("href"))
#
# # sect_heading = soup.find(name="h3", class_="heading")
# # print(sect_heading)
# #
# # anchors = soup.find_all("a")
# # print(anchors)
#
# company_url = soup.select_one(selector="p a")
# print(company_url)
