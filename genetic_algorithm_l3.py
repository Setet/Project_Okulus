from random import uniform, random
from Rosenbrock_function import rosen

class GeneticAlgorithmL3:
    def __init__(self, func, generations=50, mut_chance=0.8, survive_cof=0.8, pop_number=100):
        self.func = func
        self.population = dict()
        self.mut_chance = mut_chance
        self.survive_cof = survive_cof
        self.generations = generations
        self.pop_number = pop_number

    def generate_start_population(self, x, y):
        for i in range(self.pop_number):
            self.population[i] = [uniform(-x,x),uniform(-y,y,), 0] #Создание начальной популяции
                                                              # 2 гена (x, y) и значение фитнес-функции(z)
        
    
    def simulation(self):
        for agent in self.population.values():
            agent[2] = self.func(agent[0],agent[1]) # Вычисляем значение функции(z) по (x, y)
        print("Simulation")
        return self.population
    
    
    def select(self):
        sorted_pop = dict(sorted(self.population.items(), key=lambda item: item[1][2])) #Ранжирование

        cof = int(self.pop_number*(1-self.survive_cof))
        parents1 = list (sorted_pop.items()) [ cof : cof*2]
        parents2 = list (sorted_pop.items()) [ self.pop_number-cof : self.pop_number]
        print("Select")

        i = 0
        for pop in sorted_pop.values():
            if random() > 0.5:
                pop[0] = parents1[i][1][0]
                pop[1] = parents2[i][1][1]
                pop[2] = 0
            else:
                pop[0] = parents2[i][1][0]
                pop[1] = parents1[i][1][1]
                pop[2] = 0
            i+=1
            if i >= cof:
                break
        
        self.population = sorted_pop
    
    
    def mutation(self, cur_gen):
        print("Mutation")
        for pop in self.population.values():
            if random() < self.mut_chance:
                pop[0] += (random() - 0.5) * ((self.generations - cur_gen)/self.generations)
            if random() < self.mut_chance:
                pop[0] += (random() - 0.5) * ((self.generations - cur_gen)/self.generations)


#Схема запуска алгоритма
#genetic = GeneticAlgorithmL3(rosen,50)
#genetic.generate_start_population(5,5)
#for i in range(50):
#    genetic.simulation()
#    print(genetic.population)
#    genetic.select()
#    genetic.mutation(i)
#    print(genetic.population)
