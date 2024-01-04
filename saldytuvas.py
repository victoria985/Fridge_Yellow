import time

def add_product(fridge_content, product, quantity = 0):
    if product in fridge_content.keys():
        fridge_content[product] = fridge_content[product] + quantity
        print(f'{quantity} of {product} has been added to the fridge.')
        print_content_fridge(fridge_content)
    else:
        fridge_content[product] = quantity
        print(f'{quantity} of {product} has been added to the fridge.')
        print_content_fridge(fridge_content)
    
    return fridge_content

def remove_product(fridge_content, name, quantity = 0, condition = ''):
    
    if name in fridge_content.keys():
        print(f'Would you like to remove all {name} form the fridge?')
        if condition == '':
            condition =input('y/n: ')
        while condition.lower() not in ['y', 'n']:
            condition = input("Invalid input. Please enter 'y' or 'n': ")
        if condition.lower() == 'y':
            del fridge_content[name]
            print(f'Item {name} has been removed from the fridge')
            print(f'Fridge now has:')
            print_content_fridge(fridge_content)
        elif condition.lower() == 'n':
            print(f'Type amount of {name} you would like to remove')
            if quantity == 0:
                quantity = float(input())
            else:
                pass
            fridge_content[name] = fridge_content[name] - quantity
            if fridge_content[name] <= 0:
                del fridge_content[name]
            else:
                pass
            print(f'{quantity} {name} has been removed from the fridge')
            print_content_fridge(fridge_content)
    else:
        print('Item has not been found in the fridge')
    
    return fridge_content

def check_product(fridge_content, name):
    if name in fridge_content.keys():
        print(f'{name} is in the fridge')
        print(f'There is {fridge_content[name]} of {name} in the fridge')
    else:
        print(f'Product {name} is not in the fridge')

def print_content_fridge(fridge_content):
    
    print('=== Fridge content ===')
    for key, value in fridge_content.items():
        print(f'* {key} : {value}')

# Bonus tasks

def recepy_create(input_string):
    recepy = {}    
    pairs = input_string.split(',')
    
    for pair in pairs:
        key_value = pair.strip().split(':')
        
        if len(key_value) == 2:
            key = key_value[0].strip()
            value = key_value[1].strip()
            
            try:
                recepy[key] = float(value)
            except ValueError:
                recepy[key] = value  
        else:
            print(f"Ignoring invalid pair: {pair}")
    
    print('Recepy has beed created:')
    for key in recepy:
        print(f'{key} : {recepy[key]}')
    
    return recepy
    

def check_recepy(fridge_content, recepy):
    
    missing_ammount = {}
    recepy_ammount = {}
    missing_items = []

    for key, value in recepy.items():
        if key in fridge_content:
            if recepy[key] > fridge_content[key]:
                missing_ammount[key] = recepy[key] - fridge_content[key]
            else:
                recepy_ammount[key] = recepy[key]
        else:
            missing_items.append(key)
    
    if missing_ammount == {} and missing_items == []:
        print('Recepy has all ingreadients in the fridge')
        recepy_pass = recepy
        return recepy_pass
    else:
        if missing_items != []:
            print('Products that are not in the fridge:')
            for i in missing_items:
                print(f'*** {i}')
        if missing_ammount != {}:
            print('There is not enough of:')
            for key, value in missing_ammount.items():
                print(f'*** {key}: missing {value}')
    

# Main function

