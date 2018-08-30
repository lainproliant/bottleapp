import unittest
from bottleapp import *

# -------------------------------------------------------------------
class BottleAppTests(unittest.TestCase):
    def test_initial(self):
        class TestApp(App):
            @get
            def test(self):
                return "Hello, world!"

        TestApp().run()

# -------------------------------------------------------------------
if __name__ == "__main__":
    unittest.main()
