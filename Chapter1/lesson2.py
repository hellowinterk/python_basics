intro_text = 'Исследуем статистику различных эмодзи.'
print(intro_text)

instagram = [1.02, 1.69, 0.774, 7.31, 2.36]
print(instagram)

grinning_row = ['Ухмыляюсь', 'Grinning', 2.26, 1.02, 87.3]
print(grinning_row)

emojixpress = [2.26, 19.1, 25.6, 233.0, 15.2, 22.7, 64.6, 87.5, 6.81, 6.0]
total = 0
total += emojixpress[0]
total += emojixpress[1]
total += emojixpress[2]
total += emojixpress[3]
total += emojixpress[4]
print('{:.2f}'.format(total))
emojixpress_total = 1720

print('Доля эмодзи:')
for element in emojixpress:
	part = element / emojixpress_total
	print('{:.1%}'.format(part))
print()
print('Всего эмодзи: 1.72 млрд')

total = emojixpress[0] + emojixpress[1] + emojixpress[2] + emojixpress[3] + emojixpress[4]
print('{:.2f}'.format(total))

twitter = [87.3, 150.0, 0.0, 2270.0, 264.0, 565.0, 834.0, 432.0, 0.0, 478.0]
print('Твиттер, млн')
print('------------')
for element in twitter:
	print(element)

#total quantity of hands on the selected emojis
total_hands = 0

#emoji 'Kiss'
total_hands += 0
#emoji 'Thumbs Up'
total_hands += 1
#emoji 'ROFL'
total_hands += 0
#emoji 'Thinking'
total_hands += 1
#emoji 'Shrugging'
total_hands += 2
print(total_hands)

emojixpress = [ 2.26, 19.1, 25.6, 233.0, 15.2, 22.7, 64.6, 87.5, 6.81, 6.0, 4.72, 24.7, 21.7, 
10.0, 118.0, 3.31, 23.1, 1.74, 4.5, 0.0333]

emojixpress_total = 1720
selected_total = 0
for element in emojixpress:
	selected_total += element

selected_part = selected_total / emojixpress_total
print('Доля выбранных эмодзи в Emojixpress: {:.1%}'.format(selected_part))

twitter = [87.3, 150.0, 0.0, 2270.0, 264.0, 565.0, 834.0, 432.0, 0.0, 478.0,
198.0, 654.0, 98.7, 445.0, 1080.0, 697.0, 227.0, 0.0, 150.0, 932.0]

twitter_total = 24500
selected_total_twitter = 0
for element in twitter:
	selected_total_twitter += element
selected_part_twitter = selected_total_twitter / twitter_total
print('Доля выбранных эмодзи в Твиттере:{:.1%}'.format(selected_part_twitter))

data = [
['Ухмыляюсь', 2.26, 1.02, 87.3],
['Сияю от радости', 19.1, 1.69, 150.0],
['Катаюсь от смеха', 25.6, 0.774, 0.0],
['Слёзы радости', 233.0, 7.31, 2270.0],
['Подмигиваю', 15.2, 2.36, 264.0]]

tears_of_joy = data[3][2]
print(tears_of_joy)

data = [
    ['Ухмыляюсь', 2.26, 1.02, 87.3],
    ['Сияю от радости', 19.1, 1.69, 150.0],
    ['Катаюсь от смеха', 25.6, 0.774, 0.0],
    ['Слёзы радости', 233.0, 7.31, 2270.0],
    ['Подмигиваю', 15.2, 2.36, 264.0],
    ['Счастлив', 22.7, 4.26, 565.0],
    ['Глаза-сердца', 64.6, 11.2, 834.0],
    ['Целую', 87.5, 5.13, 432.0],
    ['Задумчивость', 6.81, 0.636, 0.0],
    ['Равнодушие', 6.0, 0.236, 478.0],
    ['Солнечные очки', 4.72, 3.93, 198.0],
    ['Громко плачу', 24.7, 1.35, 654.0],
    ['След от поцелуя', 21.7, 2.87, 98.7],
    ['Два сердца', 10.0, 5.69, 445.0],
    ['Сердце', 118.0, 26.0, 1080.0],
    ['Червы', 3.31, 1.82, 697.0],
    ['Класс', 23.1, 3.75, 227.0],
    ['Пожимаю плечами', 1.74, 0.11, 0.0],
    ['Огонь', 4.5, 2.49, 150.0],
    ['Переработка', 0.0333, 0.056, 932.0]
]
print('Название эмодзи | Emogixpress, млн | Instagram, млн | Твиттер, млн')
print('------------------------------------------------------------------')

for element in data:
	print('{: <16} | {: >16.2f} | {: >14.2f} | {: >12.2f}'.format(element[0], element[1], element [2], element[3]))

sum_emojixpress = 0
for row in data:
	sum_emojixpress += row[1]
print(sum_emojixpress)

mean_emojixpress = sum_emojixpress / len(data)
print('{:.2f}'.format(mean_emojixpress))

sum_instagram = 0
for row in data:
	sum_instagram += row[2]
mean_instagram = sum_instagram / len(data)

sum_twitter = 0
for row in data:
	sum_twitter += row[3]
mean_twitter = sum_twitter / len(data)

print('---Средние значения---')
print()
print('Emojixpress, млн | Instagram, млн | Твиттер, млн')
print('------------------------------------------------')
print('{: ^16.2f} | {: ^14.2f} | {: ^12.2f}'.format(mean_emojixpress, mean_instagram, mean_twitter))


#text layout tips
print('|{: >15}|'.format('HEART'))
print('|{: <12.2f}'.format(87.5))

