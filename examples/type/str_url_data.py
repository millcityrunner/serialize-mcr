from serialize-mcr import serialize-mcr


class StrURLData(serialize-mcr):
    schema = [
        {'name': 'prop1', 'type': (str, 'url')}
    ]


valid_data = StrURLData({'prop1': 'https://www.google.com/'})
print(valid_data)
# >>> {"prop1": "https://www.google.com/"}
valid_data = StrURLData({'prop1': 'https://www.youtube.com/watch?v=PUCLToWjMKs'})
print(valid_data)
# >>> {"prop1": "https://www.youtube.com/watch?v=PUCLToWjMKs"}

invalid_data = StrURLData({'prop1': 'ttps://www.youtube.com/watch?v=PUCLToWjMKs'})
# >>> ValueError: Property: 'prop1' with Value: 'ttps://www.youtube.com/watch?v=PUCLToWjMKs' does not confirm with Type: (<class 'str'>, 'url').
