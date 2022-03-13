from selenium import webdriver
import unittest



class NewToDoVisitor(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        # satisfied, she ends session
        self.browser.quit()


    def test_can_start_a_list_and_retrieve_it_later(self):
        # Barb log on and try to find our storefront
        self.browser.get('http://localhost:9000/')

        # the default page title says Babadook, scary!
        self.assertIn('Babadook',self.browser.title)

        # she jumps to the to-do list
        self.browser.get('http://localhost:9000/todo/')

        # the default page title says todo, much better.
        self.assertIn('To-Do',self.browser.title)
        self.fail('finish writing these tests')

        # she is invited to endter a to-do item

        # she types "buy peacock feathers" into a ButtonBox

        # when she hits enter, the page updates and now the page says:
        # "1: buy peacock feathers" as a to-do list item

        # there is still a text book for another item, she enters
        # "use peacock feathers"

        # The page updates upon pressing enter showing both items

        # Will this remember stuff? the site generated a unique url for her
        # and there is some explanatory text

        # she goes to that url and finds her todo list



if __name__ == '__main__':
    unittest.main(warnings='ignore')



