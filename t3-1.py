import pandas as pd
import matplotlib

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np

# 1
operating_systems_raw_data = pd.read_csv("operating-systems.csv", sep=';')

# 2
# # Вывести информацию о данных при помощи методов .info(), .head(). Проверить данные на наличие пустых значений
print(operating_systems_raw_data.head())
print(operating_systems_raw_data.info())

# Check data for empty values
print(operating_systems_raw_data.empty)
print(operating_systems_raw_data)

###
# operating_systems_raw_data['Date'] = (pd.to_datetime(operating_systems_raw_data['Date'], format='%b %y')).dt.year
###

#
# # ---3---
# # Построить столбчатую диаграмму (.bar)
# labels = list(map(str, list(operating_systems_raw_data['Year']))) # метка
# win = operating_systems_raw_data['Windows']
# mac = operating_systems_raw_data['macOS']
# linux = operating_systems_raw_data['Linux']
# chromeOS = operating_systems_raw_data['ChromeOS']
# others = operating_systems_raw_data['Others']
# w = 0.6 #ширина
# plt.figure(figsize=(16, 9))
# plt.bar(labels, win, color='b', width=w)
# plt.bar(labels, mac, bottom=win, color='r', width=w)
# plt.bar(labels, chromeOS, bottom=mac + win, color='m', width=w)
# plt.bar(labels, linux, bottom=mac + win + chromeOS, color='c', width=w)
# plt.bar(labels, others, bottom=mac + win + chromeOS + linux, color='y', width=w)
# plt.ylabel('Percent (%)', fontsize=16)
# plt.ylim(0, 119)
# plt.yticks(np.arange(0, 101, 10), size=14)
#
# plt.xlabel('Year', fontsize=16)
# plt.xticks(rotation=45, size=14)
# # plt.margins(0.1)
# # plt.subplots_adjust(left=0, bottom=0, right=1, top=1, wspace=0, hspace=0)
#
# plt.legend(list(operating_systems_raw_data.columns)[1:], loc='upper center', ncol=2)
# plt.title("Computer operating system market share from 2013 to 2022", fontsize=20)
# plt.show()

# # ---4 Start---
# # Построить круговую диаграмму,
# operating_systems_2021_data = operating_systems_raw_data[operating_systems_raw_data.Year == 2021]
#
# # Swap 2 columns
# # columns_titles = ['Year', 'Windows', 'ChromeOS', 'macOS', 'Linux', 'Others']
# # operating_systems_2021_data = operating_systems_2021_data.reindex(columns=columns_titles)
# # print(operating_systems_2021_data)
#
# labels = list(operating_systems_2021_data.columns)[1:]
#
# colors = ['b', 'r', 'm', 'c', 'y']
# explode = [0, 0, 0, 0, 0.2]
# values = list(operating_systems_2021_data.iloc[0])[1:]
# plt.figure(figsize=(12, 12))
# plt.title('Computer operating system market share as of 2021', fontsize=20)
# plt.pie(values, colors=colors, labels=labels, labeldistance=1.2, autopct='%1.1f%%', pctdistance=0.5, rotatelabels=True,
#         explode=explode,
#         textprops={'fontsize': 14})
# plt.show()
# # ---4 End---


# # 5 Построить линейный график с накопленными значениями количественного показателя от даты (названия)
# fig = plt.figure('График с заданными параметрами', figsize=(10, 10))  # назВание и размер Внешних границ рисунка
# plt.grid(True, color='azure')  # Включаем сетку у графика
# plt.title('Computer operating system market share from 2013 to 2022', fontsize=15)  # назВание графика и его размер
# plt.xlabel('Year', fontsize=12)  # подпись оси х и её размер
# plt.ylabel('Percent (%)', fontsize=12)  # подпись оси у и её размер
# plt.xticks(np.arange(start=2013, stop=2023, step=1), rotation=45, size=10)  # изменение шага меток оси Х,
# plt.ylim(0, 101)
# plt.yticks(np.arange(0, 101, 10), size=10)
# plt.plot(operating_systems_raw_data['Year'],  # значения для оси Х
#          operating_systems_raw_data['Windows'],  # значения для оси Y
#          marker='.',  # стиль меток на функции
#          color='blue',  # цВет функции
#          label='Windows',
#          markerfacecolor='darkblue',  # оснобной цвет метки
#          markeredgecolor='black',  # цВет контура метки
#          linewidth=2,  # толщина линии функции
#          markersize=3)  # размер метки функци
#
# plt.plot(operating_systems_raw_data['Year'],
#          operating_systems_raw_data['macOS'],
#          marker='.',
#          color='r',
#          label='macOS',
#          markerfacecolor='darkblue',
#          markeredgecolor='black',
#          linewidth=2,
#          markersize=3)
# plt.plot(operating_systems_raw_data['Year'],
#          operating_systems_raw_data['Linux'],
#          marker='.',
#          color='m',
#          label='Linux',
#          markerfacecolor='darkblue',
#          markeredgecolor='black',
#          linewidth=2,
#          markersize=3)
# plt.plot(operating_systems_raw_data['Year'],
#          operating_systems_raw_data['ChromeOS'],
#          marker='.',
#          color='c',
#          label='ChromeOS',
#          markerfacecolor='darkblue',
#          markeredgecolor='black',
#          linewidth=2,
#          markersize=3)
# plt.plot(operating_systems_raw_data['Year'],
#          operating_systems_raw_data['Others'],
#          marker='.',
#          color='y',
#          label='Others',
#          markerfacecolor='darkblue',
#          markeredgecolor='black',
#          linewidth=2,
#          markersize=3)
# plt.legend(loc='center left', ncol=2)
# plt.show()
# # ---5 end---


