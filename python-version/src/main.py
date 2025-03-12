import asyncio

from dbtables.recipes import Recipes
from dbtables.users import Users
from dbtables.comments import Comment

async def main():
    table_query = Recipes()
    table_query.get_recipe_by_title(title = 'Chocolate chip cookies')

    

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())