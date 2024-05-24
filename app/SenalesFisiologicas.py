import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

import matplotlib.pyplot as plt

# Simular algunos datos fisiológicos
np.random.seed(0)
t_hrv = np.linspace(0, 10, 1000)  # 10 segundos de señales, muestreadas a 100 Hz

data = {
    'HRV': np.random.normal(60, 10, size=t_hrv.shape),  # Variabilidad de la frecuencia cardíaca
    'EDA': np.random.normal(1, 0.1, size=t_hrv.shape),  # Actividad electrodérmica
    'Emotion': np.random.choice(['Happy', 'Sad', 'Stressed'], size=t_hrv.shape)  # Estado emocional
}

df = pd.DataFrame(data)

# Ver los primeros datos
print(df.head())
# Visualizar datos
t_hrv = np.linspace(0, 10, 1000)  # 10 segundos de señales, muestreadas a 100 Hz
hrv = df['HRV']
plt.figure(figsize=(12, 6))

# Gráfico para HRV
plt.subplot(2, 1, 1)  # 2 filas, 1 columna, 1er subplot
plt.plot(t_hrv, hrv, label='HRV')
plt.title('Variabilidad de la Frecuencia Cardíaca (HRV)')
plt.xlabel('Tiempo (s)')
plt.ylabel('HRV (unidades arbitrarias)')
plt.legend()

# Gráfico para EDA
t_eda = np.linspace(0, 10, 1000)
eda=df['EDA']
plt.subplot(2, 1, 2)  # 2 filas, 1 columna, 2do subplot
plt.plot(t_eda, eda, label='EDA', color='r')
plt.title('Actividad Electrodérmica (EDA)')
plt.xlabel('Tiempo (s)')
plt.ylabel('EDA (microsiemens)')
plt.legend()


#preprocesamiento de datos
# Preparar datos para el modelo
X = df[['HRV', 'EDA']]  # características
y = df['Emotion']  # etiquetas


# Dividir los datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Entrenar un clasificador de bosque aleatorio
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Predecir emociones en el conjunto de prueba
y_pred = model.predict(X_test)

# Evaluar el modelo
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2f}")

plt.tight_layout()
plt.show()