import re

def lexical_analyzer (input_statement):
    tokens_map = {
        "keywords": [],
        "identifiers": [],
        "numbers": [],
        "operators": [],
        "unknowns": []
    }

    keyword_lexemes = r'\b(select|insert|update|delete|create|drop|where|order by|alter|join|from|and|or|value|values|set|into|on)\b'
    identifier_lexemes = r'\b[a-zA-Z_][a-zA-Z0-9]*\b'
    number_lexemes = r'\b[0-9][0-9]*\b'

    tokens = input_statement.split()

    for token in tokens:
        if re.match(keyword_lexemes, token):
            tokens_map['keywords'].append(token)
        
        elif re.match(number_lexemes, token):
            tokens_map["numbers"].append(token)
        
        elif token == "*" or token == "+" or token == "-" or token == "/" or token == "=":
            tokens_map["operators"].append(token)

        elif re.match(identifier_lexemes, token):
            tokens_map['identifiers'].append(token)

        else:
            tokens_map["unknowns"].append(token)
    
    return tokens_map

print(lexical_analyzer("select name, email from users u join jobtype j on j.user_id = u.user_id"))