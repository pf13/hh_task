from selenium import webdriver


class Actions():

	def __init__(self):
		self.browser = webdriver.Chrome()

	def destroy(self):
		self.browser.quit()

	def open_page(self, url):
		self.browser.get(url)
