from serialize-mcr import serialize-mcr


class BoolData(serialize-mcr):
    schema = [
        {'name': 'prop1', 'type': (bool,)}
    ]


valid_data = BoolData({'prop1': True})
print(valid_data)
# >>> {"prop1": 1}
valid_data = BoolData({'prop1': False})
print(valid_data)
# >>> {"prop1": 1}

invalid_data = BoolData({'prop1': "True"})
# >>> ValueError: Property: 'prop1' with Value: 'True' does not confirm with Type: (<class 'bool'>,).
