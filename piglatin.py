def piglatin(word):
    if word[0] in 'aeiou':
        return word + 'ay'
    else:
        return word[1:] + word[0] + 'ay'

print(piglatin('abhijeet'))
print(piglatin('cassy'))