import requests

response = requests.get('http://206.81.5.208:8080/spec?name=p').json()
print('spec', response)

response = requests.get('http://206.81.5.208:8080/vacancies?name=python developer&lvl=Middle').json()
print('vacancies', response)

response = requests.post('http://206.81.5.208:8080/skills', json={'email': 'lll@lll.lll', 'skillsItemUiModel': [
    {'layoutId': 2, 'name': 'android', 'selected': {'mValue': 'True'}},
    {'layoutId': 2, 'name': 'git', 'selected': {'mValue': 'False'}}]}).json()

print('skills', response)

response = requests.get('http://206.81.5.208:8080/profile/known?email=aaa@aaa.aaa').json()
print('known', response)

response = requests.get('http://206.81.5.208:8080/profile/unknown?email=aaa@aaa.aaa').json()
print('unknown', response)

response = requests.get('http://206.81.5.208:8080/profile/score?email=aaa@aaa.aaa').json()
print('score', response)

response = requests.post('http://206.81.5.208:8080/profile/complete', json={'email': 'lll@lll.lll', 'skill': 'git'}).json()
print('score', response)
