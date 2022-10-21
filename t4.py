import random

import pandas as pd
import matplotlib

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as sts
import seaborn as sns
import statistics as st

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
# bmi_mode = sts.mode(insurance_raw_data['bmi'], keepdims=False)
# bmi_med = np.median(insurance_raw_data['bmi'])
#
# charges_mean = np.mean(insurance_raw_data['charges'])
# charges_mode = sts.mode(insurance_raw_data['charges'], keepdims=False)
# charges_med = np.median(insurance_raw_data['charges'])
#
# print('Мода индекса массы тела: ', bmi_mode)
# print('Медиана индекса массы тела: ', bmi_med)
# print('Среднее индекса массы тела: ', round(bmi_mean, 1))
#
# print('Мода расходов: ', charges_mode)
# print('Медиана расходов: ', charges_med)
# print('Среднее расходов: ', round(charges_mean, 1))
#
# # ------
#
# # вычисляем меры разброса индекса массы тела
# bmi_scope = insurance_raw_data['bmi'].max() - insurance_raw_data['bmi'].min()  # размах
# bmi_std = insurance_raw_data['bmi'].std()  # стандартное отклонение
# bmi_iqr = sts.iqr(insurance_raw_data['bmi'], interpolation='midpoint')  # межквартильный размах
#
# print('Размах индекса массы тела: ', bmi_scope)
# print('Cтандартное отклонение индекса массы тела: ', round(bmi_std, 2))
# print('Межквартильный размах индекса массы тела: ', round(bmi_iqr, 2))
#
# # вычисляем меры разброса расходов
# charges_scope = insurance_raw_data['charges'].max() - insurance_raw_data['charges'].min()  # размах
# charges_std = insurance_raw_data['charges'].std()  # стандартное отклонение
# charges_iqr = sts.iqr(insurance_raw_data['charges'], interpolation='midpoint')  # межквартильный размах
#
# print('Размах расходов: ', round(charges_scope, 2))
# print('Cтандартное отклонение расходов: ', round(charges_std, 2))
# print('Межквартильный размах расходов: ', round(charges_iqr, 2))
#
# # -------

# labels_name_central_trend = ['Мода', 'Медиана', 'Среднее']
# labels_name_scatter = ['Размах', 'Станд. откл.', 'Межквартильный размах']
#
# bmi_central_trend = [bmi_mode.mode, bmi_med, bmi_mean]
# charges_central_trend = [charges_mode.mode, charges_med, charges_mean]
#
# bmi_scatter = [bmi_scope, bmi_std, bmi_iqr]
# charges_scatter = [charges_scope, charges_std, charges_iqr]
#
# fix, ax = plt.subplots(2, 2, figsize=(17, 10))
# ax[0][0].bar(labels_name_central_trend, bmi_central_trend, edgecolor='black', color='b', linewidth=2, width=0.5)
# ax[0][0].grid(alpha=0.4)
# ax[0][0].set_title('Меры центральной тенденции ИМТ', size=18)
#
# ax[0][1].bar(labels_name_central_trend, charges_central_trend, edgecolor='black', color='m', linewidth=2, width=0.5)
# ax[0][1].grid(alpha=0.4)
# ax[0][1].set_title('Меры центральной тенденции расходов', size=18)
#
# ax[1][1].bar(labels_name_scatter, bmi_scatter, edgecolor='black', color='c', linewidth=2, width=0.5)
# ax[1][1].grid(alpha=0.4)
# ax[1][1].set_title('Меры разброса ИМТ', size=18)
#
# ax[1][0].bar(labels_name_scatter, charges_scatter, edgecolor='black', color='y', linewidth=2, width=0.5)
# ax[1][0].grid(alpha=0.4)
# ax[1][0].set_title('Меры разброса расходов', size=18)
# plt.show()
#
# # ---4 end---


# # ---5---
# plt.figure(figsize=(7, 7))
# plt.boxplot([insurance_raw_data['age'],
#              insurance_raw_data['bmi']],
#             vert=False,
#             labels=['age', 'bmi'])
# plt.show()

# # ------
# plt.figure(figsize=(8, 8))
# plt.boxplot(insurance_raw_data['children'], vert=False, labels=['children'])
# plt.show()

# # ---
#
# plt.figure(figsize=(8,8))
# plt.boxplot(insurance_raw_data['charges'], vert=False, labels=['charges'])
# plt.show()

# ---6---
## n = 20
## n = 50
# n = 200
# samples_num = 300
# t = tuple(insurance_raw_data['bmi'])
# mean_list = []
#
# for i in range(samples_num):
#     data_sample = random.sample(t, n)
#     mean_list.append(np.mean(data_sample))
#
# sns.displot(mean_list, kde=True)
# print('Среднее распределения: ', np.mean(mean_list))
# print('Стандартное отклонение распределеия: ', st.pstdev(mean_list))


# # ---6 end---
# mean_charges = []
# mean_bmi = []
#
# charges_conf_int95 = sts.norm.interval(0.95, loc=mean_charges, scale=sts.sem(insurance_raw_data['charges']))
# charges_conf_int99 = sts.norm.interval(0.99, loc=mean_charges, scale=sts.sem(insurance_raw_data['charges']))
#
# print('95% доверительный интервал для расходов: ', charges_conf_int95)
# print('99% доверительный интервал для расходов: ', charges_conf_int99)
#
# bmi_conf_int95 = sts.norm.interval(0.95, loc=mean_bmi, scale=sts.sem(insurance_raw_data['bmi']))
# bmi_conf_int99 = sts.norm.interval(0.99, loc=mean_bmi, scale=sts.sem(insurance_raw_data['bmi']))
#
# print('95% доверительный интервал для ИМТ: ', bmi_conf_int95)
# print('99% доверительный интервал для ИМТ: ', bmi_conf_int99)

# # ---7---
# bmi_sample1 = insurance_raw_data['bmi'].sample(300)
# bmi_sample2 = insurance_raw_data['bmi'].sample(300)
# print('KS-тест ИМТ: ', sts.kstest(bmi_sample1, bmi_sample2))
#
# charges_sample1 = insurance_raw_data['charges'].sample(300)
# charges_sample2 = insurance_raw_data['charges'].sample(300)
# print('KS-тест расходов: ', sts.kstest(charges_sample1, charges_sample2))


# qq_plot = sns.jointplot(
#     x=np.random.normal(size=1338),
#     y=insurance_raw_data['bmi'],
#     kind='reg',
#     color='chocolate',
#     line_kws={'lw': 1, 'color': 'black'}
# )


qq_plot_charges = sns.jointplot(
    x=np.random.normal(size=1338),
    y=insurance_raw_data['charges'],
    kind='reg',
    color='midnightblue',
    line_kws={'lw': 1, 'color': 'black'}
)

