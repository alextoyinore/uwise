from rest_framework.authtoken.models import Token


class UserCookieMiddleWare(object):
    """
    Middleware to set user cookie
    If user is authenticated and there is no cookie, set the cookie,
    If the user is not authenticated and the cookie remains, delete it
    """

    def process_response(self, request, response):
        # if user and no cookie, set cookie
        if request.user.is_authenticated() and not request.COOKIES.get('uwiseweb'):
            token = Token.objects.get(user=request.user)
            response.set_cookie("uwiseweb", token.key)
        elif not request.user.is_authenticated() and request.COOKIES.get('uwiseweb'):
            # else if no user and cookie remove user cookie, logout
            response.delete_cookie("uwiseweb")
        return response
