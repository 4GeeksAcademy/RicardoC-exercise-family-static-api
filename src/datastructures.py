
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self._next_id = 1
        self._members = [
            {"id": self._generate_id(),
              "first_name": "John",
                "last_name": self.last_name, 
                "age": 33, "lucky_numbers": [7, 13, 22]},
            {"id": self._generate_id(),
              "first_name": "Jane",
                "last_name": self.last_name,
                  "age": 35, "lucky_numbers": [10, 14, 3]},
            {"id": self._generate_id(),
              "first_name": "Jimmy", 
              "last_name": self.last_name,
                "age": 5, "lucky_numbers": [1]}
        ]

    # Para generar un id único para cada miembro
    def _generate_id(self):
        generated_id = self._next_id
        self._next_id += 1
        return generated_id

    # Agregar un nuevo miembro
    def add_member(self, member):
        # Si el id no está presente en el cuerpo, lo va a generar automaticamente
        if "id" not in member:
            member["id"] = self._generate_id()
        member["last_name"] = self.last_name
        self._members.append(member)
        return member

    # Eliminar un miembro por id
    def delete_member(self, id):
        self._members = [member for member in self._members if member["id"] != id]
        return True

    # Obtener un miembro por id
    def get_member(self, id):
        for member in self._members:
            if member["id"] == id:
                return member
        return None

    # Obtener todos los miembros
    def get_all_members(self):
        return self._members
