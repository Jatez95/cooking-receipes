from supaconnection.connection import SupaConnection

class Ingredients:
    def __init__(self):
        self.ingredient_id = ""
        self.ingredient_name = ""

        self.supaconnection = SupaConnection()
    
    def add_ingredient(self, name):
        response = self.supaconnection.supabase.table('ingredients').insert({"name": name}).execute()

        if response:
            print(f'Ingredient added succesfully')
        else:
            print(f'Error adding a new ingredient')
    
    def select_ingredient(self, name):
        response = self.supaconnection.supabase.table('ingredients').select('*').eq('name', name).execute()

        self.ingredient_name = response.data[0]['name']

        if self.ingredient_name:
            print(f'Ingredient selected: {self.ingredient_name}')
        else:
            print(f'Ingredient {self.ingredient_name} not found')
    
    def get_all_ingredients(self):
        
        response = self.supaconnection.supabase.table('ingredients').select('name').execute()

        if response:
            ingredients_list = []

            for i in range(len(response.data)):
                ingredients_list.append(response.data[i]['name'])

        print(ingredients_list)

    