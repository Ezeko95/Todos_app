
import os

os.environ['DATABASE_URL'] = 'postgres://user:password@localhost:5432/mydatabase'
os.environ['SECRET_KEY'] = '34dbb4e97665494dbcee6c4c7a9d618c'
os.environ['API_URL'] = 'GET https://api.spoonacular.com/recipes/findByIngredients'
