def check_word(guess, secret_word):
    result = []
    for i in range(len(guess)):
        if guess[i] == secret_word[i]:
            result.append("correct")
        elif guess[i] in secret_word:
            result.append("present")
        else:
            result.append("absent")
    return result