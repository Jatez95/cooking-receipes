from dbtables.ingredients import Ingredients

def main():
    table_query = Ingredients()
    table_query.get_all_ingredients()

if __name__ == '__main__':
    main()