from faker import Faker
import random
import util
import provider
from datetime import datetime, timedelta

fake = Faker('es_ES')
# Add the custom provider to the faker instance
fake.add_provider(provider.AndaluciaProvinceProvider)
fake.add_provider(provider.AndaluciaCityProvider)
fake.add_provider(provider.GymNameProvider)
fake.add_provider(provider.FightEventProvider)

# FIGHTER
def generate_fighter_insert_statement(number_of_inserts):
    insert_statement = "-- FIGHTER"
    for _ in range(number_of_inserts):
        birth_date = fake.date_of_birth(minimum_age=14, maximum_age=50).strftime('%Y-%m-%d')
        email = fake.unique.email()
        password = fake.password(length=8, special_chars=True, digits=True, upper_case=True, lower_case=True)
        register_date = fake.date_this_year().strftime('%Y-%m-%d')
        user_name = fake.user_name()
        profile_photo_id = None
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
INSERT INTO fighter (   birth_date, 
                        email, 
                        password, 
                        register_date, 
                        user_name, 
                        profile_photo_id,
                        active, 
                        biography, 
                        draws, 
                        gender, 
                        height, 
                        kos, 
                        latitude, 
                        longitude,
                        losses, 
                        name, 
                        number_of_fights, 
                        weight, 
                        wins, 
                        wins_in_a_row, 
                        category_id)
                        
    VALUES ('{birth_date}', 
            '{email}', 
            '{password}', 
            '{register_date}', 
            '{user_name}', 
            {f"'{profile_photo_id}'" if profile_photo_id else 'NULL'},
            {active}, 
            '{biography}', 
            {draws}, 
            '{gender}', 
            {height:.2f}, 
            {kos}, 
            {latitude:.6f}, 
            {longitude:.6f},
            {losses}, 
            '{name}', 
            {number_of_fights}, 
            {weight:.2f}, 
            {wins}, 
            {wins_in_a_row}, 
            {category_id});
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
INSERT INTO fighter_style ( fighter_id, 
                            style_id) 
    VALUES ({fighter_id}, 
            {style_id});
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
INSERT INTO club (  name, 
                    city, 
                    country, 
                    postal_code, 
                    state, 
                    street, 
                    phone, 
                    email, 
                    register_date,
                    description, 
                    deleted, 
                    president_id)
                    
    VALUES ('{name}', 
            '{city}', 
            '{country}', 
            '{postal_code}', 
            '{state}', 
            '{street}', 
            '{phone}', 
            '{email}',
            '{register_date}', 
            '{description}', 
            {deleted}, 
            {president_id});
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
INSERT INTO fighter_role (  fighter_id, 
                            role_id) 
                            
    VALUES ({fighter_id}, 
            {role_id});
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
def generate_follow_insert_statement(total_fighters):
    insert_statement = "-- FOLLOW"
    for follower_id in range(1, total_fighters + 1):
        follow_date = fake.date_time_this_year(before_now=True).strftime('%Y-%m-%d %H:%M')
        followed_id = random.randint(1, total_fighters)
        if follower_id != followed_id:
            insert_statement += f"""
INSERT INTO follow (follow_date, 
                    follower_fighter_id, 
                    followed_fighter_id)
                     
    VALUES ('{follow_date}', 
            {follower_id}, 
            {followed_id});
"""
            insert_statement = insert_statement.strip()
            insert_statement += "\n"

    return insert_statement


# FIGHTER_FOLLOW_REQUEST
def generate_fighter_follow_request_insert_statement(total_fighters):
    insert_statement = "-- FIGHTER_FOLLOW_REQUEST"
    for sender_id in range(1, total_fighters + 1):
        request_date = fake.date_time_this_year()
        response_date = fake.date_time_between(request_date, end_date=datetime.now()).strftime('%Y-%m-%d %H:%M')
        request_date = request_date.strftime('%Y-%m-%d %H:%M')
        status = random.choice(['PENDING', 'APPROVED', 'REJECTED'])
        for receiver_id in range(random.randint(1, total_fighters), total_fighters + 1):
            if sender_id != receiver_id:
                insert_statement += f"""
INSERT INTO fighter_follow_request (request_date, 
                                    response_date, 
                                    status,
                                    receiver_fighter_id, 
                                    sender_fighter_id)
                                     
    VALUES ('{request_date}', 
            '{response_date}', 
            '{status}', 
            {receiver_id}, 
            {sender_id});
"""
                insert_statement = insert_statement.strip()
                insert_statement += "\n"

    return insert_statement


