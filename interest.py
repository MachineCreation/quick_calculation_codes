                                                                                                                        # Inputs

investment = int(input('Enter initial investment. '))
user_interest_input = float(input('Enter interest rate. '))
investment_compounds_every = int(input('Enter the number of months between each interest period '))
term = int(input('Enter term in months. '))

                                                                                                                        # Variables

interest_rate = user_interest_input/100


#print(interest_rate)

term_months = [1]
intrest_by_month = ['Intrest return by period: ']



for i in term_months:
    if i < term:
     i = i + investment_compounds_every
     term_months.append(i)

#print(term_months)

for end_value in term_months:
    investment = float("{:.2f}".format(investment + (investment * interest_rate)))
    intrest_by_month.append(investment)

intrest_by_month = intrest_by_month[:-1]

for a in intrest_by_month:
   print(a)