import os
from dotenv import load_dotenv
from supabase import create_client, Client

load_dotenv()

class SupaConnection:

    def __init__(self):
        self.url = os.getenv('SUPA_URL')
        self.key = os.getenv('SUPA_KEY')
        self.supabase: Client = create_client(self.url, self.key)

    
    def connect(self) -> Client:
        """Establish the connection with supabase"""
        return self.supabase