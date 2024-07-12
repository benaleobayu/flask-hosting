```toml
name = 'create'
method = 'POST'
url = '{{baseUrl}}/api/todos/categories'
sortWeight = 1000000
id = '9999ecf7-cba9-4389-8e14-6290497a8d65'

[[headers]]
key = 'Content-Type'
value = 'application/x-www-form-urlencoded'

[auth.bearer]
token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcyMDQyMDI2NCwianRpIjoiMzNjODFjOTEtZDk5ZS00OTcyLWJjMDYtZTViM2EyYjMyZjNkIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6MSwibmJmIjoxNzIwNDIwMjY0LCJjc3JmIjoiMDgzNzQzNzAtNTAyYS00NTE3LThiNDktMThlMzc5ZmY5MzQ5IiwiZXhwIjoxNzIwNDIxMTY0fQ.aE7l9-RdIgqGqRj_HOQWppr24_4kyBQVJorIobkljho'

[[body.urlEncoded]]
key = 'name'
value = 'work'

[[body.urlEncoded]]
key = 'description'
value = 'todo on my work'
```
