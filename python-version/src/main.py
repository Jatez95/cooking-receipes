import asyncio

from dbtables.recipes import Recipes
from dbtables.users import Users
from dbtables.comments import Comment

async def main():
    table_query = Recipes()

    await table_query.add_recipe( 
        title = "Chocolate chip cookies",
        instructions = "Mix and bake at 350°F for 12 minutes.",
        id_user = "0965c71f-d833-45e1-8a3a-2b78f6021817",
        description = "Classic cookies everyone loves",
        difficulty = "Easy",
        ingredients_recipe = [
            {
                'id_ingredients' : '70a162e4-c2e7-4deb-a77d-df9290126d84',
                'quantity' : 2,
                'unit_of_measure' : 'cups'
            },
            {
                'id_ingredients' : '869b65f4-ca84-4b13-9ef4-85fbde45a962',
                'quantity' : 1,
                'unit_of_measure' : 'eggs'
            }
        ],
        category = {'id_category' : '9bbdef9f-b568-4e9b-9a28-cd90f06e067d'}
    )

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())