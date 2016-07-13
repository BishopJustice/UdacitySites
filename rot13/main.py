#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
from funk import encode

form ="""
<form method="post">
    <h1>Enter some text to ROT13:</h1>
        <textarea rows=10 cols=30 type="text" name="text">{words}</textarea><br><br>
    <input type="submit">
</form>
"""

class MainHandler(webapp2.RequestHandler):
    def write_form(self, text=""):
        self.response.write(form.format(words=text))

    def get(self):
        self.write_form()

    def post(self):
        words = self.request.get("text")
        encoded = encode(words)
        self.write_form(encoded)

app = webapp2.WSGIApplication([('/', MainHandler)],
                               debug=True)
