from supaconnection.connection import SupaConnection

class IngredientRecipe:
    def __init__(self):
        self.id_recipe = ""
        self.id_ingredients = ""
        self.quantity = None
        self.measure_unit = ""

        self.supaconnection = SupaConnection()
    
    def add_ingredient_recipe(self, id_recipe, id_ingredients, quantity, unit_of_measure):

        ingredient_recipe_data = {}

        if id_recipe and id_ingredients and quantity and unit_of_measure:

            ingredient_recipe_data['id_recipe'] = id_recipe
            ingredient_recipe_data['id_ingredients'] = id_ingredients
            ingredient_recipe_data['quantity'] = quantity
            ingredient_recipe_data['unit_of_measure'] = unit_of_measure

            
            response = self.supaconnection.supabase.table('ingredients_recipe').insert(ingredient_recipe_data).execute()

            print(response.data)
        
        else:
            raise ValueError('None of the values can be empty')
    
    def get_data_by_recipe(self, id_recipe):

        if not id_recipe:
            raise ValueError('The id of the recipe was empty')
        
        response = self.supaconnection.supabase.table('ingredients_recipe').select('*').eq('id_recipe', id_recipe).execute()

        print(response.data)