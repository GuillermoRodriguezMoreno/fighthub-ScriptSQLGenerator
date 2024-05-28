from faker import Faker
import random
import util
import provider
from datetime import datetime

fake = Faker('es_ES')
# Add the custom provider to the faker instance
fake.add_provider(provider.AndaluciaProvinceProvider)
fake.add_provider(provider.AndaluciaCityProvider)
fake.add_provider(provider.GymNameProvider)

# FIGHTER
def generate_fighter_insert_statement(number_of_inserts):
    insert_statement = "-- FIGHTER"
    for _ in range(number_of_inserts):
        birth_date = fake.date_of_birth(minimum_age=14, maximum_age=50).strftime('%Y-%m-%d')
        email = fake.unique.email()
        password = fake.password(length=8, special_chars=True, digits=True, upper_case=True, lower_case=True)
        register_date = fake.date_this_year().strftime('%Y-%m-%d')
        user_name = fake.user_name()
        profile_photo_id = 'NULL'
        active = True
        biography = fake.text(max_nb_chars=100)
        draws = random.randint(0, 10)
        gender = random.choice(['Male', 'Female'])
        height = random.uniform(120, 250)
        latitude = util.generate_random_lat_andalucia()
        longitude = util.generate_random_long_andalucia()
        losses = random.randint(0, 10)
        name = fake.name()
        weight = random.uniform(30, 150)
        wins = random.randint(0, 30)
        kos = random.randint(0, wins)
        number_of_fights = losses + wins + draws
        wins_in_a_row = random.randint(0, wins)
        category_id = random.randint(1, 4)
        insert_statement += f"""
INSERT INTO fighter (birth_date, email, password, register_date, user_name, profile_photo_id,
                     active, biography, draws, gender, height, kos, latitude, longitude,
                     losses, name, number_of_fights, weight, wins, wins_in_a_row, category_id)
    VALUES ('{birth_date}', '{email}', '{password}', '{register_date}', '{user_name}', {profile_photo_id},
            {active}, '{biography}', {draws}, '{gender}', {height:.2f}, {kos}, {latitude:.6f}, {longitude:.6f},
            {losses}, '{name}', {number_of_fights}, {weight:.2f}, {wins}, {wins_in_a_row}, {category_id});
        """
        insert_statement = insert_statement.strip()
        insert_statement += "\n"

    return insert_statement

# FIGHTER_STYLE
def generate_fighter_style_insert_statement(total_fighters, total_styles):
    insert_statement = "-- FIGHTER_STYLE"
    for fighter_id in range(1, total_fighters + 1):
        for style_id in range(random.randint(1, total_styles), total_styles + 1):
            insert_statement += f"""
INSERT INTO fighter_style (fighter_id, style_id) VALUES ({fighter_id}, {style_id});
"""
            insert_statement = insert_statement.strip()
            insert_statement += "\n"

    return insert_statement

# CLUB
def generate_club_insert_statement(number_of_inserts, total_fighters):
    insert_statement = "-- CLUB"
    for _ in range(number_of_inserts):
        name = fake.gym_name()
        state = fake.andalucia_province()
        city = fake.city_from_province(state)
        country = 'Spain'
        postal_code = fake.postcode()
        street = fake.street_address()
        phone = fake.phone_number()
        email = fake.unique.email()
        register_date = fake.date_this_year().strftime('%Y-%m-%d')
        description = fake.text(max_nb_chars=150)
        deleted = False
        president_id = fake.unique.random_int(min=1, max=total_fighters)
        insert_statement += f"""
INSERT INTO club (name, city, country, postal_code, state, street, phone, email, register_date,
                  description, deleted, president_id)
    VALUES ('{name}', '{city}', '{country}', '{postal_code}', '{state}', '{street}', '{phone}', '{email}',
            '{register_date}', '{description}', {deleted}, {president_id});
        """
        insert_statement = insert_statement.strip()
        insert_statement += "\n"

    return insert_statement

# FIGHTER_ROLE
def generate_fighter_role_insert_statement(total_fighters):
    insert_statement = "-- FIGHTER_ROLE"
    for fighter_id in range(1, total_fighters + 1):
        role_id = random.randint(1, 3)
        insert_statement += f"""
INSERT INTO fighter_role (fighter_id, role_id) VALUES ({fighter_id}, {role_id});
"""
        insert_statement = insert_statement.strip()
        insert_statement += "\n"

    return insert_statement

# ASSOCIATE FIGHTERS WITH CLUB
def associate_fighters_with_club(total_fighters, total_clubs):
    insert_statement = "-- FIGHTER_CLUB"
    for fighter_id in range(1, total_fighters + 1):
        club_id = random.randint(1, total_clubs)
        insert_statement += f"""
UPDATE fighter SET club_id = {club_id} WHERE id = {fighter_id};
"""
        insert_statement = insert_statement.strip()
        insert_statement += "\n"

    return insert_statement

# FOLLOW
#toDo: Fix the follow insert statement
def generate_follow_insert_statement(total_fighters):
    insert_statement = "-- FOLLOW"
    for follower_id in range(1, total_fighters + 1):
        followed_id = random.randint(1, total_fighters)
        if follower_id != followed_id:
            insert_statement += f"""
INSERT INTO follow (follower_fighter_id, followed_fighter_id) VALUES ({follower_id}, {followed_id});
"""
            insert_statement = insert_statement.strip()
            insert_statement += "\n"

    return insert_statement

# FIGHTER_FOLLOW_REQUEST
def generate_fighter_follow_request_insert_statement(total_fighters):
    insert_statement = "-- FIGHTER_FOLLOW_REQUEST"
    for sender_id in range(1, total_fighters + 1):
        request_date = fake.date_this_year()
        response_date = fake.date_between(request_date, end_date=datetime.now().date()).strftime('%Y-%m-%d')
        request_date = request_date.strftime('%Y-%m-%d')
        status = random.choice(['PENDING', 'APPROVED', 'REJECTED'])
        for receiver_id in range(random.randint(1, total_fighters), total_fighters + 1):
            if sender_id != receiver_id:
                insert_statement += f"""
INSERT INTO fighter_follow_request (request_date, response_date, status,
                                    receiver_fighter_id, sender_fighter_id) 
    VALUES ('{request_date}', '{response_date}', '{status}', {receiver_id}, {sender_id});
"""
                insert_statement = insert_statement.strip()
                insert_statement += "\n"

    return insert_statement
