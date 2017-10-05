
# -*- coding: utf-8 -*-

from datafile import *
from locators import HhPage


class TestHh:

	def test_find_by_name_in_searchvacancy(self, action):
		try:
			action.open_page('https://spb.hh.ru/search/vacancy?text={0}&area=2'.format(find_name_company))
			action.browser.find_element_by_xpath('//a[contains(@href, employer_path)]')		
		except Exception as e:
			raise print('Company not found in vacancy search')


	def test_find_by_name_in_employerslist(self, action): 
		try:
			action.open_page('https://spb.hh.ru/employers_list?query={0}&areaId=113'.format(find_name_company))
			action.browser.find_element_by_xpath('//a[contains(@href, employer_path)]')
		except Exception as e:
			raise print('Company not found in employer search')


	def test_check_quantity_vacancies_in_region(self, action):
		try:
			action.open_page(base_url+employer_path)
			qtt = action.browser.find_element_by_css_selector('.b-employerpage-vacancies.g-expand .b-employerpage-vacancies-region .b-employerpage-vacancies-hint')
			assert qtt.text == quantity_vacancies
		except Exception as e:
			raise print('Quantity vacancies in reagion not right')
				

	def test_check_qa_vacancy_in_region(self, action):
		try:
			action.open_page(base_url+employer_path)
			action.browser.find_element_by_css_selector('[data-qa="vacancies-group-title-link"]').click()
			jobs_list = action.browser.find_elements_by_css_selector('[data-qa="vacancy-serp__vacancy-title"]')
			qa_job = [job.text for job in jobs_list]
			assert find_name_vacancy in qa_job
		except Exception as e:
			raise print('No QA vacancy in region')
