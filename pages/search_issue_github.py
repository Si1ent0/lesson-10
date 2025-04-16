import allure

from selene import browser, by, be, have
from selene.support.shared.jquery_style import s

class IssuePage:

    @allure.step("Открываем главную страницу")
    def open_page(self, url):
        browser.open(url)


    @allure.step("Ищем репозиторий {repo}")
    def search_for_repository(self, repo):
        s(".header-search-button").click()
        s('//*[@id="query-builder-test"]').send_keys(repo)
        s('//*[@id="query-builder-test"]').submit()


    @allure.step("Переходим по ссылке репозитория {repo}")
    def go_to_repository(self, repo):
        s(by.link_text(repo)).click()


    @allure.step("Открываем таб Issues")
    def open_issue_tab(self):
        s("#issues-tab").click()


    @allure.step("Проверяем наличие Issue с текстом {text}")
    def should_see_issue_with_text(self, text):
        s('.Title-module__container--l9xi7').should(be.visible)
        element = browser.element('.Title-module__container--l9xi7')
        expected_text = text
        element.should((have.text(expected_text)))