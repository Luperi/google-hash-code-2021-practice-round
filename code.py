from collections import OrderedDict

filepaths = [
    'a_example',
    'b_little_bit_of_everything.in',
    'c_many_ingredients.in',
    'd_many_pizzas.in',
    'e_many_teams.in'
]


def run_algo(filepath, output_filepath):
    # Using readlines()
    file1 = open(filepath, 'r')
    Lines = file1.readlines()

    count = 0
    pizzas = []
    list_of_ingredients = {}
    pizzas_per_ingredient = {}
    ingredients_per_pizza = {}
    # Strips the newline character
    for line in Lines:
        x = line.split()
        # HEADER
        if count == 0:
            pizzas_number = int(x[0])
            team2 = int(x[1])
            team3 = int(x[2])
            team4 = int(x[3])
        # PIZZA
        else:
            pizza_id = count - 1
            ingredients_number = int(x[0])
            ingredients_per_pizza[pizza_id] = ingredients_number
            pizza_ingredients = {}
            for i in range(1, ingredients_number+1):
                ing = x[i]
                # save pizza
                if ing in pizzas_per_ingredient:
                    pizzas_per_ingredient[ing].append(
                        pizza_id)  # append number of pizza
                else:
                    pizzas_per_ingredient[ing] = [pizza_id]
                if ing in list_of_ingredients:
                    list_of_ingredients[ing] += 1
                else:
                    list_of_ingredients[ing] = 1
                pizza_ingredients[x[i]] = 1
            pizzas.append(pizza_ingredients)
        count += 1

    ordered_list_of_ingredients = dict(
        sorted(list_of_ingredients.items(), key=lambda item: item[1]))
    ordered_ingredients_per_pizza = dict(
        sorted(ingredients_per_pizza.items(), reverse=True, key=lambda item: item[1]))

    assert(len(pizzas) == pizzas_number)

    pizza_id_ordered_ingredient = list(ordered_ingredients_per_pizza)

    # assign pizzas to teams
    team_pizzas = {
        4: [],
        3: [],
        2: []
    }
    while len(pizza_id_ordered_ingredient) > 3 and team4 > 0:
        ps = []
        for j in range(4):
            ps.append(str(pizza_id_ordered_ingredient[0]))
            del pizza_id_ordered_ingredient[0]
        team_pizzas[4].append(ps)
        team4 -= 1

    while len(pizza_id_ordered_ingredient) > 2 and team3 > 0:
        ps = []
        for j in range(3):
            ps.append(str(pizza_id_ordered_ingredient[0]))
            del pizza_id_ordered_ingredient[0]
        team_pizzas[3].append(ps)
        team3 -= 1

    while len(pizza_id_ordered_ingredient) > 1 and team2 > 0:
        ps = []
        for j in range(2):
            ps.append(str(pizza_id_ordered_ingredient[0]))
            del pizza_id_ordered_ingredient[0]
        team_pizzas[2].append(ps)
        team2 -= 1

    # writing to file
    lines = []
    file1 = open(output_filepath, 'w')
    lines.append(
        str(len(team_pizzas[4]) + len(team_pizzas[3]) + len(team_pizzas[2])))
    for i in range(len(team_pizzas[4])):
        lines.append("\n4 " + ' '.join(team_pizzas[4][i]))
    for i in range(len(team_pizzas[3])):
        lines.append("\n3 " + ' '.join(team_pizzas[3][i]))
    for i in range(len(team_pizzas[2])):
        lines.append("\n2 " + ' '.join(team_pizzas[2][i]))
    file1.writelines(lines)
    file1.close()


def judge(filepath, output_filepath):
    file = open(filepath, 'r')
    lines = file.readlines()
    count = 0
    pizzas = []
    for line in lines:
        x = line.split()
        if count == 0:
            pizzas_number = int(x[0])
            team2 = int(x[1])
            team3 = int(x[2])
            team4 = int(x[3])
        else:
            ingredients_number = int(x[0])
            ingredients = []
            for i in range(1, ingredients_number+1):
                ingredients.append(x[i])
            pizzas.append(ingredients)
        count += 1
    assert(len(pizzas) == pizzas_number)

    # read output file
    tot_score = 0
    filepath = output_filepath
    file = open(filepath, 'r')
    lines = file.readlines()
    count = 0
    for line in lines:
        x = line.split()
        if count == 0:
            num_delivery = int(x[0])
        else:
            team_people = int(x[0])
            ingredients = set()
            for i in range(1, team_people + 1):
                pizza_id = int(x[i])
                pizza_ingredients = pizzas[pizza_id]
                for ingredient in pizza_ingredients:
                    ingredients.add(ingredient)
            tot_score += len(ingredients)**2
        count += 1
    print(tot_score)


for filepath in filepaths:
    run_algo(filepath, filepath+'.out')
    judge(filepath, filepath+'.out')