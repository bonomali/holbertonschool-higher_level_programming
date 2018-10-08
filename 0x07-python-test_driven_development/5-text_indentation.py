#!/usr/bin/python3
def text_indentation(text):
    """Prints a text with 2 new lines after each period,
    question mark, and colon
    Args:
    text (str): the given text
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    lett = 0
    while lett < len(text):
        if text[lett] is "." or text[lett] is "?" or text[lett] is ":":
            print(text[lett] + "\n")
            lett += 1
            while text[lett] is " ":
                lett += 1
        print(text[lett], end="")
        lett += 1
