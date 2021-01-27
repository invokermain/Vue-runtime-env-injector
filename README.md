# Vue-runtime-env-injector
A minimal Starlette implementation to solve the problem of injecting environment variables at runtime.

The solution is to use data attributes on the main <div> component of the Vue.js app.
Couple this with some Jinja2 templating and your Vue.js app can load variables declared at runtime!

While this repo mainly serves as a reference on how one could solve this problem, it is possible
to use the dockerfile provided to host your Vue app. The project is optimized for production use
and therefore any performance hits of using this should be minimal and more than suitable for small scale web apps.

# In more detail

This project is just a Starlette app that uses Jinja2 templating to allow you to template any
environment variable starting with `VUE_APP_` in your `index.html` file. It uses `[[` and `]]`
for the Jinja templating delimiters so that it does not conflict with Vue.JS.

# Example
If you look at `dist/index.html` you will see the `div` has various `data-...` attributes which refer
to the templated environment variables. At runtime these variables will have their actual values.

Using this and some javascript it is possible to pass these variables to your Vue app. A good way of doing this
that works for production and development is to use the following pattern in your `main.js`:

e.g. passing `VUE_APP_BASE_URL` to Vue.
```js
const el = document.getElementById('app');
const baseURL = (
  el.attributes['data-base-url']
    ? el.attributes['data-base-url'].value
    : process.env.VUE_APP_BASE_URL
);
```

You can then pass `baseUrl` to a Vue mixin etc.

# Production
To use the dockerfile in production all you need to do is mount your built Vue files and pass in any environment variables. e.g.

`docker run -p 8000:8000 -v C:\dev\vue-runtime-env-injector\mount:/dist --env-file .env.production injector`
