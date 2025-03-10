from supaconnection.connection import SupaConnection

class Receipes:
    def __init__(self, id_receipe, id_user, description, title, creation_date, instructions, dificulty):
        self.id_receipe = id_receipe
        self.id_user = id_user
        self.description = description
        self.title = title
        self.creation_date = creation_date
        self.instructions = instructions
        self.dificulty = dificulty
        self.connection = SupaConnection()

    def get_receipes(self):
        response = self.connection.supabase.table('receipes').select('*').execute()
        print(response)
    
    
    