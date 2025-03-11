from dbtables.receipes import Receipes
from dbtables.users import Users

def main():
    table_query = Receipes()
    table_query.update_receipe(description = "Sabroso caldo de pollo con fideos" , title = "Sopa de pollo", new_title = "Sopa de pollo simple", instructions = "Vertir caldo de pollo en una olla grande una vez caliente hecha los fideos y esperar a que se inflen los fideos", difficulty = "Mid")

if __name__ == '__main__':
    main()