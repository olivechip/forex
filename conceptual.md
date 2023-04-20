### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?

  *Javascript is prototype-based language, python is more class-based object oriented language*

- Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you
  can try to get a missing key (like "c") *without* your programming
  crashing.

  *1. dictionary.get("c", "value")*
  *2. dictionary["key"] = "value"*

- What is a unit test?

  *Unit test tests individual functions of a program*

- What is an integration test?

  *Integration test tests how the components of the program work together*

- What is the role of web application framework, like Flask?

  *Helper framework that makes tedious tasks easier to do; ex: routing*

- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?

  *Depending on if there is more data that falls under the "pretzel" category, I may choose to use a query param over a route url*
  *I will use the route url if it is a simple matter of just 1 type of food*

- How do you collect data from a URL placeholder parameter using Flask?
  *use request.args['search term'] to access data from url placeholder parameter*

- How do you collect data from the query string using Flask?

  *from flask import request*
  *use request.args['search term'] to access data from query string*

- How do you collect data from the body of the request using Flask?
  *request.json*
  
- What is a cookie and what kinds of things are they commonly used for?
  *cookies are used for storing user specific info/data in a browser, keeping track of sessions, log-ins, targeted ads, etc*

- What is the session object in Flask?

  *session object allows storage of user specific data*
  *prevents data tampering through use of secret key*

- What does Flask's `jsonify()` do?

  *return the server response in JSON form so the client browser can read*