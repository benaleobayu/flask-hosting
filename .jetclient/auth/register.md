```toml
name = 'register'
method = 'POST'
url = '{{baseUrl}}/api/register'
sortWeight = 2000000
id = '8ea50404-cb8e-47d7-a798-efab0e51cb5a'

[[headers]]
key = 'Content-Type'
value = 'application/x-www-form-urlencoded'

[[body.urlEncoded]]
key = 'name'
value = 'beno'

[[body.urlEncoded]]
key = 'username'
value = 'beno'

[[body.urlEncoded]]
key = 'email'
value = 'beno@gmail.com'

[[body.urlEncoded]]
key = 'password'
value = 'password'
```
