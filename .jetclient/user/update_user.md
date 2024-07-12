```toml
name = 'update_user'
method = 'PUT'
url = '{{baseUrl}}/api/users/4'
sortWeight = 4000000
id = '5d90a58b-4d75-4b2e-8666-8279505f76c3'

[[headers]]
key = 'Content-Type'
value = 'application/x-www-form-urlencoded'

[[body.urlEncoded]]
key = 'name'
value = 'John Doe'

[[body.urlEncoded]]
key = 'username'
value = 'johndoes'

[[body.urlEncoded]]
key = 'email'
value = 'johndoes@example.com'

[[body.urlEncoded]]
key = 'password'
value = 'password'
```
