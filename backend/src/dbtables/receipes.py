from supaconnection.connection import SupaConnection

class Receipes:
    def __init__(self):
        self.id_receipe = ""
        self.id_user = ""
        self.description = ""
        self.title = ""
        self.creation_date = ""
        self.instructions = ""
        self.dificulty = ""
        
        self.supaconnection = SupaConnection()

    def get_all_receipes(self):
        

        response = self.supaconnection.supabase.table('receipes').select('*').execute()

        if response:
            receipes_list = []
            
            for i in range(len(response)):
                receipes_list.append(response.data[i])
        
        print(receipes_list)
    
    def get_receipe_by_title(self, title):

        response = self.supaconnection.supabase.table('receipe').select('*').execute()

        self.title = response.data[0]['title']
        self.id_receipe = response.data[0]['id_receipe']

        if self.title:
            print(f'Found receipe: {self.title} with id {self.id_receipe}')
        else:
            print(f'Receipe not found')

        self.id_receipe = ""
        self.title = ""

    
    def add_receipe(self, title, instructions, id_user = None,  description=None, difficulty = None):

        

        receipe_data = {
            'title' : title, 
            'instructions' : instructions, 
        }

        if id_user is not None:
            receipe_data['id_user'] = id_user

        if description is not None:
            receipe_data['description'] = description
        
        if difficulty is not None:
            difficulties = ['Easy', 'Mid', 'Hard']

            if difficulty not in difficulties:
                raise ValueError(f'Difficulty must be one of this: {difficulties}')
            
            receipe_data['difficulty'] = difficulty
        
        response = self.supaconnection.supabase.table('receipes').insert(receipe_data).execute()

        print(response.data)

        
    
    def delete_receipe(self, title):

        response = self.supaconnection.supabase.table('receipes').delete().eq('title', title).execute()

        if response:
            print(f"receipe {title} succesfuly deleted")
        else:
            print(f"An error ocurred deleting the receipe {title}")

    def update_receipe(self, title, description = None, new_title = None, instructions = None, difficulty = None):

        receipe_data = {}

        if new_title is not None:
            receipe_data['title'] = new_title
        
        if description is not None:
            receipe_data['description'] = description

        if instructions is not None:
            receipe_data['instructions'] = instructions
        
        if difficulty is not None:
            difficulties = ['Easy', 'Mid', 'Hard']

            if difficulty not in difficulties:
                raise ValueError(f'Difficulty must be one of this: {difficulties}')
            
            receipe_data['difficulty'] = difficulty

        receipe_response = self.supaconnection.supabase.table('receipes').update(receipe_data).eq('title', title).execute()

        print(receipe_response.data)