# EVENT
def generate_event_insert_statement(number_of_inserts, total_clubs):
    insert_statement = "-- EVENT"
    for _ in range(number_of_inserts):
        country = 'Spain'
        postal_code = fake.postcode()
        state = fake.andalucia_province()
        city = fake.city_from_province(state)
        street = fake.street_address()
        description = fake.text(max_nb_chars=150)
        name = fake.fight_event_name()
        open_date = fake.future_datetime(end_date='+1y')
        end_date = open_date + timedelta(hours=5)
        start_date = open_date + timedelta(hours=1)
        open_date = open_date.strftime('%Y-%m-%d %H:%M')
        club_id = fake.random_int(min=1, max=total_clubs)

        insert_statement += f"""
INSERT INTO event ( city, 
                    country, 
                    postal_code, 
                    state, street, 
                    description, 
                    end_date, 
                    name, 
                    open_date, 
                    start_date, 
                    club_id)
                    
    VALUES (    '{city}', 
                '{country}', 
                '{postal_code}', 
                '{state}', 
                '{street}', 
                '{description}',
                '{end_date}', 
                '{name}', '
                {open_date}',
                '{start_date}', 
                {club_id});
"""
        insert_statement = insert_statement.strip()
        insert_statement += "\n"

    return insert_statement


# CLUB_MEMBERSHIP_REQUEST
def generate_club_membership_request_insert_statement(total_fighters, total_clubs):
    insert_statement = "-- CLUB_MEMBERSHIP_REQUEST"
    for fighter_id in range(1, total_fighters + 1):
        request_date = fake.date_time_this_year(before_now=True)
        response_date = fake.date_time_between(start_date=request_date, end_date=datetime.now().date()).strftime('%Y-%m-%d %H:%M')
        request_date = request_date.strftime('%Y-%m-%d %H:%M')
        status = random.choice(['PENDING', 'APPROVED', 'REJECTED'])
        club_id = random.randint(1, total_clubs)
        insert_statement += f"""
INSERT INTO club_membership_request (   request_date, 
                                        response_date, 
                                        status, 
                                        club_id, 
                                        fighter_id)
                                        
    VALUES (    '{request_date}', 
                '{response_date}', 
                '{status}', 
                {club_id}, 
                {fighter_id});
"""
        insert_statement = insert_statement.strip()
        insert_statement += "\n"

    return insert_statement


# CLUB_REVIEW
def generate_club_review_insert_statement(total_fighters, total_clubs):
    insert_statement = "-- CLUB_REVIEW"
    for fighter_id in range(1, total_fighters + 1):
        for club_id in range(1, total_clubs + 1):
            content = fake.text(max_nb_chars=150)
            rating = random.randint(1, 5)
            review_date = fake.date_time_this_year(before_now=True).strftime('%Y-%m-%d %H:%M')
            if(random.choice([True, False])):
                insert_statement += f"""
INSERT INTO club_review (   content, 
                            rating, 
                            review_date, 
                            club_id, 
                            fighter_id)
                            
    VALUES (    '{content}', 
                {rating}, 
                '{review_date}', 
                {club_id}, 
                {fighter_id});
"""
            insert_statement = insert_statement.strip()
            insert_statement += "\n"

    return insert_statement


