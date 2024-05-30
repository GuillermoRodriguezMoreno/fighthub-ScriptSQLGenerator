import insert_data

# Constants
TOTAL_FIGHTERS = 10
TOTAL_CLUBS = 5
TOTAL_EVENTS = 10
TOTAL_STYLES = 6
TOTAL_FIGHTS = 10


def generate_sql_script():
    # Initialize the SQL script
    sql_script = ""
    # Add Fighter data
    sql_script += insert_data.generate_fighter_insert_statement(TOTAL_FIGHTERS)
    # Associate Fighters with Role
    sql_script += "\n"+insert_data.generate_fighter_role_insert_statement(TOTAL_FIGHTERS)
    # Add fighter_style data
    sql_script += "\n"+insert_data.generate_fighter_style_insert_statement(TOTAL_FIGHTERS, TOTAL_STYLES)
    # Add club data
    sql_script += "\n"+insert_data.generate_club_insert_statement(TOTAL_CLUBS, TOTAL_FIGHTERS)
    # Associate some fighters with club
    sql_script += "\n"+insert_data.associate_fighters_with_club(TOTAL_FIGHTERS, TOTAL_CLUBS)
    # Add profile photo of fighters
    sql_script += "\n"+insert_data.generate_fighter_profile_photo_insert_statement(TOTAL_FIGHTERS)
    # Add club photo
    sql_script += "\n"+insert_data.generate_club_photo_insert_statement(TOTAL_CLUBS)
    # Add follow data
    sql_script += "\n"+insert_data.generate_follow_insert_statement(TOTAL_FIGHTERS)
    # Add fighter_follow_request data
    sql_script += "\n"+insert_data.generate_fighter_follow_request_insert_statement(TOTAL_FIGHTERS)
    # Add event data
    sql_script += "\n"+insert_data.generate_event_insert_statement(TOTAL_EVENTS, TOTAL_CLUBS)
    # Add club_membership_request data
    sql_script += "\n"+insert_data.generate_club_membership_request_insert_statement(TOTAL_FIGHTERS, TOTAL_CLUBS)
    # Add club_review data
    sql_script += "\n"+insert_data.generate_club_review_insert_statement(TOTAL_FIGHTERS, TOTAL_CLUBS)
    # Add event_review data
    sql_script += "\n"+insert_data.generate_event_review_insert_statement(TOTAL_FIGHTERS, TOTAL_EVENTS)
    # Add fight data
    sql_script += "\n"+insert_data.generate_fight_insert_statement(TOTAL_EVENTS, TOTAL_FIGHTERS, TOTAL_FIGHTS)
    # Add fight_inscription_request data
    sql_script += "\n"+insert_data.generate_fight_inscription_request_insert_statement(TOTAL_FIGHTERS, TOTAL_EVENTS, TOTAL_CLUBS)

    return sql_script


sql_script = generate_sql_script()

# Guardar el script SQL en un archivo
with open('sql/insert_data.sql', 'a') as file:
    file.write(sql_script)

print("Script SQL generado exitosamente.")
