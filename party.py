class Party:

    def __init__(self):
        self.people = []


party = Party()

while True:
    command = input()
    if command == "End":
        break

    party.people.append(command)

result = ", ".join(party.people)
print(f"Going: {result}")
print(f"Total: {len(party.people)}")
