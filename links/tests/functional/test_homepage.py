from links.tests.functional.base import FunctionalTest

class HomepageSmallTest(FunctionalTest):
    fixtures = ['data-small.json', 'users.json']

	#Charlie opens his web browser and goes to the Bounce homepage
    def test_small_homepage_layout(self):
        # Charlie opens his web browser and goes to the Bounce homepage
        ###self.browser.get('http://localhost:8000')
        self.browser.get(self.live_server_url)

        # He sees "Bounce" in the page header and browser title
        self.assertEqual(self.browser.title, "Bounce")
        header_text = self.browser.find_element_by_css_selector('header h1').text
        self.assertEqual(header_text, "Bounce")

        # He sees fifteen interesting links to check out
        links = self.browser.find_elements_by_css_selector('li.link a')
        self.assertEqual(len(links), 6)

        for link in links:
        	self.assertTrue(link.get_attribute("href"))
        	self.assertTrue(link.text)

        # He notices that the first link was submitted by [your username]
        username = self.browser.find_element_by_css_selector('.link span.submitted-by')
        self.assertEqual(username.text, "falnabol")

        #he notices that the first link was submitted some time ago
        time_ago = self.browser.find_element_by_css_selector('.link span.submitted-at').text
        self.assertTrue(time_ago.replace('ago', ''))

        #he notices that the first link is from http://gfycat.com/LegalMemorableFlies
        domain = self.browser.find_element_by_css_selector('.link small.link-domain').text
        self.assertEqual(domain, "imgur.com")

class HomepageLargeTest(FunctionalTest):
    fixtures = ['data-large.json', 'users.json']

    def test_large_homepage_layout(self):

        #D opens his web browser and goes to the Bounce homepage
        self.browser.get(self.live_server_url)

        #he sees fifteen interesting links to check out
        links = self.browser.find_elements_by_css_selector('li.link a')
        self.assertEqual(len(links), 15)

        for link in links:
            self.assertTrue(link.get_attribute("href"))
            self.assertTrue(link.text)

class HomepageEmptyTest(FunctionalTest):
    #Bobby opens his web browser and goes to the Bounce homepage
    def test_empty_homepage_layout(self):
        self.browser.get(self.live_server_url)

        #No links have been posted so he only sees a "no links" message
        links = self.browser.find_elements_by_css_selector('li.link a')
        self.assertEqual(len(links), 0)

        message = self.browser.find_element_by_id('no-links').text
        self.assertEqual(message, "Sorry, no links have been posted.")

#if __name__ == '__main__':
#	unittest.main(warnings='ignore')