def get_answer(prompt, valid_lowercase_answers):
    valid = False
    while not valid:
        answer = input(prompt).strip().casefold()
        valid = answer in valid_lowercase_answers
    return answer

