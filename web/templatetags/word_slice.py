from django import template

register = template.Library()

@register.filter
def word_slice(value, start_word, end_word):
    words = value.split()
    start_index = max(0, min(len(words), start_word))
    end_index = max(0, min(len(words), end_word))
    return ' '.join(words[start_index:end_index])

