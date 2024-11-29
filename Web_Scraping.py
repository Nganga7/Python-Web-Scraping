#British Airways Data Science Virtual Experience
#Import Requests, BeautifulSoup, Matplotlib and Textwrap
from matplotlib import pyplot as mat
import requests
from bs4 import BeautifulSoup
from textwrap import wrap
from textblob import TextBlob
from newspaper import Article

#Get URL link and use BeautifulSoup to parse the html content
url = ('https://www.airlinequality.com/')
html = requests.get(url)
soup = BeautifulSoup(html.content,'lxml')

#Create empty arrays to store values from loops
my_ratings = []
my_airlines = []
my_categories = []
my_review_count = []
my_review_content = []

#Airline review content within the article tag and class as below
#Ratings within div tag dependent on article tag
#Splitting of ratings and slicing array for ratings
#Conversion of ratings from string to interger
for article in soup.find_all('article',class_='comp comp_media-review-rated list-item media position-content'):
    rating = article.find('div',class_='rating-10').text
    ratings = rating.split('/')[0]
    ratings_ln = ratings.splitlines()
    ratings_ln = [int(i) for i in ratings_ln]
    for ratn in ratings_ln:
        my_ratings.append(ratn)

#Airlines within div tag dependent on article tag
#Content isolated and put in a array
#Splitting of content and slicing array for airlines
#Replacing of '-' with new line to enable word wrap
    airline_cat = article.find('div',class_='body').h2.a['href']
    airline = airline_cat.split('/')[2]
    airlines = airline.splitlines()
    for arln in airlines:
        my_airlines.append(arln)
    my_airlines = [ label.replace('-', '\n') for label in my_airlines]

#Categories within div tag dependent on article tag
#Content isolated and put in a array
#Splitting of content and slicing array for categories
    category = airline_cat.split('/')[1]
    categories = category.splitlines()
    for cat in categories:
        my_categories.append(cat)

#Review count within div span dependent on article tag
#Splitting of review count and slicing array for count
#Conversion of review count from string to interger
    reviews = article.find('span',class_='review-count').text
    review_count = reviews.split(' ')[0]
    review_count_ln = review_count.splitlines()
    review_count_ln = [int(i) for i in review_count_ln]
    #print(review_count_ln)
    for rev in review_count_ln:
        my_review_count.append(rev)

#Review count within div span dependent on article tag
#Splitting of review count and slicing array for count
#Conversion of review count from string to interger
    review_content = article.find('div',class_='text_content toggleEx active').text
    blob = TextBlob(review_content)
    polarities = blob.sentiment.polarity
    polarities_ln = str(polarities).splitlines()
    pols_int = [float(i) for i in polarities_ln]
    for pols in pols_int:
        my_review_content.append(pols)
    #sentiments = my_review_content.splitlines()
    #print(sentiments)




print(my_ratings)
print(my_airlines)
print(my_review_count)
print(my_review_content)


mat.bar(my_airlines,my_ratings,label = 'Ratings per Airline')
mat.xlabel('Airlines')
mat.ylabel('Ratings')
mat.title('Ratings per Airline')
mat.show()

mat.bar(my_airlines,my_review_count,label = 'No. of Reviews per Airline')
mat.xlabel('Airlines')
mat.ylabel('No. of Reviews')
mat.title('No. of Reviews per Airline')
mat.show()

mat.bar(my_airlines,my_review_content,label = 'Sentiment Analysis per Airline')
mat.xlabel('Airlines')
mat.ylabel('Sentiment')
mat.title('Sentiment Analysis per Airline')
mat.show()
