'''9 — String methods: For text = " Python Bootcamp! ", remove the surrounding spaces, convert the result to lowercase, and check whether "Python" appears in the original string. '''

text = " Python Bootcamp! "

# 1. Remove surrounding spaces
stripped_text = text.strip()
print("Stripped text:", repr(stripped_text))

# 2. Convert the result to lowercase
lower_text = stripped_text.lower()
print("Lowercase text:", lower_text)

# 3. Check whether "Python" appears in the original string
has_python = "Python" in text
print("Contains 'Python':", has_python)