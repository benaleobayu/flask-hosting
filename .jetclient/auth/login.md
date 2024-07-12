```toml
name = 'login'
method = 'POST'
url = '{{baseUrl}}/api/login'
sortWeight = 1000000
id = '10924956-88f6-45dd-9d09-bd39dcdb9933'

[[headers]]
key = 'Content-Type'
value = 'application/x-www-form-urlencoded'

[[body.urlEncoded]]
key = 'username'
value = 'beno'

[[body.urlEncoded]]
key = 'password'
value = 'password'
```
