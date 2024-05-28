from faker.providers import DynamicProvider


provincia_andalucia_provider = DynamicProvider(
    provider_name="provincia_andalucia",
    elements=["Almería", "Cádiz", "Córdoba", "Granada", "Huelva", "Jaén", "Málaga", "Sevilla"],
)