# EVENT_REVIEW
def generate_event_review_insert_statement(total_fighters, total_events):
    insert_statement = "-- EVENT_REVIEW"
    for fighter_id in range(1, total_fighters + 1):
        for event_id in range(1, total_events + 1):
            content = fake.text(max_nb_chars=150)
            rating = random.randint(1, 5)
            review_date = fake.date_time_this_year(before_now=True).strftime('%Y-%m-%d %H:%M')
            if(random.choice([True, False])):
                insert_statement += f"""
INSERT INTO event_review (  content, 
                            rating, 
                            review_date, 
                            event_id, 
                            fighter_id)
                            
    VALUES (    '{content}', 
                {rating}, 
                '{review_date}', 
                {event_id}, 
                {fighter_id});
"""
            insert_statement = insert_statement.strip()
            insert_statement += "\n"

    return insert_statement


# FIGHT
def generate_fight_insert_statement(total_events, total_fighters, total_fights):
    insert_statement = "-- FIGHT"
    for event_id in range(1, total_events + 1):
        fight_order = 0
        for fight in range(1, random.randint(5, total_fights+1)):
            fight_order += 1
            is_title_fight = random.choice([True, False])
            minutes = random.choice([2, 3])
            total = random.choice([2, 3])
            start_time = fake.date_time_this_year().strftime('%Y-%m-%d %H:%M')
            weight = random.uniform(30, 150)
            isKo = random.choice([True, False])
            blue_corner_fighter_id = random.randint(1, total_fighters)
            category_id = random.randint(1, 4)
            red_corner_fighter_id = random.randint(1, total_fighters)
            if blue_corner_fighter_id == red_corner_fighter_id:
                red_corner_fighter_id = random.randint(1, total_fighters)
            event_id = random.randint(1, total_events)
            style_id = random.randint(1, 6)
            winner_id = None
            if(random.choice([True, False])):
                winner_id = random.choice([blue_corner_fighter_id, red_corner_fighter_id])

            insert_statement += f"""
INSERT INTO fight ( fight_order,
                    is_title_fight, 
                    minutes, 
                    total, 
                    start_time, 
                    weight, 
                    is_ko,
                    blue_corner_fighter_id, 
                    category_id, 
                    event_id, 
                    red_corner_fighter_id, 
                    style_id,
                    winner_id)
                    
    VALUES ({fight_order}, 
            {is_title_fight}, 
            {minutes}, 
            {total}, 
            '{start_time}', 
            {weight:.2f}, 
            {isKo},
            {blue_corner_fighter_id}, 
            {category_id}, 
            {event_id}, 
            {red_corner_fighter_id}, 
            {style_id}, 
            {f"'{winner_id}'" if winner_id else 'NULL'});
"""
            insert_statement = insert_statement.strip()
            insert_statement += "\n"

    return insert_statement


# FIGHT_INSCRIPTION_REQUEST
def generate_fight_inscription_request_insert_statement(total_fighters, total_events, total_clubs):
    insert_statement = "-- FIGHT_INSCRIPTION_REQUEST"
    for fighter_id in range(1, total_fighters + 1):
        club_id = random.randint(1, total_clubs)
        for event_id in range(1, total_events + 1):
            for fight_id in range(1, 5+1):
                message = fake.text(max_nb_chars=100)
                request_date = fake.date_time_this_year(before_now=True)
                status = random.choice(['PENDING', 'APPROVED', 'REJECTED'])
                response_date = None
                response = None
                if status == 'APPROVED' or status == 'REJECTED':
                    response_date = fake.date_time_between(start_date=request_date, end_date=datetime.now()).strftime('%Y-%m-%d %H:%M')
                    response = fake.text(max_nb_chars=100)

                request_date = request_date.strftime('%Y-%m-%d %H:%M')
                insert_statement += f"""
INSERT INTO fight_inscription_request ( message, 
                                        request_date,
                                        response,
                                        response_date,
                                        status,
                                        club_id,
                                        fight_id,
                                        fighter_id,
                                        event_id)
                                        
    VALUES ('{message}',
            '{request_date}',
            {f"'{response}'" if response else 'NULL'},
            {f"'{response_date}'" if response_date else 'NULL'},
            '{status}',
            '{club_id}',
            '{fight_id}',
            {fighter_id},
            {event_id});
"""
                insert_statement = insert_statement.strip()
                insert_statement += "\n"

    return insert_statement

