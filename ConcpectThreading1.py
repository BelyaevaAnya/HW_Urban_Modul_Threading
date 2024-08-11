import requests
from datetime import datetime
time_start = datetime.now()
THE_URL = 'https://api.github.com/user'
res = []

for i in range(4):
    response = requests.get(THE_URL)
    page_response = response.json()
    res.append(page_response)
time_end = datetime.now()
print()
print(f'Время выполнения программы {time_end-time_start}')
print(res)

# Время выполнения программы 0:00:00.732428
# [{'message': 'Requires authentication', 'documentation_url': 'https://docs.github.com/rest/users/users#get-the-authenticated-user', 'status': '401'},
# {'message': 'Requires authentication', 'documentation_url': 'https://docs.github.com/rest/users/users#get-the-authenticated-user', 'status': '401'},
# {'message': 'Requires authentication', 'documentation_url': 'https://docs.github.com/rest/users/users#get-the-authenticated-user', 'status': '401'},
# {'message': 'Requires authentication', 'documentation_url': 'https://docs.github.com/rest/users/users#get-the-authenticated-user', 'status': '401'},
# {'message': 'Requires authentication', 'documentation_url': 'https://docs.github.com/rest/users/users#get-the-authenticated-user', 'status': '401'},
# {'message': 'Requires authentication', 'documentation_url': 'https://docs.github.com/rest/users/users#get-the-authenticated-user', 'status': '401'},
# {'message': 'Requires authentication', 'documentation_url': 'https://docs.github.com/rest/users/users#get-the-authenticated-user', 'status': '401'},
# {'message': 'Requires authentication', 'documentation_url': 'https://docs.github.com/rest/users/users#get-the-authenticated-user', 'status': '401'},
# {'message': 'Requires authentication', 'documentation_url': 'https://docs.github.com/rest/users/users#get-the-authenticated-user', 'status': '401'},
# {'message': 'Requires authentication', 'documentation_url': 'https://docs.github.com/rest/users/users#get-the-authenticated-user', 'status': '401'},
# {'message': 'Requires authentication', 'documentation_url': 'https://docs.github.com/rest/users/users#get-the-authenticated-user', 'status': '401'},
# {'message': 'Requires authentication', 'documentation_url': 'https://docs.github.com/rest/users/users#get-the-authenticated-user', 'status': '401'},
# {'message': 'Requires authentication', 'documentation_url': 'https://docs.github.com/rest/users/users#get-the-authenticated-user', 'status': '401'},
# {'message': 'Requires authentication', 'documentation_url': 'https://docs.github.com/rest/users/users#get-the-authenticated-user', 'status': '401'},
# {'message': 'Requires authentication', 'documentation_url': 'https://docs.github.com/rest/users/users#get-the-authenticated-user', 'status': '401'},
# {'message': 'Requires authentication', 'documentation_url': 'https://docs.github.com/rest/users/users#get-the-authenticated-user', 'status': '401'},
# {'message': 'Requires authentication', 'documentation_url': 'https://docs.github.com/rest/users/users#get-the-authenticated-user', 'status': '401'},
# {'message': 'Requires authentication', 'documentation_url': 'https://docs.github.com/rest/users/users#get-the-authenticated-user', 'status': '401'},
# {'message': 'Requires authentication', 'documentation_url': 'https://docs.github.com/rest/users/users#get-the-authenticated-user',
# 'status': '401'}, {'message': 'Requires authentication', 'documentation_url': 'https://docs.github.com/rest/users/users#get-the-authenticated-user', 'status': '401'}]
