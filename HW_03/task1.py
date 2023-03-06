# several variable for small automatisation
text_='I love Python'
count=42

# v1 One string for all text (ugly)
print("v1 One string for all text (ugly)")
text_v1=text_*count
print(text_v1)

# v2 One string for all text with separator (better)
print("v2 One string for all text with separator (better)")
text_separator=' '
text_v2=(text_+text_separator)*count
print(text_v2)

# v3 One string for each phrase (i like)
print("v3 One string for each phrase (i like)")
text_v3=(text_+'\n')*count
print(text_v3)