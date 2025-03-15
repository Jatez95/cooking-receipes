from supaconnection.connection import SupaConnection
from dbtables.categories import Categories

class RecipeCategory:
    def __init__(self):
        self.id_category = ""
        self.id_recipe = ""

        self.supaconnection = SupaConnection()

    def add_recipe_category(self, category_id = None, recipe_id = None):

        if category_id is None and recipe_id is None:
            
            raise ValueError('The recipe must need a category')
        
        recipe_category_data = {
                'id_category' : category_id,
                'id_recipe' : recipe_id
            }
            
        response = self.supaconnection.supabase.table('recipe_categories').insert(recipe_category_data).execute()

        return response.data
    
    def update_recipe_category(self, category_id = None, recipe_id = None, new_category = None):
        categories = Categories()
        
        exist_response = categories.get_category_by_id(category_id)

        if exist_response:
            if new_category is not None:
                categoty_to_update = {
                    'id_category' : new_category,
                    'id_recipe' : recipe_id
                }
                response_delete = self.supaconnection.supabase.table('recipe_categories').delete().eq('id_recipe', recipe_id).execute()
                delete_data = response_delete.data
                if delete_data:
                    self.supaconnection.supabase.table('recipe_categories').insert(categoty_to_update).execute()

                print('category updated')
                
            else:
                print('the category wont be updated')
        
    def delete_recipe_category(self, recipe_id):

        response = self.supaconnection.supabase.table('recipe_categories').delete().eq('id_recipe', recipe_id).execute()

        print(response.data)

    def delete_recipe_category_by_category(self, id_category):

        response = self.supaconnection.supabase.table('recipe_categories').delete().eq('id_category', id_category).execute()

        return response.data
    
    def get_recipe_category_by_recipe(self, id_recipe):
        response = self.supaconnection.supabase.table('recipe_categories').select('id_category').eq('id_recipe', id_recipe).execute()
        
        return response.data[0]['id_category']