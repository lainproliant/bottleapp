from bottleapp import *
import bottle

# -------------------------------------------------------------------
class TestApp(App):
    @get
    def test(self):
        return "Hello, world!"
    
    @route
    def lazy(self):
        return "It's a piece of cake..."

    @route
    def echo(self):
        return request

    @route('/message/<id:int>/view', ['GET'])
    def view_message(self, id, name):
        return "This is message %d for user %s!" % (id, name)

    @error(404)
    def oops(self, error):
        return "OOPS!"

# -------------------------------------------------------------------
if __name__ == "__main__":
    TestApp().run()

