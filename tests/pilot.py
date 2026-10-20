"""Тестовый пилот: только делегирование публичных команд."""


class Pilot:
    def __init__(self, plane):
        self.plane = plane

    def идти_по_дороге(self, km):
        return self.plane.move(km, "road")

    def идти_по_камням(self, km):
        return self.plane.move(km, "rough")

    def идти_по_воде(self, km):
        return self.plane.move(km, "water")

    def взлететь(self, km):
        return self.plane.move(km, "air")

    def проверить_преграду(self, height):
        return self.plane.can_step_over(height)

    def перешагнуть(self, height):
        return self.plane.step_over(height)

    def заправиться(self, amount):
        return self.plane.refuel(amount)

    def повредить_ноги(self):
        return self.plane.damage_legs()

    def починить_ноги(self):
        return self.plane.repair_legs()

    def оценить_расход_на_камнях(self, km):
        return self.plane.calculate_energy(km, "rough")
