from supaconnection.connection import SupaConnection
from ingredient_recipe import IngredientRecipe

class Recipes:
    def __init__(self):
        self.id_recipe = ""
        self.id_user = ""
        self.description = ""
        self.title = ""
        self.creation_date = ""
        self.instructions = ""
        self.dificulty = ""
        
        self.supaconnection = SupaConnection()

    def get_all_recipes(self):
        

        response = self.supaconnection.supabase.table('recipes').select('*').execute()

        if response:
            recipes_list = []
            
            for i in range(len(response)):
                recipes_list.append(response.data[i])
        
        print(recipes_list)
    
    def get_recipe_by_title(self, title):

        response = self.supaconnection.supabase.table('recipe').select('*').execute()

        self.title = response.data[0]['title']
        self.id_recipe = response.data[0]['id_recipe']

        if self.title:
            print(f'Found recipe: {self.title} with id {self.id_recipe}')
        else:
            print(f'Recipe not found')

        self.id_recipe = ""
        self.title = ""

    
    def add_recipe(
        self, 
        title, 
        instructions, 
        id_user = None, 
        description=None, 
        difficulty = None, 
        ingredients_recipe = None
    ):

        recipe_data = {
            'title' : title, 
            'instructions' : instructions, 
        }

        if id_user is not None:
            recipe_data['id_user'] = id_user

        if description is not None:
            recipe_data['description'] = description
        
        if difficulty is not None:
            difficulties = ['Easy', 'Mid', 'Hard']

            if difficulty not in difficulties:
                raise ValueError(f'Difficulty must be one of this: {difficulties}')
            
            recipe_data['difficulty'] = difficulty
        
        response = self.supaconnection.supabase.table('recipes').insert(recipe_data).execute()


        if response.data and len(response.data) > 0:

            new_recipe_id = response.data[0]['id_recipe'] 
            new_recipe_title = response.data[0]['title']
            print(f'created recipe with title: {new_recipe_title} and id {new_recipe_id}')

            if ingredients_recipe is not None and isinstance(ingredients_recipe, list):
                table_ingredient_recipe = IngredientRecipe()

                for ingredient in ingredients_recipe:
                    if isinstance(ingredient, dict) and ['id_ingredients', 'quantity', 'unit_of_measuer'] in ingredient: # and 'quantity' in ingredient and 'unit_of_measuer' in ingredient this will be used if with the list dosnt work

                        try:
                            table_ingredient_recipe.add_ingredient_recipe(
                                id_recipe = new_recipe_id,
                                id_recipe = ingredient['id_ingredients'],
                                quantity = ingredient['quantity'],
                                unit_of_measure = ingredient['unit_of_measure']
                            )
                        except ValueError as e:
                            print(f'Error adding ingredient {str(e)}')
                    
                    else:
                        print('invalid ingredient format, skipping')
        
        return response.data

        

        
    
    def delete_recipe(self, title):

        response = self.supaconnection.supabase.table('recipes').delete().eq('title', title).execute()

        if response:
            print(f"recipe {title} succesfuly deleted")
        else:
            print(f"An error ocurred deleting the recipe {title}")

    def update_recipe(self, title, description = None, new_title = None, instructions = None, difficulty = None):

        recipe_data = {}

        if new_title is not None:
            recipe_data['title'] = new_title
        
        if description is not None:
            recipe_data['description'] = description

        if instructions is not None:
            recipe_data['instructions'] = instructions
        
        if difficulty is not None:
            difficulties = ['Easy', 'Mid', 'Hard']

            if difficulty not in difficulties:
                raise ValueError(f'Difficulty must be one of this: {difficulties}')
            
            recipe_data['difficulty'] = difficulty

        recipe_response = self.supaconnection.supabase.table('recipes').update(recipe_data).eq('title', title).execute()

        print(recipe_response.data)