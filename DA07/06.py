# from sklearn.preprocessing import LabelEncoder
import numpy as np
from sklearn.preprocessing import OneHotEncoder

from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import minmax_scale

people = np.array(["male", "male", "female", "female", "male", "male", "female"]).reshape((-1, 1))

encoder = OneHotEncoder()
people_encode = encoder.fit_transform(people)
print(people_encode)
# print(encoder.inverse_transform([1, 1, 0, 0, 1, 1, 0]))