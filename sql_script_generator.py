from faker import Faker
import random
import util
import provider


fake = Faker('es_ES')
# Add the custom provider to the faker instance
fake.add_provider(provider.provincia_andalucia_provider)


def generate_insert_statement():
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
    number_of_fights = losses+wins+draws
    wins_in_a_row = random.randint(0, wins)
    category_id = random.randint(1, 4)

    insert_statement = f"""
    INSERT INTO fighter (birth_date, email, password, register_date, user_name, profile_photo_id,
                         active, biography, draws, gender, height, kos, latitude, longitude,
                         losses, name, number_of_fights, weight, wins, wins_in_a_row, category_id)
    VALUES ('{birth_date}', '{email}', '{password}', '{register_date}', '{user_name}', {profile_photo_id},
            {active}, '{biography}', {draws}, '{gender}', {height:.2f}, {kos}, {latitude:.6f}, {longitude:.6f},
            {losses}, '{name}', {number_of_fights}, {weight:.2f}, {wins}, {wins_in_a_row}, {category_id});
    """
    return insert_statement.strip()

def generate_sql_script(num_records):
    sql_script = ""
    for _ in range(num_records):
        sql_script += generate_insert_statement() + "\n"
    return sql_script

# Generar un script SQL con 10 registros de ejemplo
num_records = 10
sql_script = generate_sql_script(num_records)

# Guardar el script SQL en un archivo
with open('sql/insert_fighter_data.sql', 'w') as file:
    file.write(sql_script)

print("Script SQL generado exitosamente.")