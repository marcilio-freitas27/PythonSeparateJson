import json

# carrega o arquivo json que será usado
# loads json file that be used
with open('U1ZQR43RB.json','r') as f: 
    users = json.load(f)
    names = []
    msgs = []

# separa nomes e mensagens e insere cada um na sua lista
# divide names and messages and insert each one in your respective list
for separate in users:
    names.append(separate['user'])
    msgs.append(separate['text'])

# dicionário data criado e chaves-listas user e text dentro dele
# dict named data was create and "key-lists" named user and text inside data dict
data = {}
data['user'] = []
data['text'] = []

# Eu tentei criar arquivos .json e separar por nomes de usuários e suas mensagens. Esse é uma das tentativas.
# I tried create files .json and to separate per names of users and your messages. This is one of the attemps
for i in range(0,213):
    json.dump(data,open('data{}.json'.format(names[i]), 'w'))
    data['user'].append(names[i])
    data['text'].append(msgs[i])
    if data['user'][i] == "U0KK0T3CG":
        json.dump(data,open('dataU0KK0T3CG.json', 'w'))
        data['user'].append(names[i])
        data['text'].append(msgs[i])
    elif data['user'][i] == "U0MFNAG05":
        json.dump(data,open('dataU0MFNAG05.json', 'w'))
        data['user'].append(names[i])
        data['text'].append(msgs[i])
    elif data['user'][i] == "U1ZQR43RB":        
        json.dump(data,open('dataU1ZQR43RB.json', 'w'))
        data['user'].append(names[i])
        data['text'].append(msgs[i])
    elif data['user'][i] == "USLACKBOT":
        json.dump(data,open('dataUSLACKBOT.json', 'w'))
        data['user'].append(names[i])
        data['text'].append(msgs[i])

