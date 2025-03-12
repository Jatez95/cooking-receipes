from supaconnection.connection import SupaConnection
import hashlib

class Users:
    def __init__(self):
        self.id_user = ""
        self.name = ""
        self.email = ""
        self.password = ""
        self.register_date = ""
        
        self.supaconnection = SupaConnection()

    def add_user(self, name, email, password):
        self.name = name
        self.email = email

        self.password = hashlib.sha256((password).encode()).hexdigest()

        response = self.supaconnection.supabase.table('users').insert({"name" : self.name, "email" : self.email, "password" : self.password}).execute()
        print(response.data)

        self.name = ""
        self.email = ""
        self.password = ""

        
    
    def get_user(self, name, password):

        self.password = hashlib.sha256(password.encode()).hexdigest()

        response = self.supaconnection.supabase.table('users').select('id_user, name, email').eq('name', name).eq('password', self.password).execute()


        self.id_user = response.data[0]["id_user"]
        self.name = response.data[0]["name"]
        self.email = response.data[0]["email"]

        if self.id_user and self.name and self.email:
            print(f"Welcome: {self.name} with id {self.id_user} and email {self.email}")
        
        else: 
            print("User Not found")

        
        self.id_user = ""
        self.name = ""
        self.email = ""
    
    def change_password(self, name, email, password):

        self.password = hashlib.sha256(password.encode()).hexdigest()

        response = self.supaconnection.supabase.table('users').update(
                {'password' : self.password}
                ).eq('name', name).eq('email', email).execute()
        
        if response:
            print('Password updated succesfuly')
        else:
            print(f'User {name} not found')

        self.password = ""
    
    def change_email(self, name, password, email):

        self.password = hashlib.sha256(password.encode()).hexdigest()

        old_email = self.supaconnection.supabase.table('users').select('email').eq('name', name).eq('password', self.password).execute()

        response = self.supaconnection.supabase.table('users').update(
            {'email' : email}
        ).eq('name', name).eq('password', self.password).execute()

        if response:
            print(response)
            print(f'Your old email {old_email.data[0]['email']} has been updated to: {email}')
        else:
            print('Error updating the email')
        
        self.password = ""
    
    def change_username(self, name, password, new_name):

        self.password = hashlib.sha256(password.encode()).hexdigest()

        old_name = self.supaconnection.supabase.table('users').select('name').eq('name', name).eq('password', self.password).execute()

        

        if old_name:
            comprove_response = self.supaconnection.supabase.table('users').update({'name' : new_name}).eq('name', name).eq('password', self.password).execute()
            if comprove_response:
                print(f'Name updated succesfully! last name: {old_name.data[0]['name']} current: {new_name}')
        else:
            print('Error updating the username')
    
    def delete_user(self, name, password):

        self.password = hashlib.sha256(password.encode()).hexdigest()

        response = self.supaconnection.supabase.table('users').select('*').eq('name', name).eq('password', password).execute()

        if response:
            delete_response = self.supaconnection.supabase.table('users').delete().eq('name', name).eq('password', self.password).execute()
            if delete_response.data:
                print('User deleted succesfuly')
        else:
            print(f'Error: user with name {name} not found')