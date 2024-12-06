def parse_input(filename):
    with open (filename, 'r') as file:
        clean_rules =[]
        input = file.read().strip()
        rules, updates = input.split('\n\n')
        for rule in rules.split('\n'):
            a, b = map(int,rule.split('|'))
            clean_rules.append((a,b))
        clean_updates = [list(map(int,update.split(','))) for update in updates.split('\n')]
    return clean_rules, clean_updates

# def rule_graph(rules):
#     graph = {}
#     for rule in rules.split('\n'):
#         first, second = map(int,rule.split('|'))
#         graph.setdefault(first, set()).add(second)
#     return graph

# def is_valid_order(updates, graph):
#     is_valid = False
#     valid_mid_pages = []
#     for update in updates.split('\n'):
#         page_num = list(map(int,update.split(',')))
#         for i in range(len(page_num)):
#             for j in range(i+1,len(page_num)):
#                 if page_num[i] in graph and page_num[j] in graph[page_num[i]] and page_num.index(page_num[i]) > page_num.index(page_num[j]):
#                     is_valid = False
#                 else:
#                     is_valid = True
#         if is_valid:
#             middle_index = len(page_num) // 2
#             valid_mid_pages.append(page_num[middle_index])
#     return valid_mid_pages

# def sum_middle_pages(valid_mid_pages):
#     return sum(valid_mid_pages)

def is_valid_update(update,rules):
    indexes ={}
    for i, val in enumerate(update):
        indexes[val] = i
    for x, y in rules:
        if x in indexes and y in indexes and indexes[x] > indexes[y]:
            return False, 0
    return True, update[len(update) // 2]

def sum_middle(updates, rules):
    result = 0
    for update in updates:
        is_valid, middle = is_valid_update(update,rules)
        if is_valid:
            result += middle

    return result

def sorted_upadate(update, rules):
    while True:
        is_sorted = True
        for i in range(len(update)-1):
            if (update[i+1],update[i]) in rules:
                is_sorted = False
                update[i], update[i+1] = update[i+1], update[i]
        if is_sorted:
            return update



def main():
    rules, updates = parse_input("input.txt")
    # graph = rule_graph(rules)
    # mid_pages = is_valid_order(updates, graph)
    # result = sum_middle_pages(mid_pages)
    result = sum_middle(updates,rules)
    print(result)
    res = 0
    for update in updates:
        if is_valid_update(update, rules)[0]:
            continue
        correct_update = sorted_upadate(update,rules)
        res += correct_update[len(correct_update)//2]
    print(res)

if __name__ == '__main__':
    main()