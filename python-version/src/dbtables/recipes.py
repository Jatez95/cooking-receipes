from supaconnection.connection import SupaConnection
from .ingredient_recipe import IngredientRecipe
from .recipe_category import RecipeCategory
from .users import Users
from .ingredients import Ingredients

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

            recipes_response = response.data

            recipes_list = []

            for recipe in recipes_response:
                recipe_data = {}
                

                recipe_data['recipe_title'] = recipe['title']
                recipe_data['recipe_description'] = recipe['description']
                recipe_data['recipe_instructions'] = recipe['instructions']
                recipe_data['difficulty'] = recipe['difficulty']

                creation_date = recipe['creation_date']

                creation_date = str(creation_date).replace('T' , ' ')
                recipe_data['creation_date'] = creation_date

                
                id_user = recipe['id_user']
                
                if id_user is not None:
                    user = Users()
                    user_name = user.get_user_by_id(id_user)

                    recipe_data['user_creator'] = user_name
                else:
                    recipe_data['user_creator'] = 'Anonymous'
                
                ingredients_recipe_table = IngredientRecipe()

                ingredients_recipe_data = ingredients_recipe_table.get_data_by_recipe(id_recipe = recipe['id_recipe'])

                if ingredients_recipe_data is not None:
                    ingredients_list = []
                    
                    ingredients_table = Ingredients()

                    for i in range(len(ingredients_recipe_data)):
                        ingredients_needed = {}
                        ingredients_needed['unit_of_measure'] = ingredients_recipe_data[i]['unit_of_measure']
                        ingredients_needed['quantity'] = ingredients_recipe_data[i]['quantity']



                        ingredient = ingredients_table.get_ingredients_by_id(ingredients_recipe_data[i]['id_ingredients'])
                        ingredients_needed['ingredient_name'] = ingredient[0]['name']

                        ingredients_list.append(ingredients_needed)
                    
                    recipe_data['ingredients_list'] = ingredients_list
                    
                    
                else:
                    print('This recipe has no ingredients found, skipping')
                    recipe_data['ingredients_list'] = None
                    
                
                recipes_list.append(recipe_data)

        return recipes_list



                

                
    
    def get_recipe_by_title(self, title = None):

        if title is None:
            raise ValueError(f'The recipe title: {title} is None')

        response = self.supaconnection.supabase.table('recipes').select('*').eq('title', title).execute()

        if response:

            recipes_response = response.data[0]

            recipe_data = {}     

            recipe_data['recipe_title'] = recipes_response['title']
            recipe_data['recipe_description'] = recipes_response['description']
            recipe_data['recipe_instructions'] = recipes_response['instructions']
            recipe_data['difficulty'] = recipes_response['difficulty']

            creation_date = recipes_response['creation_date']

            creation_date = str(creation_date).replace('T' , ' ')
            recipe_data['creation_date'] = creation_date

                
            id_user = recipes_response['id_user']
                
            if id_user is not None:
                user = Users()
                user_name = user.get_user_by_id(id_user)

                recipe_data['user_creator'] = user_name
            else:
                recipe_data['user_creator'] = 'Anonymous'
                
            ingredients_recipe_table = IngredientRecipe()

            ingredients_recipe_data = ingredients_recipe_table.get_data_by_recipe(id_recipe = recipes_response['id_recipe'])

            if ingredients_recipe_data is not None:
                ingredients_list = []
                    
                ingredients_table = Ingredients()

                for i in range(len(ingredients_recipe_data)):
                    ingredients_needed = {}
                    ingredients_needed['unit_of_measure'] = ingredients_recipe_data[i]['unit_of_measure']
                    ingredients_needed['quantity'] = ingredients_recipe_data[i]['quantity']



                    ingredient = ingredients_table.get_ingredients_by_id(ingredients_recipe_data[i]['id_ingredients'])
                    ingredients_needed['ingredient_name'] = ingredient[0]['name']

                    ingredients_list.append(ingredients_needed)
                    
                recipe_data['ingredients_list'] = ingredients_list
                          
            else:
                print('This recipe has no ingredients found, skipping')
                recipe_data['ingredients_list'] = None
            
            return recipe_data
        

    
    async def add_recipe(
        self, 
        title, 
        instructions, 
        id_user = None, 
        description=None, 
        difficulty = None, 
        ingredients_recipe = None,
        category = None
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

                print(ingredients_recipe)

                for ingredient in ingredients_recipe:
                    if isinstance(ingredient, dict) and 'id_ingredients' in ingredient and 'quantity' in ingredient and 'unit_of_measure' in ingredient:

                        try:
                            table_ingredient_recipe.add_ingredient_recipe(
                                id_recipe = new_recipe_id,
                                id_ingredients = ingredient['id_ingredients'],
                                quantity = ingredient['quantity'],
                                unit_of_measure = ingredient['unit_of_measure']
                            )
                        except ValueError as e:
                            print(f'Error adding ingredient {str(e)}')
                    
                    else:
                        print('invalid ingredient format, skipping')
        
            if category is not None and isinstance(category, dict):
                recipe_category_table = RecipeCategory()

                try: 
                    recipe_category_table.add_recipe_category(
                        category_id = category['id_category'],
                        recipe_id = new_recipe_id
                    )
                except ValueError as e:
                    print(f'Error adding a category to the recipe: {str(e)}')
            else:
                print('invalid data to add')

        
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