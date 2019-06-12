#AUTHOR = @FARUK
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
#file = open('BPM.csv','r')
dataset = pd.read_csv('BPMs.csv')



X = dataset.iloc[:,[2,3]].values

kmeans=KMeans(n_clusters=4,init='k-means++',random_state=0)
y_kmeans=kmeans.fit_predict(X)
plt.scatter(X[y_kmeans==0,0],X[y_kmeans==0,1],s=30,c='red',label='Smoking and not doing Sport')
plt.scatter(X[y_kmeans==1,0],X[y_kmeans==1,1],s=30,c='blue',label='Smoking and doing Sport')
plt.scatter(X[y_kmeans==2,0],X[y_kmeans==2,1],s=30,c='green',label='not Smoking and doing Sport')
plt.scatter(X[y_kmeans==3,0],X[y_kmeans==3,1],s=30,c='red',label='not Smoking and not doing Sport')    


plt.scatter(kmeans.cluster_centers_[:,0],kmeans.cluster_centers_[:,1],s=300,c='yellow',label='Center Point')

plt.title('Heart Driver')
plt.xlabel('Yas Araliklari')
plt.ylabel('Nabiz Degerleri')

plt.legend()
plt.show()