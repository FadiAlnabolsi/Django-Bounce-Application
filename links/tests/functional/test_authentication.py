from links.tests.functional.base import FunctionalTest

class AuthenticationTest(FunctionalTest):
	fixtures = ['data-small.json', 'users.json']

	def test_user_can_login_and_logout(self):
		# Q is browsing link on bouce
		self.browser.get(self.live_server_url)

		# He wants to login to have a customized user experience
		# he clicks the 'Login' link which takes him to the login form
		login_link = self.browser.find_element_by_id('login')
		self.click_wait(login_link)

		# He notices the browser title change
		self.assertEqual(self.browser.title, 'Bounce | Login')

		# he enters his username and password and clicks the 'Login' submission button
		self.login('test_user', 'test_password')

		# He is redirected back to the homepage but now sees his username
		# and logout button in the header. The login button is no longer present
		header_text = self.browser.find_element_by_tag_name('header').text
		self.assertIn('test_user', header_text)
		self.assertIn('Logout', header_text)
		self.assertNotIn('Login', header_text)

		# Q is done browsing links and wants to logout so he clicks the 'Logout' button
		logout_link = self.browser.find_element_by_id('logout')
		self.click_wait(logout_link)

		# The homepage reloads and he can no longer see his username
		# or the logout in the header. The login button is again present.
		header_text = self.browser.find_element_by_tag_name('header').text

		self.assertNotIn('Logout', header_text)
		self.assertNotIn('test_user', header_text)
		self.assertIn('Login', header_text)

	def test_user_cant_login_and_returns_to_homepage(self):
		# Bo wants to login to Bounce
		self.browser.get(self.live_server_url + '/login')

		# He enters an invalid username and password and clicks the 'login' button
		self.login('invalid_user', 'invalid_password')

		#the login form responds with an error message
		error_message = self.browser.find_element_by_css_selector('p.error').text
		self.assertIn("Your username and password didn't match.", error_message)

		#Bo can't remember his login info and decides to just browse without logging in
		home_link = self.browser.find_element_by_css_selector('header>h1>a')
		self.click_wait(home_link)
		self.assertEqual(self.browser.current_url, self.live_server_url + '/')



