import pandas as pd
import matplotlib.pyplot as plt

# Dane wejściowe dla silników spalinowych z różnymi paliwami
data = {
    'Silnik': ['Silnik 1', 'Silnik 2', 'Silnik 3'],
    'Moc (kW)': [100, 150, 200],
    'Zużycie biogazu (m3/h)': [10, 15, 20],
    'Zużycie benzyny (l/h)': [8, 12, 16],
    'Zużycie diesla (l/h)': [7, 10, 14],
    'Wartość opałowa biogazu (MJ/m3)': [22.67, 21.05, 23.71],
    'Wartość opałowa benzyny (MJ/l)': [34.2, 34.2, 34.2],
    'Wartość opałowa diesla (MJ/l)': [35.8, 35.8, 35.8]
}

# Tworzenie DataFrame z danymi
df = pd.DataFrame(data)

# Obliczanie dostarczonej energii z paliwa (MJ/h)
df['Dostarczona energia biogazu (MJ/h)'] = df['Zużycie biogazu (m3/h)'] * df['Wartość opałowa biogazu (MJ/m3)']
df['Dostarczona energia benzyny (MJ/h)'] = df['Zużycie benzyny (l/h)'] * df['Wartość opałowa benzyny (MJ/l)']
df['Dostarczona energia diesla (MJ/h)'] = df['Zużycie diesla (l/h)'] * df['Wartość opałowa diesla (MJ/l)']

# Obliczanie energii uzyskanej (MJ/h) (1 kW = 3.6 MJ)
df['Uzyskana energia (MJ/h)'] = df['Moc (kW)'] * 3.6

# Obliczanie efektywności energetycznej (%)
df['Efektywność biogazu (%)'] = (df['Uzyskana energia (MJ/h)'] / df['Dostarczona energia biogazu (MJ/h)']) * 100
df['Efektywność benzyny (%)'] = (df['Uzyskana energia (MJ/h)'] / df['Dostarczona energia benzyny (MJ/h)']) * 100
df['Efektywność diesla (%)'] = (df['Uzyskana energia (MJ/h)'] / df['Dostarczona energia diesla (MJ/h)']) * 100

# Tworzenie wykresu efektywności energetycznej
plt.figure(figsize=(12, 8))
width = 0.2  # Szerokość słupków

# Pozycje słupków
r1 = range(len(df['Silnik']))
r2 = [x + width for x in r1]
r3 = [x + width for x in r2]

plt.bar(r1, df['Efektywność biogazu (%)'], color='blue', width=width, edgecolor='grey', label='Biogaz')
plt.bar(r2, df['Efektywność benzyny (%)'], color='green', width=width, edgecolor='grey', label='Benzyna')
plt.bar(r3, df['Efektywność diesla (%)'], color='red', width=width, edgecolor='grey', label='Diesel')

plt.xlabel('Silnik', fontweight='bold')
plt.xticks([r + width for r in range(len(df['Silnik']))], df['Silnik'])
plt.ylabel('Efektywność energetyczna (%)')
plt.title('Porównanie efektywności energetycznej różnych paliw')
plt.legend()

# Wyświetlanie wykresu
plt.tight_layout()
plt.show()
