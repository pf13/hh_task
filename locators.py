# -*- coding: utf-8 -*-

from datafile import *

class HhPage:
	search_field = '[data-qa="vacancy-serp__query"]'
	vacancies_group_title_link = '[data-qa="vacancies-group-title-link"]'
	vacancy_serp_vacancy_title = '[data-qa="vacancy-serp__vacancy-title"]'
	quantity_vacancies_on_page = '.b-employerpage-vacancies.g-expand .b-employerpage-vacancies-region .b-employerpage-vacancies-hint'
	find_vacancy_title_in_result = '//a[contains(@href, employer_path)]'