# # ---6 Start---
# # Построить ящик с усами для количества продаж, сохранив оформление с предыдущих графиков
# fig = plt.figure('Диаграмма ящик с усами', figsize=(12, 12))
# plt.title("Computer operating system market share from 2013 to 2022", fontsize=20)
# operating_systems_data_for_boxplot = operating_systems_raw_data[['Windows', 'macOS', 'Linux', 'ChromeOS', 'Others']]
# labels = list(operating_systems_data_for_boxplot.columns)
# plt.grid(True)
# plt.xlabel('Operating System Name', fontsize=12)
# plt.ylim(0, 101)
# plt.yticks(np.arange(0, 101, 10), size=10)
# plt.ylabel('Percent (%)', fontsize=12)
# plt.boxplot(operating_systems_data_for_boxplot,
#             meanline=True,# average line
#             showmeans=True,# show average line
#             labels=labels,
#             widths=0.4)
# plt.show()
# # ---6 End---


# ---7 Start---
# Постараться создать аналогичные графики с использованием библиотеки matplotlib.
fig, (ax1, ax2, ax3, ax4, ax5) = plt.subplots(1, 5, figsize=(25, 8))
x_labels = np.arange(start=2013, stop=2023, step=1)

ax1.plot(operating_systems_raw_data['Year'],  # значения для оси Х
         operating_systems_raw_data['Windows'],  # значения для оси Y
         marker='.',  # стиль меток на функции
         color='b',  # цВет функции
         label='Windows',
         markerfacecolor='darkblue',  # оснобной цвет метки
         markeredgecolor='black',  # цВет контура метки
         linewidth=2,  # толщина линии функции
         markersize=3)
ax1.set_xlabel('Year', fontsize=12)
ax1.set_xticks(x_labels)
ax1.set_xticklabels(x_labels, rotation=60)
ax1.set_ylabel('Percent (%)', fontsize=12)
ax1.set_yticks(np.arange(start=75, stop=92, step=1))
ax1.legend(loc='upper center')
ax1.set_title("Windows")

ax2.plot(operating_systems_raw_data['Year'],  # значения для оси Х
         operating_systems_raw_data['macOS'],  # значения для оси Y
         marker='.',  # стиль меток на функции
         color='r',  # цВет функции
         label='macOS',
         markerfacecolor='darkblue',  # оснобной цвет метки
         markeredgecolor='black',  # цВет контура метки
         linewidth=2,  # толщина линии функции
         markersize=3)
ax2.set_xlabel('Year', fontsize=12)
ax2.set_xticks(x_labels)
ax2.set_xticklabels(x_labels, rotation=60)
ax2.set_ylabel('Percent (%)', fontsize=12)
ax2.set_yticks(np.arange(start=7, stop=20, step=1))
ax2.legend(loc='upper center')
ax2.set_title("macOS")

ax3.plot(operating_systems_raw_data['Year'],  # значения для оси Х
         operating_systems_raw_data['Linux'],  # значения для оси Y
         marker='.',  # стиль меток на функции
         color='m',  # цВет функции
         label='Linux',
         markerfacecolor='darkblue',  # оснобной цвет метки
         markeredgecolor='black',  # цВет контура метки
         linewidth=2,  # толщина линии функции
         markersize=3)
ax3.set_xlabel('Year', fontsize=12)
ax3.set_xticks(x_labels)
ax3.set_xticklabels(x_labels, rotation=60)
ax3.set_ylabel('Percent (%)', fontsize=12)
ax3.set_yticks(np.arange(start=1.25, stop=2.75, step=0.25))
ax3.legend(loc='upper center')
ax3.set_title("Linux")

ax4.plot(operating_systems_raw_data['Year'],  # значения для оси Х
         operating_systems_raw_data['ChromeOS'],  # значения для оси Y
         marker='.',  # стиль меток на функции
         color='c',  # цВет функции
         label='ChromeOS',
         markerfacecolor='darkblue',  # оснобной цвет метки
         markeredgecolor='black',  # цВет контура метки
         linewidth=2,  # толщина линии функции
         markersize=3)
ax4.set_xlabel('Year', fontsize=12)
ax4.set_xticks(x_labels)
ax4.set_xticklabels(x_labels, rotation=60)
ax4.set_ylabel('Percent (%)', fontsize=12)
ax4.set_yticks(np.arange(start=0, stop=3.25, step=0.25))
ax4.legend(loc='upper center')
ax4.set_title("ChromeOS")

ax5.plot(operating_systems_raw_data['Year'],  # значения для оси Х
         operating_systems_raw_data['Others'],  # значения для оси Y
         marker='.',  # стиль меток на функции
         color='y',  # цВет функции
         label='Others',
         markerfacecolor='darkblue',  # оснобной цвет метки
         markeredgecolor='black',  # цВет контура метки
         linewidth=2,  # толщина линии функции
         markersize=3)
ax5.set_xlabel('Year', fontsize=12)
ax5.set_xticks(x_labels)
ax5.set_xticklabels(x_labels, rotation=60)
ax5.set_ylabel('Percent (%)', fontsize=12)
ax5.set_yticks(np.arange(start=0, stop=5, step=0.5))
ax5.legend(loc='upper center')
ax5.set_title("Others")
fig.tight_layout(pad=5.0)

plt.show()
