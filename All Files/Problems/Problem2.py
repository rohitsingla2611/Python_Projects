class Shelter:
    def __init__(self, shelter_for):
        self.shelter_for = shelter_for
        print(shelter_for)


class Tent(Shelter):
    def __init__(self, shelter_for, no_of_cots, no_of_chain):
        super().__init__(shelter_for)
        self.no_of_cots = no_of_cots
        self.no_of_chain = no_of_chain


class Cage(Shelter):
    def __init__(self, shelter_for, type_of_locks):
        # super().__init__(shelter_for)
        super(shelter_for)
        self.type_of_locks = type_of_locks


ta = Tent(1, 2, 3)
