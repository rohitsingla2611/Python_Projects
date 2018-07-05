# Monkey is a Circus Animal
class CircusAnimal:
    def bow_before_perf(self):
        print("Bowing Before")

    def wave_after_perf(self):
        counter = int(input('Enter the times of Wave'))
        wave_counter = 0
        while wave_counter < counter:
            print('Wave after performance')
            wave_counter += 1


class Monkey(CircusAnimal):
    def ride_cycle(self):
        self.bow_before_perf()
        print('Ride Cycle')
        self.wave_after_perf()


class Lion(CircusAnimal):
    def jump_ring(self):
        self.bow_before_perf()
        print('Jumps through Ring')
        self.wave_after_perf()


doodo = Monkey()
doodo.ride_cycle()
