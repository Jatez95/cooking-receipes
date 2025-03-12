from supaconnection.connection import SupaConnection

class Categories:
    def __init__(self):
        self.id_category = ""
        self.category_name = ""

        self.supaconnection = SupaConnection()

    def add_category(self, category_name):
        response = self.supaconnection.supabase.table('categories').insert({'name' : category_name}).execute()

        if response:
            print(f"Category {category_name} succesfully added")
        else:
            print(f"Couldnt add the categorie {category_name}")
    
    def get_category(self, category_name):

        response = self.supaconnection.supabase.table('categories').select('name').eq('name', category_name).execute()

        self.category_name = response.data[0]['name']

        if self.category_name:
            print(self.category_name)
        else:
            print(f'The category {category_name} dosnt exists')
        
        self.category_name = ""

    def get_all_categories(self):

        response = self.supaconnection.supabase.table('categories').select('name').execute()

        if response:
            categories_list = []

            for i in range(len(response.data)):
                categories_list.append(response.data[i]['name'])
            
        print(categories_list)
