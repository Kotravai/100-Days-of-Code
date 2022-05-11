import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)
contents = response.text

soup = BeautifulSoup(contents, "html.parser")
movie_list = []

movie_list = [movie.text for movie in soup.find_all(name="h3", class_="title")]

# for movie in movies:
#     movie_list.append(movie.text)
#     movie_list.append("\n")

movie_list.reverse()

with open("movie_list.txt", "w") as file:
    for _ in movie_list:
        file.write(f"{_}\n")




# print(movie_list)

    # file.write(movie)

    # movie_list.append(movie)




# print(contents)
