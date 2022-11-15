import random
import numpy as np
from operator import itemgetter


# Bee and Particle swarm Hybrid
class BPH:
    def __init__(self, func, scouts, elite, perspect, bees_to_leet, bees_to_persp, fi_p, fi_g, radius, position_x,
                 position_y):
        self.func = func

        self.pos_x = float(position_x)
        self.pos_y = float(position_y)

        assert fi_p + fi_g > 4, "Сумма коэффициентов должна быть > 4"
        self.fi_p = fi_p
        self.fi_g = fi_g
        self.xi = 2 / (np.abs(2 - (fi_p + fi_g) - np.sqrt((fi_p + fi_g) ** 2 - 4 * (fi_p + fi_g))))

        self.scouts = [[random.uniform(-self.pos_x, self.pos_x), random.uniform(-self.pos_y, self.pos_y), 0.0] for _ in
                       range(scouts)]

        for i in self.scouts:
            i[2] = self.func(i[0], i[1])

        self.n_workers = elite * bees_to_leet + perspect * bees_to_persp
        self.e = elite
        self.p = perspect
        self.b_leet = bees_to_leet
        self.b_persp = bees_to_persp
        self.rad = radius

        self.workers = [[0.0, 0.0, 0.0] for _ in range(self.n_workers)]
        self.bees = list()
        self.selected = list()

        self.nostalgia = list()
        self.selected_nostalgia = list()
        self.velocity = [[0.0 for _ in range(2)] for _ in range(self.n_workers)]

    def send_scouts(self):
        for unit in self.scouts:
            unit[0] = random.uniform(-self.pos_x, self.pos_x)
            unit[1] = random.uniform(-self.pos_y, self.pos_y)
            unit[2] = self.func(unit[0], unit[1])

    def init_research(self):
        BPH.send_scouts()
        self.selected = sorted(self.scouts, key=itemgetter(2), reverse=False)[:self.e + self.p]

        for i in range(self.e):
            BPH.send_workers(self.func, self.workers[i * self.b_leet:i * self.b_leet + self.b_leet], self.selected[i],
                             i, self.rad)

        for i in range(self.p):
            BPH.send_workers(self.func, self.workers[
                                        self.e * self.b_leet + i * self.b_persp:self.e * self.b_leet + i * self.b_persp + self.b_persp],
                             self.selected[self.e + i], self.e + i, self.rad)
        self.nostalgia = self.workers.copy()

    def iteration(self):
        BPH.send_scouts()
        BPH.research_reports()

        for i in range(self.e):
            BPH.move_worker_swarm(self,
                                  self.workers[i * self.b_leet:i * self.b_leet + self.b_leet],
                                  self.velocity[i * self.b_leet:i * self.b_leet + self.b_leet],
                                  self.nostalgia[i * self.b_leet:i * self.b_leet + self.b_leet],
                                  self.selected_nostalgia[i]
                                  )

        for i in range(self.p):
            BPH.move_worker_swarm(self,
                                  self.workers[
                                  self.e * self.b_leet + i * self.b_persp:self.e * self.b_leet + i * self.b_persp + self.b_persp],
                                  self.velocity[
                                  self.e * self.b_leet + i * self.b_persp:self.e * self.b_leet + i * self.b_persp + self.b_persp],
                                  self.nostalgia[i * self.b_leet:i * self.b_leet + self.b_leet],
                                  self.selected_nostalgia[self.e + i]
                                  )

    def research_reports(self):
        self.bees = self.scouts + self.workers + self.selected_nostalgia
        self.bees = sorted(self.bees, key=itemgetter(2), reverse=False)

        self.selected = self.bees[:self.e + self.p]

    def send_workers(self, bee_part, sector, sector_numb, radius):
        for bee in bee_part:
            bee[0] = random.uniform(sector[0] - radius, sector[0] + radius)
            bee[1] = random.uniform(sector[1] - radius, sector[1] + radius)
            bee[2] = self.func(bee[0], bee[1])
            if bee[2] < sector[2]:
                self.selected_nostalgia[sector_numb] = bee.copy()

    def update_velocity(self, velocity, particle, nostalgia, point_best) -> list:
        new_vel = list()
        for i in range(2):
            r1 = random.random()
            r2 = random.random()

            new_vel.append(self.xi * (velocity[i] + self.fi_p * r1 * (nostalgia[i] - particle[i]) + self.fi_g * r2 * (
                    point_best[i] - particle[i])))
        return new_vel

    def update_position(self, velocity, particle):
        x = particle[0] + velocity[0]
        y = particle[1] + velocity[1]

        return [x, y, self.func(x, y)]

    def move_worker_swarm(self, worker_part, velocity_part, nostalgia_part, best_point):
        for i in range(worker_part):

            if nostalgia_part[i][2] < worker_part[i][2]:
                best_point = nostalgia_part[i]
            else:
                nostalgia_part[i] = worker_part[i]
                best_point = worker_part[i]

            velocity_part[i] = BPH.update_velocity(self, velocity_part[i], worker_part[i], nostalgia_part[i],
                                                   best_point)
            worker_part[i] = BPH.update_position(self, velocity_part[i], worker_part[i])

    def selected_search(self, param):
        for i in range(self.e):
            BPH.send_workers(self.func, self.workers[i * self.b_leet:i * self.b_leet + self.b_leet], self.selected[i],
                             self.rad * param)

        for i in range(self.p):
            BPH.send_workers(self.func, self.workers[
                                        self.e * self.b_leet + i * self.b_persp:self.e * self.b_leet + i * self.b_persp + self.b_persp],
                             self.selected[self.e + i], self.rad * param)

    def get_best(self):
        return self.bees[0]
