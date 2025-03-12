from supaconnection.connection import SupaConnection

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

        
        exist_response = self.supaconnection.supabase.table('recipe_ingredient').select('*').eq('id_category', category_id).eq('id_recipe', recipe_id).execute()

        recipe_category_data = exist_response.data

        if recipe_category_data and new_category is not None:
            categoty_to_update = {
                'id_category' : new_category
            }
            response = self.supaconnection.supabase.table('recipe_ingredient').update(categoty_to_update).eq('id_recipe', recipe_id).execute()

            return response
        else:
            print('the category wont be updated')
        