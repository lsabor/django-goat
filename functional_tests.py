from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
import unittest



class NewToDoVisitor(unittest.TestCase):

    def setUp(self):
        options = Options()
        options.headless = True
        self.browser = webdriver.Firefox(options = options)
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
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # she is invited to endter a to-do item
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # she types "buy peacock feathers" into a ButtonBox
        inputbox.send_keys('Buy peacock feathers')

        # the page updates and now the page says:
        # "1: buy peacock feathers" as a to-do list item
        inputbox.send_keys(Keys.ENTER)
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: Buy peacock feathers' for row in rows),
            "new todo item didn't appear in table"
        )

        # there is still a text book for another item, she enters
        # "use peacock feathers"

        # The page updates upon pressing enter showing both items

        # Will this remember stuff? the site generated a unique url for her
        # and there is some explanatory text

        # she goes to that url and finds her todo list

        self.fail('finish writing these tests')


if __name__ == '__main__':
    unittest.main(warnings='ignore')



