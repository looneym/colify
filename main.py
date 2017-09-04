spain = ["madrid", "barcelona", "bilbao", "Malaga"]
italy = ["rome", "florence", "milan", "venice", "palermo", "padua"]
france = ["paris", "lyon", "toulouse", "nantes"]
countries = {}
countries['spain'] = spain
countries['italy'] = italy
countries['france'] = france

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

class Colify():

    def __init__(self, user_data):
        self.user_data = user_data
        self.headers = user_data.keys()
        self.columns = user_data.values()

    def total_width(self):
        return len(self.columns) * self.max_width()      

    def max_rows(self):
        column_lengths = []
        for column in self.user_data.values():
            column_lengths.append(len(column))
        return max(column_lengths)   

    def max_width(self):
        column_widths = []
        for column in self.columns:
            for row in column:
                column_widths.append(len(row))
        return max(column_widths)        

    def output_string(self):
        s= '{'
        s+=':>'
        s+=str(self.max_width())
        s+='} | '
        return s

    def print_line(self):
        output =""
        for i in range(0, self.total_width(), 1):
            output += ' '
        print output

    def print_headers(self):
        output = '| '
        for header in self.headers:
            output += self.output_string()
        print color.UNDERLINE \
            + output.format(*[ word.upper() for word in self.headers]) \
            + color.END
        
    def print_body(self):      
        for i in range(0, self.max_rows() -1 , 1):
            output = '| '
            values = []
            for column in self.user_data.values():
                try:
                    values.append(column[i])
                except IndexError:
                    pass     
            for value in values:   
                output += self.output_string()     
            print output.format(*values)

c = Colify(countries)
c.print_headers() 
c.print_body()




