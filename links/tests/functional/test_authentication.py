import time
from links.tests.functional.base import FunctionalTest

class AuthenticationTest(FunctionalTest):
	fixtures = ['data-small.json', 'users.json']

	def test_user_can_login_and_logout(self):
		# Q is browsing link on bouce
		self.browser.get(self.live_server_url)

		# He wants to login to have a customized user experience
		# he clicks the 'Login' link which takes him to the login form
		login_link = self.browser.find_element_by_id('login')
		login_link.click()
		time.sleep(5)

		# he enters his username and password and clicks the 'Login' submission button
		self.browser.find_element_by_id('id_username').send_keys('test_user')
		self.browser.find_element_by_id('id_password').send_keys('test_password')
		login_button = self.browser.find_element_by_id('submit')
		login_button.click()
		time.sleep(5)


		# He is redirected back to the homepage but now sees his username
		# and logout button in the header. The login button is no longer present
		header_text = self.browser.find_element_by_tag_name('header').text
		self.assertIn('test_user', header_text)
		self.assertIn('Logout', header_text)
		self.assertNotIn('Login', header_text)

		# Q is done browsing links and wants to logout so he clicks the 'Logout' button
		logout_link = self.browser.find_element_by_id('logout')
		logout_link.click()
		time.sleep(5)

		# The homepage reloads and he can no longer see his username
		# or the logout in the header. The login button is again present.
		header_text = self.browser.find_element_by_tag_name('header').text

		self.assertNotIn('Logout', header_text)
		self.assertNotIn('test_user', header_text)
		self.assertIn('Login', header_text)

		self.fail('Finish the auth test!')



