# Open the file for reading
with open('varenumre-5485.txt', 'r') as file:
    # Iterate over each line in the file
    for line in file:
        # Find the text between single quotes
        start_index = line.find("'")
        end_index = line.rfind("'")

        # If there are single quotes on the line
        if start_index != -1 and end_index != -1:
            text_between_quotes = line[start_index + 1:end_index]
            print(text_between_quotes)