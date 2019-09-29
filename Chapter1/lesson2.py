intro_text = 'Исследуем статистику различных эмодзи.'
print(intro_text)

instagram = [1.02, 1.69, 0.774, 7.31, 2.36]
print(instagram)

grinning_row = ['Ухмыляюсь', 'Grinning', 2.26, 1.02, 87.3]
print(grinning_row)

emojixpress = [2.26, 19.1, 25.6, 233.0, 15.2, 22.7, 64.6, 87.5, 6.81, 6.0]
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

