

class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        if pet_type not in self.PET_TYPES:
            raise Exception("Invalid pet type")

        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        self.add_to_all_instances()

    def add_to_all_instances(self):
        self.__class__.all.append(self)


class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]

    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception("Not a valid pet")

        pet.owner = self
        Pet.all.append(pet)

    def get_sorted_pets(self):
        owner_pets = self.pets()
        sorted_pets = sorted(owner_pets, key=lambda x: x.name)
        return sorted_pets
    
