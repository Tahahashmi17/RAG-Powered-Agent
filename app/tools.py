import requests
def calculate_expression(expression):
    try:
        result = eval(expression, {"__builtins__": {}})
        return f"The result is: {result}"
    except Exception as e:
        return f"Calculation error: {str(e)}"
def define_word(word):
    try:
        response = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}")
        if response.status_code != 200:
            return "Sorry, I couldn't find a definition."
        data = response.json()
        meaning_block = data[0]["meanings"][0]
        part_of_speech = meaning_block["partOfSpeech"]
        definitions = meaning_block["definitions"][:2]
        definition_texts = [d["definition"] for d in definitions]
        return f"{word.capitalize()} ({part_of_speech}): " + "; ".join(definition_texts)
    except Exception as e:
        return f"Definition error: {str(e)}"
