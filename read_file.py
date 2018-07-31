import pickle
import matplotlib.pyplot as plt

pkl_file = open('data.pkl', 'rb')
data1 = pickle.load(pkl_file)
pkl_file.close()

plt.plot(data1)
plt.show()

