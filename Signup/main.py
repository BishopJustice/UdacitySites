import webapp2

import validators

form = """
<h1>Signup</h1>
<form method="post">
    Username <input type="text" name="username" value="{username}"> 
        <div style="color: red; display: inline-block;"> {username_error} </div> <br>
    Password <input type="text" name="password" value="{password}">
        <div style="color: red; display: inline-block;"> {password_error} </div> <br>
    Verify Password <input type="text" name="verify" value="{verify}">
        <div style="color: red; display: inline-block;"> {verify_error} </div> <br>
    Email <input type="text" name="email" value="{email}">
        <div style="color: red; display: inline-block;"> {email_error} </div><br>
    <input type="submit">
</form>
"""


class MainPage(webapp2.RequestHandler):
    def write_form(self, username_error="", password_error="", email_error="", verify_error="", username="", password="", verify="", email=""):
        self.response.write(form.format(username_error=username_error,
                                        email_error=email_error,
                                        password_error=password_error,
                                        verify_error=verify_error,
                                        username=username,
                                        password=password,
                                        verify=verify,
                                        email=email))

    def get(self):
        self.write_form()

    def post(self):
        username = self.request.get('username')
        password = self.request.get('password')
        verify = self.request.get('verify')
        email = self.request.get('email')
        email_error = ""
        username_error = "" 
        password_error = ""
        verify_error = ""
        errors = 0
        if not validators.valid_username(username):
            username_error = "That's not a valid username."
            errors += 1
        if not validators.valid_password(password):
            password_error="That's not a valid password"
            errors += 1
        if not validators.valid_email(email) and email:
            email_error="That's not a valid email."
            errors += 1
        if password != verify:
            verify_error = "Your passwords do not match"
            errors += 1
        if errors > 0:
            self.write_form(username_error=username_error,
                            email_error=email_error,
                            password_error=password_error,
                            verify_error=verify_error,
                            username=username_error,
                            email=email)
        else:
            return self.redirect("/welcome")

        

class WelcomeHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write("You did it!")

app = webapp2.WSGIApplication([('/', MainPage),
                              ('/welcome', WelcomeHandler)],
                               debug=True)


