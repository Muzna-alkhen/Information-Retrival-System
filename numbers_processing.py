import re
import num2words

def formatNumbers(text):
    text = re.sub(r"(\d+)", lambda x: num2words.num2words(int(x.group(0))), text)

    # print(text)
    return text