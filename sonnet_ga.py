import random

# === Paste Functions Below Here ===



# === Paste Functions Above Here ===

# ==== Main Program Below ====
sonnet_str='Shall I compare thee to a summers day'.upper()
sonnet_size = len(sonnet_str)

gene_alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ '
num_mutations = int(sonnet_size*0.05)

pop = make_population(200, sonnet_size, gene_alphabet)
map_fitness(pop, sonnet_str)
best = get_fittest(pop)
print ('0 : ' + best[0])

generation = 0
while best[0] != sonnet_str:

    new_pop = [best]
    for individiual in range(len(pop)):
        parent1 = pick_parent(pop)
        parent2 = pick_parent(pop)
        offspring = reproduce(parent1, parent2, num_mutations, gene_alphabet)
        new_pop.append([offspring, 0])
        
    pop = new_pop
    generation = generation + 1
    
    map_fitness(pop, sonnet_str)
    best = get_fittest(pop)
    print (str(generation) + ': ' + best[0])