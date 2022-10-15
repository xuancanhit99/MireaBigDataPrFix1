import pandas as pd
import matplotlib

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as sts

# 1,2
insurance_raw_data = pd.read_csv("insurance.csv", sep=',')
# print(insurance_raw_data)
# print(insurance_raw_data.describe())
# ---1, 2 end---

# # 3
# fig, ax = plt.subplots(2, 2, figsize=(17, 10))
# ax[0][0].hist(insurance_raw_data['age'], edgecolor='black', color='b', label='age', bins=47)
# ax[0][0].legend()
# ax[0][1].hist(insurance_raw_data['bmi'], edgecolor='black', color='m', label='bmi', bins=40)
# ax[0][1].legend()
# ax[1][0].hist(insurance_raw_data['children'], edgecolor='black', color='c', label='children', bins=6)
# ax[1][0].legend()
# ax[1][1].hist(insurance_raw_data['charges'], edgecolor='black', color='y', label='charges', bins=50)
# ax[1][1].legend()
# plt.show()
# # ---3 end---

# # 4 меры центральной тенденции
# bmi_mean = np.mean(insurance_raw_data['bmi'])
# bmi_moda = sts.mode(insurance_raw_data['bmi'], keepdims=False)
# bmi_med = np.median(insurance_raw_data['bmi'])
#
# charges_mean = np.mean(insurance_raw_data['charges'])
# charges_moda = sts.mode(insurance_raw_data['charges'], keepdims=False)
# charges_med = np.median(insurance_raw_data['charges'])
#
# print('Мода индекса массы тела: ', bmi_moda)
# print('Медиана индекса массы тела: ', bmi_med)
# print('Среднее индекса массы тела: ', round(bmi_mean, 1))
#
# print('Мода расходов: ', charges_moda)
# print('Медиана расходов: ', charges_med)
# print('Среднее расходов: ', round(charges_mean, 1))
#
# # ------

# вычисляем меры разброса индекса массы тела
bmi_scope = insurance_raw_data['bmi'].max() - insurance_raw_data['bmi'].min() # размах
bmi_std = insurance_raw_data['bmi'].std() # стандартное отклонение
bmi_iqr = sts.iqr(insurance_raw_data['bmi'], interpolation='midpoint') # межквартильный размах

print('Размах индекса массы тела: ', bmi_scope)
print('Cтандартное отклонение индекса массы тела: ', round(bmi_std, 2))
print('Межквартильный размах индекса массы тела: ', round(bmi_iqr, 2))

# вычисляем меры разброса расходов
charges_scope = insurance_raw_data['charges'].max() - insurance_raw_data['charges'].min() # размах
charges_std = insurance_raw_data['charges'].std() # стандартное отклонение
charges_iqr = sts.iqr(insurance_raw_data['charges'], interpolation='midpoint') # межквартильный размах

print('Размах расходов: ', round(charges_scope, 2))
print('Cтандартное отклонение расходов: ', round(charges_std, 2))
print('Межквартильный размах расходов: ', round(charges_iqr, 2))

# -------

labels_name_central_trend = ['Мода', 'Медиана', 'Среднее']
labels_name_scatter = ['Размах', 'Станд. откл.', 'Ме  ук']


# ---4 end---
