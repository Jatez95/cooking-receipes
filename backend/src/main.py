from backend.src.dbtables.recipes import Recipes
from dbtables.users import Users
from dbtables.comments import Comment

def main():
    table_query = Comment()

    table_query.delete_comment(id_user = "0965c71f-d833-45e1-8a3a-2b78f6021817", id_comment = "e443c3cd-d4bd-45c3-adfc-d365a34765c9")

if __name__ == '__main__':
    main()