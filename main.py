import pandas as pd #Mengimpor pustaka pandas dengan alias pd untuk memanipulasi dan menganalisis data
import matplotlib.pyplot as plt #Mengimpor pustaka matplotlib dengan alias plt untuk membuat visualisasi data
import scipy.stats as stats #Mengimpor pustaka scipy.stats untuk analisis statistik

#Membaca file CSV "AirQualityUCI.csv" ke dalam DataFrame pandas df dengan menggunakan fungsi read_csv(), dengan pemisah kolom yang ditentukan sebagai ";".
df = pd.read_csv("AirQualityUCI.csv", sep=";")

mean_pH = df["RH"].mean() #Menghitung rata-rata dari kolom "RH" (Relatif Humidity) 
median_pH = df["RH"].median() #Menghitung median dari kolom "RH"
mode_pH = df["RH"].mode()[0] #Menghitung modus dari kolom "RH"
print("Mean RH:", mean_pH) #Mencetak rata-rata kelembaban relatif
print("Median RH:", median_pH) #Mencetak median kelembaban relatif
print("Mode RH:", mode_pH) #Mencetak modus kelembaban relatif

# Simulasi distribusi normal dari kolom "RH"
data_fixed_acidity = df['RH']
# Plot histogram distribusi
plt.hist(data_fixed_acidity, bins=30, density=True, alpha=0.6, color='g')
# Plot distribusi probabilitas
plt.title('Distribusi Normal - Relatif Humidity')
plt.xlabel('Relatif Humidity (RH)')
plt.ylabel('Probabilitas')
plt.show()

# Mengambil sampel acak
sample_quality = df['CO(GT)'].sample(n=100, random_state=1)
# Estimasi rata-rata Karbon Monoksida
mean_quality_estimasi = sample_quality.mean()
print("Estimasi rata-rata Karbon Monoksida:", mean_quality_estimasi)

# Data sampel
sample_high_quality = df[df['RH'] > 6]['AH']
sample_low_quality = df[df['RH'] <= 6]['AH']
# Uji hipotesis
stat, p = stats.ttest_ind(sample_high_quality, sample_low_quality)
if p < 0.05:
    print("Terdapat perbedaan signifikan antara kandungan Karbon Monoksida dengan Absolute Humidity")
else:
    print("Tidak terdapat perbedaan signifikan antara kandungan Karbon Monoksida dengan Absolute Humidity")

variance_volatile_acidity = df['RH'].var()
std_deviaction_volatile_acidity = df['RH'].std()
print("Varians Relative Humidity :", variance_volatile_acidity)
print('Standar Deviasi Relative Humidity :', std_deviaction_volatile_acidity)
