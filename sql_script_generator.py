import insert_data


def generate_sql_script():
    # Initialize the SQL script
    sql_script = ""
    # Add Fighter data
    sql_script += insert_data.generate_fighter_insert_statement(10)
    # Associate Fighters with Role
    sql_script += "\n"+insert_data.generate_fighter_role_insert_statement(10)
    # Add fighter_style data
    sql_script += "\n"+insert_data.generate_fighter_style_insert_statement(10, 6)
    # Add club data
    sql_script += "\n"+insert_data.generate_club_insert_statement(10, 10)
    # Associate some fighters with club
    sql_script += "\n"+insert_data.associate_fighters_with_club(10, 10)
    # Add follow data
    sql_script += "\n"+insert_data.generate_follow_insert_statement(10)
    # Add fighter_follow_request data
    sql_script += "\n"+insert_data.generate_fighter_follow_request_insert_statement(10)
    # Add event data
    sql_script += "\n"
    # Add club_membership_request data
    sql_script += "\n"
    # Add club_review data
    sql_script += "\n"
    # Add event_review data
    sql_script += "\n"
    # Add fight data
    sql_script += "\n"
    # Add fight_inscription_request data
    sql_script += "\n"

    return sql_script


sql_script = generate_sql_script()

# Guardar el script SQL en un archivo
with open('sql/insert_data.sql', 'a') as file:
    file.write(sql_script)

print("Script SQL generado exitosamente.")
