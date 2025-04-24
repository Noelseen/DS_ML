import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('/Users/neledauelsberg/Repos/intruduction_ml/sessions/wetter.csv')


df['Datum'] = pd.to_datetime(df['Datum'])
df['Monat'] = df['Datum'].dt.month

sum_temp = df['Temperatur'].sum()
count_temp = df['Temperatur'].count()
avg_temp = sum_temp / count_temp


temp_may_sum = df[df['Monat'] == 5]['Temperatur'].sum()
temp_may_count = df[df['Monat'] == 5]['Temperatur'].count()
avg_temp_may = temp_may_sum / temp_may_count

temp_july_sum = df[df['Monat'] == 7]['Temperatur'].sum()
temp_july_count = df[df['Monat'] == 7]['Temperatur'].count()
avg_temp_july = temp_july_sum / temp_july_count


plt.scatter(df['Monat'], df['Temperatur'])
plt.xlabel('Monat')
plt.ylabel('Temperatur')
plt.title('Temperatur vs Monat')
plt.axhline(y=avg_temp, color='r', linestyle='--', label='Durchschnittstemperatur')
plt.axhline(y=avg_temp_may, color='g', linestyle='--', label='Durchschnitt Mai')
plt.axhline(y=avg_temp_july, color='b', linestyle='--', label='Durchschnitt Juli')
plt.legend()
plt.show()
