class Zoo:
    __animals = 0

    def __init__(self, name):
        self.name = name
        self.birds = []
        self.mammals = []
        self.fishes = []

    def add_animal(self, species, name):
        if species == "mammal":
            self.mammals.append(name)
        elif species == "bird":
            self.birds.append(name)
        elif species == "fish":
            self.fishes.append(name)
        self.__animals += 1

    def get_info(self, species):
        result = ""
        if species == "mammal":
            mammals = ", ".join(self.mammals)
            result += f"Mammals in {self.name}: {mammals}"
            result += f"\nTotal animals: {self.__animals}"
        elif species == "bird":
            birds = ", ".join(self.birds)
            result += f"Birds in {self.name}: {birds}"
            result += f"\nTotal animals: {self.__animals}"
        elif species == "fish":
            fishes = ", ".join(self.fishes)
            result += f"Fishes in {self.name}: {fishes}"
            result += f"\nTotal animals: {self.__animals}"

        return result


zoo_name = input()

zoo = Zoo(zoo_name)
number = int(input())
for x in range(number):
    animals_info = input().split(" ")
    species = animals_info[0]
    name = animals_info[1]
    zoo.add_animal(species, name)

species = input()

print(zoo.get_info(species))