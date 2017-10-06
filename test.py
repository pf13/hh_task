
# -*- coding: utf-8 -*-

from datafile import *
from locators import HhPage


class TestHh:
	#Поиск компании по вакансиям по ключевому слову "Новые облачные"
	def test_find_by_name_in_searchvacancy(self, action):
		try:
			action.open_page('https://spb.hh.ru/search/vacancy?text={0}&area=2'.format(find_name_company))
			action.browser.find_element_by_xpath(HhPage.find_vacancy_title_in_result)		
		except Exception as e:
			raise print('Company not found in vacancy search')

	#Поиск компании по компаниям по ключевому слову "Новые облачные"		
	def test_find_by_name_in_employerslist(self, action): 
		try:
			action.open_page('https://spb.hh.ru/employers_list?query={0}&areaId=113'.format(find_name_company))
			action.browser.find_element_by_xpath(HhPage.find_vacancy_title_in_result)
		except Exception as e:
			raise print('Company not found in employer search')

	#Проверка количества вакансий на странице компании в текущем регионе		
	def test_check_quantity_vacancies_in_region(self, action):
		try:
			action.open_page(base_url+employer_path)
			qtt = action.browser.find_element_by_css_selector(HhPage.quantity_vacancies_on_page)
			assert qtt.text == quantity_vacancies
		except Exception as e:
			raise print('Quantity vacancies in region not right')
				
	#Проверка отображения вакансии "QA Automation Engineer"на странице компании		
	def test_check_qa_vacancy_in_region(self, action):
		try:
			action.open_page(base_url+employer_path)
			action.browser.find_element_by_css_selector(HhPage.vacancies_group_title_link).click()
			jobs_list = action.browser.find_elements_by_css_selector(HhPage.vacancy_serp_vacancy_title)
			qa_job = [job.text for job in jobs_list]
			assert find_name_vacancy in qa_job
		except Exception as e:
			raise print('No QA vacancy in region')
