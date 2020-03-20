class Term():

    def __init__(self, string):
        
        assert type(string) is str, f'Term\'s argument must be a string, not a {type(string)}'
        
        self.string = string

        if 'x' not in self.string:
            self.coefficient = int(string)
        elif string[:string.find('x')] == '':
            self.coefficient = 1
        else:
            self.coefficient = int(string[:string.find('x')])
        
        if string[string.find('x')+1:] == '':
            self.power = 1
        else:
            self.power = int(string[string.find('x')+1:])

    def __repr__(self):
        return self.string

    def derivate(self):

        if self.power == 1:
            return str(self.coefficient)
        elif self.power - 1 == 1:
            return str(self.coefficient * self.power) + 'x'
        else:
            return str(self.coefficient * self.power) + 'x^' + str(self.power - 1)

class Polynomial():

    def __init__(self, terms):
        self.terms = terms

    def __getitem__(self, index):
        return self.terms[index]

    def derivative(self):
        derivative_list = []

        for term in self.terms:

            if 'x' in term.string:

                derivative_list.append(term.derivate())

        return derivative_list

def main():
    pass
    
if __name__ == '__main__':
    main()