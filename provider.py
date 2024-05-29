from faker.providers import BaseProvider
import random


class AndaluciaProvinceProvider(BaseProvider):
    provinces = [
        'Sevilla', 'Málaga', 'Cádiz', 'Granada',
        'Córdoba', 'Almería', 'Huelva', 'Jaén'
    ]

    def andalucia_province(self):
        return self.random_element(self.provinces)


class AndaluciaCityProvider(BaseProvider):
    provinces_and_cities = {
        'Sevilla': ['Sevilla', 'Dos Hermanas', 'Utrera'],
        'Málaga': ['Málaga', 'Marbella', 'Fuengirola'],
        'Cádiz': ['Cádiz', 'Jerez de la Frontera', 'Algeciras'],
        'Granada': ['Granada', 'Motril', 'Almuñécar'],
        'Córdoba': ['Córdoba', 'Lucena', 'Montilla'],
        'Almería': ['Almería', 'Roquetas de Mar', 'El Ejido'],
        'Huelva': ['Huelva', 'Lepe', 'Almonte'],
        'Jaén': ['Jaén', 'Linares', 'Úbeda']
    }

    def city_from_province(self, province):
        if province not in self.provinces_and_cities:
            raise ValueError(f"Province '{province}' is not in the list")
        return random.choice(self.provinces_and_cities[province])


class GymNameProvider(BaseProvider):
    gym_names = [
        "Warriors Gym", "Fight Club", "Champions Arena", "Elite MMA",
        "Gladiator Gym", "Knockout Boxing", "Victory Gym", "Titan Gym",
        "Spartan Gym", "Phoenix Fight Club", "Dragons Den MMA",
        "Iron Fist Gym", "Powerhouse Gym", "Supreme Combat", "Raging Bull Gym",
        "Lionheart Gym", "Battle Ground Gym", "Champions Circle", "Invictus Gym",
        "Fearless Fighters", "Ultimate Fight Gym", "Valor Gym", "Heroes Gym",
        "Noble Warriors Gym", "Predator Gym", "Bulldog Gym", "Raging Lions Gym",
        "Victory Path Gym", "Kings Gym", "Champions League Gym", "Epic Fight Club",
        "Titanium Gym", "Renegade Gym", "Iron Warriors Gym", "Stealth Fighters Gym",
        "Conquerors Gym", "Dominion Gym", "Fortress Gym", "Arena of Champions",
        "Legendary Gym", "Viking Gym", "Spartan Strength Gym", "Combat Zone Gym",
        "Battle Arena Gym", "Warriors Edge Gym", "Maverick Gym", "Grit and Glory Gym",
        "Pinnacle Gym", "Warpath Gym"
    ]

    def gym_name(self):
        return self.random_element(self.gym_names)


class FightEventProvider(BaseProvider):
    fight_event_names = [
        "Ultimate Showdown", "Champions Clash", "Warriors Battle", "Fight Night",
        "Gladiator Games", "Battle of the Titans", "Knockout Championship",
        "MMA Grand Prix", "Rage in the Cage", "Fight for Glory",
        "Ultimate Fighter", "Battle Royale", "Fight Fest", "Warriors Path",
        "Cage Warriors", "Victory Challenge", "Rumble in the Ring",
        "Fight of the Champions", "Combat Kings", "The Final Round",
        "Warriors Quest", "Battle for Supremacy", "Knockout Kings",
        "Raging Warriors", "Combat Showdown", "Fight to the Finish",
        "Champions Arena", "Warriors War", "Gladiators Arena",
        "The Ultimate Battle", "Fight Masters", "MMA Showdown",
        "Rumble in the Arena", "Cage Combat", "Battle Grounds",
        "Fight Championship", "Warriors Crown", "Rage of the Gladiators",
        "Ultimate Combat", "Champions War", "Fight Night Extravaganza",
        "Warriors Arena", "MMA Fight Fest", "The Combat Challenge",
        "Battle of the Champions", "Ultimate Warrior", "Knockout Clash",
        "Fight Kingdom", "Rumble Royale"
    ]

    def fight_event_name(self):
        return self.random_element(self.fight_event_names)