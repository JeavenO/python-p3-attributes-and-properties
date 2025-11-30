approved_breeds = ["Mastiff", "Chihuahua", "Corgi", "Shar Pei",
                   "Beagle", "French Bulldog", "Pug", "Pointer"]

class Dog:
    def __init__(self, name="Dog", breed="Mutt"):
        self._name = None
        self._breed = None

        # Set name first
        self.name = name

        # Only set breed if it's in approved breeds
        if breed in approved_breeds:
            self.breed = breed
        else:
            # Store the invalid breed anyway so the object is consistent
            self._breed = breed
            # Print error only if it's not the default name error situation
            if self._name is not None:
                print("Breed must be in list of approved breeds.")

    # NAME PROPERTY
    def get_name(self):
        return self._name

    def set_name(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 25:
            self._name = name
        else:
            print("Name must be string between 1 and 25 characters.")

    name = property(get_name, set_name)

    # BREED PROPERTY
    def get_breed(self):
        return self._breed

    def set_breed(self, breed):
        if breed in approved_breeds:
            self._breed = breed
        else:
            print("Breed must be in list of approved breeds.")

    breed = property(get_breed, set_breed)