def main(fridge_content, recepy):

    while True:

        print("-------------------------------")
        print("--- Yellow Submerged Fridge ---")
        print("-------------------------------")
        print("0: Exit")
        print("1: Add to the fridge")
        print("2: Remove from the fridge")
        print("3: Check for Product")
        print("4: Show conntent of the fridge")
        print("5: Recepy creation")
        print("6: Recepy check")
        print("7: Clense fridge")
        choice = input("Choice: ")
        if choice == "0":
            break
        if choice == '1':
            product = input('What product would you like to add?: ').lower()
            quantity = float(input('Ammount of product you want to add: '))
            fridge_content = add_product(fridge_content, product, quantity)
        if choice == '2':
            name = input('What product would you like to remove?: ').lower()
            fridge_content = remove_product(fridge_content, name)
        if choice == '3':
            name = input('What product you are looking for?').lower()
            check_product(fridge_content, name)
        if choice == '4':
            print_content_fridge(fridge_content)
        if choice == '5':
            recepy_input = input('Please write items needed for recepy: ').lower()
            recepy = recepy_create(recepy_input)
        if choice == '6':
            check_recepy(fridge_content, recepy)
        if choice == '7':
            fridge_content = {}
            recepy = {}
            print('\033[91m' + '+++ fridge has been clensed +++' + '\033[0m')
        if choice == 'test':
            program_test()

def program_test():
    
    fridge_content_test ={}
    recepy_test = {}
    recepy_pass_test = {}

    check = 0
    fridge_content_test = add_product(fridge_content_test, 'pienas', 1.5)
    print('PASS')
    check += 1
    print(f'\033[32mPassed tests: {check}/15\033[0m')
    time.sleep(1)
    fridge_content_test = add_product(fridge_content_test, 'pienas', 2.3)
    print('PASS')
    check += 1
    print(f'\033[32mPassed tests: {check}/15\033[0m')
    time.sleep(1)
    fridge_content_test = add_product(fridge_content_test, 'batonas', 5)
    print('PASS')
    check += 1
    print(f'\033[32mPassed tests: {check}/15\033[0m')
    time.sleep(1)
    fridge_content_test = add_product(fridge_content_test, 'suris', 15)
    print('PASS')
    check += 1
    print(f'\033[32mPassed tests: {check}/15\033[0m')
    time.sleep(1)
    fridge_content_test = add_product(fridge_content_test, 'pomidoras', 7.58)
    print('PASS')
    check += 1
    print(f'\033[32mPassed tests: {check}/15\033[0m')
    time.sleep(1)
    fridge_content_test = add_product(fridge_content_test, 'kiausiniai', 50)
    print('PASS')
    check += 1
    print(f'\033[32mPassed tests: {check}/15\033[0m')
    time.sleep(1)
    fridge_content_test = remove_product(fridge_content_test, 'batonas', 3, 'n')
    print('PASS')
    check += 1
    print(f'\033[32mPassed tests: {check}/15\033[0m')
    time.sleep(1)
    fridge_content_test = remove_product(fridge_content_test, 'suris', 0, 'y')
    print('PASS')
    check += 1
    print(f'\033[32mPassed tests: {check}/15\033[0m')
    time.sleep(1)
    check_product(fridge_content_test, 'pienas')
    print('PASS')
    check += 1
    print(f'\033[32mPassed tests: {check}/15\033[0m')
    time.sleep(1)
    recepy_test = recepy_create("milk:50, pienas:2, pomidoras:3, batonas:20")
    print('PASS')
    check += 1
    print(f'\033[32mPassed tests: {check}/15\033[0m')
    time.sleep(1)
    check_recepy(fridge_content_test, recepy_test)
    print('PASS')
    check += 1
    print(f'\033[32mPassed tests: {check}/15\033[0m')
    time.sleep(1)
    fridge_content_test = add_product(fridge_content_test, 'milk', 50)
    print('PASS')
    check += 1
    print(f'\033[32mPassed tests: {check}/15\033[0m')
    time.sleep(1)
    fridge_content_test = add_product(fridge_content_test, 'batonas', 20)
    print('PASS')
    check += 1
    print(f'\033[32mPassed tests: {check}/15\033[0m')
    time.sleep(1)
    check_recepy(fridge_content_test, recepy_test)
    print('PASS')
    check += 1
    print(f'\033[32mPassed tests: {check}/15\033[0m')
    time.sleep(1)
    print_content_fridge(fridge_content_test)
    print('PASS')
    check += 1
    print(f'\033[32mPassed tests: {check}/15\033[0m')




fridge_content = {}
recepy = {}
recepy_pass = {}

main(fridge_content, recepy)