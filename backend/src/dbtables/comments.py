from supaconnection.connection import SupaConnection

class Comment:
    def __init__(self):
        self.id_recipe = ""
        self.id_user = ""
        self.comment = ""
        self.calification = None

        self.supaconnection = SupaConnection()

    def add_comemnt(self, comment, id_recipe = None, id_user = None, calification = None):

        comment_data = {
            'comment' : comment
        }

        if id_recipe is not None:
            comment_data['id_recipe'] = id_recipe
        
        if id_user is not None:
            comment_data['id_user'] = id_user
        
        if calification is not None:
            if calification in [1, 2, 3, 4, 5]:
                comment_data['calification'] = calification
            else:
                raise ValueError(f'The calification must be between 1 and 5')
        
        response = self.supaconnection.supabase.table('comments').insert(comment_data).execute()

        print(response.data)
    
    def get_comments_by_recipe_id(self, id_recipe):
        
        response = self.supaconnection.supabase.table('comments').select('*').eq('id_recipe', id_recipe).execute()

        print(response.data)

    def delete_comment(self, id_comment, id_user):
            
            if not id_comment or not id_user:
                raise ValueError('Cant delete the comment wihtout and user id or comment id')
            
            comment_response = self.supaconnection.supabase.table('comments').select('*').eq('id_comments', id_comment).eq('id_user', id_user).execute()

            comment_data = comment_response.data
            if comment_data:

                delete_response = self.supaconnection.supabase.table('comments').delete().eq('id_comments', id_comment).execute()

                print(delete_response.data)
            else:
                print('An error ocurred trying to delete the comment')
                
    
    def update_comment(self, comment, id_comment, id_user, calification = None):

        comment_data = {
            'comment' : comment
        }

        if calification is not None:
            comment_data['calification'] = calification

        if id_comment and id_user:
            response = self.supaconnection.supabase.table('comments').update(comment_data).eq('id_comments', id_comment).execute()

        else:
            raise ValueError('We need boths ids, the id of the comment and the user id. To update the comment.')
        
        print(response.data)