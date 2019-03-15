# django-oidc
OpenID connect server based on Django


### How to run ?

- setup your environment

```
./setup.sh
```

- setup and run the oidc provider server

```
./django_oidc/setup.sh
./django_oidc/run.sh
```

- go to the [admin site](http://localhost:8000/admin/oidc_provider/client/) and create a public client with a response_type `id_token token` and a redirect_uri `http://localhost:3000`

- edit the file `rp_client/index.html` and set your `client_id` with the value you can find on the [admin site](http://localhost:8000/admin/oidc_provider/client/).

- run the relying party client

```
./rp_client/run.sh
```

- go to the [RP client page](http://localhost:3000) and click on login button.

You should be redirected to a page asking for your permission, with an url that should look like this example

```
http://localhost:8000/authorize?response_type=id_token token&scope=openid profile email&nonce=42a6dm&client_id=869001&redirect_uri=http://localhost:3000&state=18f7s4n
```

- click on *Authorize* and you should then be redirected to your home page and you should see an `access_token` and `id_token` in the URL.

Ex:
```
http://localhost:3000/#access_token=50a56b0113874128a5d97c725107420a&id_token=eyJhbGciOiJSUzI1NiIsImtpZCI6Ijc4YTllODkxN2QxNzc5ZmZmZjQ1YWI2NmFjZDY5NWM2In0.eyJpc3MiOiJodHRwOi8vbG9jYWxob3N0OjgwMDAiLCJzdWIiOiIxIiwiYXVkIjoiODY5MDAxIiwiZXhwIjoxNTUyNDg1OTE0LCJpYXQiOjE1NTI0ODUzMTQsImF1dGhfdGltZSI6MTU1MjQ4NDU0OCwibm9uY2UiOiI0MmE2ZG0iLCJhdF9oYXNoIjoic1NvZ2htVko0WXphVS15aVgzTlBYdyJ9.WMxhbQ1Ms-wxALMyKlF1CV0PMfOsH7w7JqPecgSEeFk84vgg1MtQI2U3gWenvtC84o7RBq4ufgTCvhUvgBICPfXEcCxYE2mfOzQkO18bMRoM5ETqFZAjaGSxsB3r-3rwtCGJP4aKpno28Jtt5080zJxwH-q9mbWgwxEiPULR6ffvglBisX9Bt5uIfw34sojABaBNDS7jCuUZuTTlbzoE3O_IbXh3lmvj4Kb1HUwgPgmyKU13wlLv8EMJOyTxiTkQc-aiW7c2BjGi-TQkKpi5SO8shF6h9fYm23BCUUEiIkamAgr4PCklISYCiXamSoajCuBQBXsO__K34T-Oo3oz6Q&token_type=bearer&expires_in=3600&state=18f7s4n
```

You also should see your user info in a popup view.

- Get user info

```
http http://localhost:8000/userinfo/?access_token=50a56b0113874128a5d97c725107420a
```

### Online help documentation

https://medium.com/@darutk/new-architecture-of-oauth-2-0-and-openid-connect-implementation-18f408f9338d
https://medium.com/@darutk/diagrams-of-all-the-openid-connect-flows-6968e3990660
https://connect2id.com/products/server/docs/api
https://security.stackexchange.com/questions/129928/oidc-flow-for-spa-and-restful-api
https://developer.okta.com/blog/2017/07/25/oidc-primer-part-1
https://django-oidc-rp.readthedocs.io/en/stable/index.html

### Decode JWT token

https://jwt.io/


### Implicit flow

- User navigates to SPA, which redirects user to IdP to sign in.
- User signs in (and authorizes the application, if needed).
- IdP returns user to SPA with Access Token and ID Token.
- JavaScript code in SPA stores the Access Token and ID Token in the browser's localStorage and sends the Access Token to the REST API server for every request it makes (usually as an Authorization: Bearer <access token> header).
- If needed, REST API Server checks the validity of the Access Token by talking to the IdP. (Often, signing the token in the IdP and verifying that signature will be enough, and no communication is actually necessary.)
