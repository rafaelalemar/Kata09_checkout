'''
Kata09: Back to the Checkout
============================
Script created for concretesolutions.com.br in order to demonstrate
the ability of understand the problem and offer a solution

Language: Python 2.6
By Rafael Vidal | rafaelalemar@gmail.com
'''

class Checkout:

    # Scan the product and adds to the total shopping cart
    def scan(self, item):

        if not self.rules.has_key(item):
            return

        self.carrinho.append(item)

        special_qtd = self.rules[item]["special_qtd"]

        # Verify if the product has a discout price
        if special_qtd is not None and self.carrinho.count(item) % special_qtd == 0:
            price = self.rules[item]["special_price"]-((special_qtd-1)*self.rules[item]["price"])
        else:
            price = self.rules[item]["price"]

        # Add the price to the total
        self.total += price

    def __init__(self, rules):
        self.rules = rules
        self.carrinho = []
        self.total = 0