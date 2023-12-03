import numpy as np
import pandas as pd


from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report


def detectar_cardio(caracteristicas):

    # Carregando o conjunto de dados da base cardiovascular.
    df = pd.read_csv('./cardio_train.csv', sep=';')

    # Ajustando os valores incorretos na base de dados
    for x in df['ap_hi'].unique():
        
        if x > 300 and len(str(x)) <= 4:
            df['ap_hi'].replace(x, int(x/10), inplace=True)
            
        if x > 300 and len(str(x)) == 5:
            df['ap_hi'].replace(x, int(x/100), inplace=True)
            
    for x in df['ap_lo'].unique():
        if x > 300 and len(str(x)) == 3:
            df['ap_lo'].replace(x, int(x/10), inplace=True)
            
        if x > 300 and len(str(x)) == 4:  
            if int(x/10) > 190:
                df['ap_lo'].replace(x, int(x/100), inplace=True)
            else:
                df['ap_lo'].replace(x, int(x/10), inplace=True)
                
        if x > 300 and len(str(x)) == 5:
            df['ap_lo'].replace(x, int(x/100), inplace=True)
            
    df['age'] = df['age'] / 365
    df['age'] = df['age'].astype('int64')


    X = df[['age','weight','ap_hi','ap_lo','cholesterol']] # Matriz de características
    y = df.cardio  # Vetor de rótulos

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    # Normalização das características
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    k = 20  # Valor de K (número de vizinhos)
    knn = KNeighborsClassifier(n_neighbors=k, metric='euclidean', algorithm='brute')
    knn.fit(X_train, y_train)

    y_pred = knn.predict(X_test)

    carac_padronizados = scaler.transform(caracteristicas)

    # Realize a previsão usando o modelo KNN
    previsao = knn.predict(carac_padronizados)

    # Mapeie o resultado da previsão de volta para a descrição do possivel resultado da situação do coração.
    mapeamento_classes = {
        0: 'Conforme análise, não temos ríscos de doenças cardíacas no momento.',
        1: 'Conforme análise, temos ríscos de doenças cardíacas.',
    }
    return mapeamento_classes[previsao[0]], previsao[0]

#Idade, Peso, Pressão Arterial sistólica, Pressão arterial diastólica, colesterol
caracteristicas = [[25,90,200,200,90]]
resultado, indica = detectar_cardio(caracteristicas)
print(resultado)
print(indica)
