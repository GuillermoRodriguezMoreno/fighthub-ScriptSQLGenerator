from faker import Faker
import Util
import Provider


fake = Faker('es_ES')
# Add the custom provider to the faker instance
fake.add_provider(Provider.provincia_andalucia_provider)

for i in range(10):
    print(fake.name())
    print(fake.date_of_birth(None, 14, 50))
    print(fake.provincia_andalucia())