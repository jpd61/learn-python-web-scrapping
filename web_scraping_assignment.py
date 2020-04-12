import requests
from bs4 import BeautifulSoup

requests.get('https://www.epicurious.com/recipes/food/views/potatoes-with-peppers-and-chorizo-231381?intcid=recirc_outbrain_dfooter')

recipe = requests.get('https://www.epicurious.com/recipes/food/views/potatoes-with-peppers-and-chorizo-231381?intcid=recirc_outbrain_dfooter')

soup = BeautifulSoup(recipe.text, features='lxml')

title = soup.find('h1', itemprop='name')

rating = soup.find(class_='rating')

descrip = soup.find(itemprop='description')

yields = soup.find(itemprop='recipeYield')

ingredients = soup.find_all(itemprop='ingredients')

steps = soup.find(class_='preparation-steps')

if(not title):
    pass
else:
    print(f"\nRecipe Title: {title.text}\n")
if(not rating):
    pass
else:
    print(f"Rating: {rating.text}\n")
if(not descrip):
    pass
else:
    print(f"Description: {descrip.text}\n")
if(not yields):
    pass
else:
    print(f"Yields: {yields.text}\n")
if(not ingredients):
    pass
else:
    print("Ingredients: \n")
    for ingredient in ingredients:
        print(ingredient.text)
if(not steps):
    pass
else:
    print("\nSteps: \n")
for step in steps:
    print(step.text.lstrip())
