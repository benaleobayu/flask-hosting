```toml
name = 'create_user'
method = 'POST'
url = '{{baseUrl}}/api/users'
sortWeight = 2500000
id = '1b88b0e6-5877-42e3-80ba-e14c640344f7'

[[headers]]
key = 'Content-Type'
value = 'application/x-www-form-urlencoded'

[[body.urlEncoded]]
key = 'name'
value = 'hepi'

[[body.urlEncoded]]
key = 'username'
value = 'benos'

[[body.urlEncoded]]
key = 'email'
value = 'benozs@gmail.com'

[[body.urlEncoded]]
key = 'password'
value = 'password'
```
