import asyncio

from dbtables.recipes import Recipes
from dbtables.users import Users
from dbtables.comments import Comment

def main():
    table_query = Recipes()
    table_query.update_recipe(
        id_recipe = '710d6574-048f-46fb-9fa4-aae4eedf3f45',
        new_title = 'Fucking Cookies no chocolate',
        instructions = 'Bake that shit',
        description = 'There is no Oreo',
        difficulty = 'Hard',
        ingredients_recipe = [
            {
                'id_ingredients' : '574c60c6-17ed-4f33-b78e-8720a8f820da',
                'quantity' : 1,
                'unit_of_measure' : 'leafs'
            },
            {
                'id_ingredients' : '869b65f4-ca84-4b13-9ef4-85fbde45a962',
                'quantity' : 10,
                'unit_of_measure' : 'eggs'
            },
            {
                'id_ingredients' : '055fde67-f78e-4974-b8d4-464fadfca945',
                'quantity' : 1,
                'unit_of_measure' : 'glass'
            }
        ],
        category = {'id_category' : '44dddc3f-0760-49e8-a25f-b8475e1cc8cd'}
    )

    # table_query.add_recipe(
    #     title = 'Chocolate Chip Cookie',
    #     instructions = 'Mix and bake at 350°F for 12 minutes.',
    #     id_user = '0965c71f-d833-45e1-8a3a-2b78f6021817',
    #     description = 'Classic cookies everyone loves',
    #     difficulty = 'Easy',
    #     ingredients_recipe = [
    #         {
    #             'id_ingredients' : '70a162e4-c2e7-4deb-a77d-df9290126d84',
    #             'quantity' : 2,
    #             'unit_of_measure' : 'cups'
    #         },
    #         {
    #             'id_ingredients' : '869b65f4-ca84-4b13-9ef4-85fbde45a962',
    #             'quantity' : 1,
    #             'unit_of_measure' : 'eggs'
    #         }
    #     ],
    #     category = {'id_category' : '9bbdef9f-b568-4e9b-9a28-cd90f06e067d'}
    # )

    # table_query.delete_recipe(id_recipe = '710d6574-048f-46fb-9fa4-aae4eedf3f45')

    

if __name__ == '__main__':
    main()