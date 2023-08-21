from data import MENU, resources, prices, coins
import os

class coffe_machine:
    '''This is a coffe machine class'''
    
    def __init__(self) -> None:
        '''This is a constructor'''
        self.MENU = MENU
        self.resources = resources
        self.prices = prices
        self.coins = coins
    
    def main(self) -> None:
        '''This is a main method which executes the program'''

        print('What would you like? (espresso/latte/cappuccino):')
        print('=' * 30)
        [print(f'{k} = {v}') for k, v in self.prices.items()]
        response = input()

        os.system('cls') if os.name == 'nt' else os.system('clear')
        
        if response == 'off':
            exit()
        elif response == 'report':
            print('Report:')
            [print(f'{k} = {v}')   for k, v in self.resources.items()]
            print('=' * 30)
        elif response in self.MENU.keys():
            self.check(response)
            self.coin_transaction(response)
        else:
            print('Invalid input, try again.\n')
            self.main()

    def check(self, coffee_name) -> None:
        '''This method checks if there is enough resources to make a coffe'''

        indicator = True
        for i in self.MENU[f'{coffee_name}']['ingredients']:
            if self.MENU[f'{coffee_name}']['ingredients'][f'{i}'] > self.resources[f'{i}']:
                indicator = False

        if indicator:
            print('Please insert coins.')
        else:
            print('Sorry there is not enough resources.\n')
            self.main()
    
    def coin_process(self) -> float:
        '''This method processes the coins inserted by the user'''
        sum = 0
        
        for i in self.coins:
            print(i + ' =', end='')
            sum += float(input()) * self.coins[i]

        return sum
    
    def coin_transaction(self, coffe_name) -> None:
        '''This method checks if the user has inserted enough money to buy a coffe'''
        sam = self.coin_process()

        if sam < self.prices[f'{coffe_name}']:
            print('Sorry, that is not enough money. Money refunded.\n')
        else:
            difference = sam - self.prices[f'{coffe_name}']
            print('Here is your change = ' + f'{difference}')
            print(f'Here is your {coffe_name} ☕ Enjoy!')
            print('=' * 30)
            self.make_coffe(coffe_name)
    
    def make_coffe(self, coff_name) -> None:
        '''This method makes a coffe and reduces the resources'''
        for i in self.MENU[f'{coff_name}']['ingredients']:
            self.resources[f'{i}'] -= self.MENU[f'{coff_name}']['ingredients'][f'{i}']

coffeMachine = coffe_machine()

while True:
    coffeMachine.main()

