from supaconnection.connection import SupaConnection

class IngredientRecipe:
    def __init__(self):
        self.id_recipe = ""
        self.id_ingredients = ""
        self.quantity = None
        self.measure_unit = ""

        self.supaconnection = SupaConnection()
    
    def add_ingredient_recipe(self, id_recipe, id_ingredients, quantity, unit_of_measure):

        if id_recipe and id_ingredients and quantity and unit_of_measure:

            ingredient_recipe_data = {
                'id_ingredients' : id_ingredients,
                'id_recipe' : id_recipe,
                'quantity' : quantity,
                'unit_of_measure' : unit_of_measure
            }

            
            response = self.supaconnection.supabase.table('ingredients_recipe').insert(ingredient_recipe_data).execute()

            return response.data
        
        else:
            raise ValueError('None of the values can be empty')
    
    def get_data_by_recipe(self, id_recipe):

        if not id_recipe:
            raise ValueError('The id of the recipe was empty')
        
        response = self.supaconnection.supabase.table('ingredients_recipe').select('*').eq('id_recipe', id_recipe).execute()

        if len(response.data) == 0:
            return None
        return response.data
    
    def delete_data_by_recipe_id(self, id_recipe):

        response = self.supaconnection.supabase.table('ingredients_recipe').delete().eq('id_recipe', id_recipe).execute()

        return response.data

    def delete_relation_by_ingredient(self, id_ingredient):
        response = self.supaconnection.supabase.table('ingredients_recipe').delete().eq('id_ingredients', id_ingredient).execute()

        return response.data
    
    def update_ingredient_recipe(self, id_recipe, id_ingredient, quantity = None, unit_of_measure = None):
        ingredients_recipe_data = {}

        if quantity is not None:
            ingredients_recipe_data['quantity'] = quantity
        
        if unit_of_measure is not None:
            ingredients_recipe_data['unit_of_measure'] = unit_of_measure
        
        response = self.supaconnection.supabase.table('ingredients_recipe').update(ingredients_recipe_data)\
            .eq('id_recipe', id_recipe)\
            .eq('id_ingredients', id_ingredient)\
            .execute()

        data = response.data

        if data:
            print('Ingredient updated')
        else:
            print('Error updating the ingredient')

        

    def check_for_update(self, id_recipe, ingredients_recipe_objects):

        if isinstance(ingredients_recipe_objects, list):

            ingredients_added_to_recipe = self.supaconnection.supabase.table('ingredients_recipe').select('*')\
                .eq('id_recipe', id_recipe).execute()

            added_ingredients_list = ingredients_added_to_recipe.data


            to_add = []
            to_update = []

            current_ingredients_dict = {item['id_ingredients'] : item for item in added_ingredients_list}

            
            for ingredient in ingredients_recipe_objects:
                if ingredient['id_ingredients'] in current_ingredients_dict:
                    to_update.append(ingredient)
                else:
                    to_add.append(ingredient)
            
            for ingredient in to_update:
                try:
                    self.update_ingredient_recipe(
                        id_recipe = id_recipe,
                        id_ingredient = ingredient['id_ingredients'],
                        quantity = ingredient['quantity'],
                        unit_of_measure = ingredient['unit_of_measure']
                    )
                except ValueError as e:
                    print(f'Error adding ingredient {str(e)}')

            for ingredient in to_add:
                try:
                    self.add_ingredient_recipe(
                        id_recipe = id_recipe,
                        id_ingredients = ingredient['id_ingredients'],
                        quantity = ingredient['quantity'],
                        unit_of_measure = ingredient['unit_of_measure']
                    )
                except ValueError as e:
                    print(f'Error adding ingredient {str(e)}')
        
        elif isinstance(ingredients_recipe_objects, dict):
            ingredients_added_to_recipe = self.supaconnection.supabase.table('ingredients_recipe').select('*')\
                .eq('id_recipe', id_recipe).execute()

            added_ingredients_list = ingredients_added_to_recipe.data

            current_ingredients_dict = {item['id_ingredients'] : item for item in added_ingredients_list}

            if ingredients_recipe_objects['id_ingredients'] in current_ingredients_dict:
                try:
                    self.update_ingredient_recipe(
                        id_recipe = id_recipe,
                        id_ingredient = ingredients_recipe_objects['id_ingredients'],
                        quantity = ingredients_recipe_objects['quantity'],
                        unit_of_measure = ingredients_recipe_objects['unit_of_measure']
                    )
                except ValueError as e:
                    print(f'Error adding ingredient {str(e)}')
            else:
                try:
                    self.add_ingredient_recipe(
                        id_recipe = id_recipe,
                        id_ingredients = ingredients_recipe_objects['id_ingredients'],
                        quantity = ingredients_recipe_objects['quantity'],
                        unit_of_measure = ingredients_recipe_objects['unit_of_measure']
                    )
                except ValueError as e:
                    print(f'Error adding ingredient {str(e)}')