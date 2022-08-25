from inspect import TPFLAGS_IS_ABSTRACT


weather_data = {'day':['01-01-2017', '01-02-2017', '01-03-2017', '01-04-2017', '01-05-2017', '01-06-2017'],
                'temperature': [32, 35, 28, 24, 32, 32],
                'windspeed': [6, 7, 2, 7, 4, 2],
                'event': ['rainy', 'sunny', 'snow', 'snow', 'rainy', 'sunny']
}

weather_tplist = []

for i in range(len(list(weather_data.values())[0])):
    tp = []
    j = 0
    for cols, ls in weather_data.items():
        tp.append(ls[i])
        j+=1
    tp = tuple(tp)
    weather_tplist.append(tp)

print(weather_tplist)

