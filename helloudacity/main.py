import webapp2

import validators


form = """
<form method="post">
    What is your birthday?<br>
    <br>
    <label>Month
    <input type="text" name="month" value="{month}">
    </label>
    <label>Day
    <input type="text" name="day" value="{day}">
    </label>
    <label>Year
    <input type="text" name="year" value="{year}">
    </label>
    <div style="color: red"> {error} </div>
    <br>
    <br>
    <input type="submit">
</form>
"""


class MainPage(webapp2.RequestHandler):
    def write_form(self, error="", month="", day="", year=""):
        self.response.write(form.format(error=validators.esc(error),
                                        month=validators.esc(month),
                                        day=validators.esc(day),
                                        year=validators.esc(year)))

    def get(self):
        self.write_form()

    def post(self):
        user_month = self.request.get('month')
        user_day = self.request.get('day')
        user_year = self.request.get('year')

        month = validators.valid_month(user_month)
        day = validators.valid_day(user_day)
        year = validators.valid_year(user_year)
        
        if not (month and day and year):
            self.write_form("That's an error buddy!", 
                            user_month,
                            user_day,
                            user_year)
        else:
            self.redirect("/thanks")

class ThanksHandler(webapp2.RequestHandler):
    def get(self):
        self.response.out.write("Thanks!")

app = webapp2.WSGIApplication([('/', MainPage),
                               ("/thanks", ThanksHandler)],
                               debug=True)

