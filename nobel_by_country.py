import json
import matplotlib.pyplot as plt

with open('data/Nobel Prize by Country.json') as f:
    data_prize = json.load(f)["countries"] 

countries =[]
for i in range(len(data_prize)):
    if "code" in data_prize[i]:
        countries.append(data_prize[i]['code'])
    else:
        pass
print ('country_codes=', countries)

new_dict = {}
for i in range(len(data_prize)):
    if "code" in data_prize[i]:
        if data_prize[i]['code'] not in new_dict:
            new_dict[data_prize[i]['code']] = 1
        else: 
            new_dict[data_prize[i]['code']] += 1 
print ('new_dict=', new_dict)

freq_country = []
for k,v in new_dict.items():
    freq_country.append(v)
print ('timesCountry =', freq_country)

fig, ax = plt.subplots()
ax.set(
    xlabel='Country Code',
    ylabel='Frequency of Nobel Prize Award',
    title='Frequency of Nobel Prize Award by Country'
)

ax.bar(countries[0:17] , freq_country[0:17] )
plt.show()