# A Weather Outfit Picker that asks about 
# temperature
# rain,
#  wind,
#  and 
# puddles,
#  then uses if and if-else statements
#  to decide what outfit, 
# umbrella, 
# windbreaker, 
# and 
# shoes to wear,
#  all while keeping every block properly indented.






print('Hey!!!!!!!!!!!!!!!!!!!!!!!!1')
print('Lets choose an ideal drees for todays weather.')

temp = int(input('What is the temperaure of todays weather in celcius??'))
rain = input('Did it rain today???"In Yes or No"')
wind = input('How is the wind now?=>Normal/Frosting/Extreme')

if temp>26<35:
    print('As the weather is natural You can wear a normal \n T-Shirt and a Jeans')
elif temp<35:
    print('As the weather is hot enough,You just wear a \n thin shirt and a pant  ')
    print('Take an umbrella to avoid heavy sunlight')
else:
    print('There is cold enough to wear a \n thick  Hoody and trouser ')

if rain=='Yes':
    puddles = input("Is there puddles in your way?=>Yes or NO")
    print('So you should wear boots')
    print('Take an umbrella')
    print('If possible , wear a raincoat')
    print('Wear off-white pant as if it can be covered with mud quickly')
else:
    print("So as the weather is sunny and clean wear \n pale-green pant and gray shirt")
    print('Also no need of umbrella.')
    print('Wear a brown shoe')

if wind=="Normal":
    print('As the wind is calm \n you can go outside showing your nice dress-up')
elif wind=="Frosting":
    print('If you have problems with cold \n    You sholud wear a windbreaker \n to avoid breeze')
elif wind=="Extreme":
    print("There is an estreme airspeed outside \n So remember to wear a windbreaker tightly")




