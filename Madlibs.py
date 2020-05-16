from os import listdir, path

madlib_path = 'Madlibs'

items = listdir(madlib_path)
templates = []
for item in items:
    item_path = path.join(madlib_path, item)
    if path.isfile(item_path) and item.casefold().endswith('.txt'):
        templates.append(item)

template_names = [t[:-4] for t in templates]

print('Choose a story:')
for x in range(0, len(template_names)):
    print('{0}: {1}'.format(x + 1, template_names[x]))

story_index = 0
while not story_index:
    try:
        story_index = int(input('Choose a story number? '))
        if story_index < 1 or story_index > len(template_names):
            story_index = 0
    except ValueError:
        pass # they must not have typed a number

story = template_names[story_index - 1]

print('\n' + story)

template_filepath = path.join(madlib_path, story + '.txt')
template_file = open(template_filepath, 'r')

words = []
while True:
    word_description = template_file.readline()
    if word_description.strip() == '--begin--':
        break
    word = input('Enter a {0}? '.format(word_description.strip()))
    words.append(word)

story_format_string = template_file.read()
print(story_format_string.format(*words))


