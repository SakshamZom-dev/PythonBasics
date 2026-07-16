# print('''Twinkle, twinkle, little star,
# How I wonder what you are!
# Up above the world so high,
# Like a diamond in the sky.''')

letter = '''Hello <|Name|>, welcome to the club
Its dated <|Date|>, when there's a meeting scheduled'''
print(letter.replace("<|Name|>", "Zom").replace("<|Date|>", "Today"))
