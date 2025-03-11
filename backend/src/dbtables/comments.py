from supaconnection.connection import SupaConnection

class Comment:
    def __init__(self):
        self.id_receipe = ""
        self.id_user = ""
        self.comment = ""
        self.calification = None

        self.supaconnection = SupaConnection()

    def add_comemnt(self, comment, id_receipe = None, id_user = None, calification = None):

        comment_data = {
            'comment' : comment
        }

        if id_receipe is not None:
            comment_data['id_receipe'] = id_receipe
        
        if id_user is not None:
            comment_data['id_user'] = id_user
        
        if calification is not None:
            if calification in [1, 2, 3, 4, 5]:
                comment_data['calification'] = calification
            else:
                raise ValueError(f'The calification must be between 1 and 5')
        
        response = self.supaconnection.supabase.table('comments').insert(comment_data).execute()

        print(response.data)
    
    def get_comments_by_receipe_id(self, id_receipe):
        
        response = self.supaconnection.supabase.table('comments').select('*').eq('id_receipe', id_receipe).execute()

        print(response.data)

    def delete_comment(self, id_comment, id_user):
            
            comment_response = self.supaconnection.supabase.table('comments').select('*').eq('id_comment', id_comment).eq('id_user', id_user).execute()

            comment_data = comment_response.data
            if comment_data:

                delete_response = self.supaconnection.supabase.table('comments').delete().eq('id_comment', id_comment).execute()

                print(delete_response.data)
            else:
                print('An error ocurred trying to delete the comment')
    
    def update_comment(self, id_user, comment):

        comment_data = {
            'comment' : comment
        }

        response = self.supaconnection.supabase.table('comments').update(comment_data).eq('id_user', id_user).execute()

        print(response.data)