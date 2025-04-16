import allure
from allure_commons.types import Severity
from selene import browser, by, be, have
from selene.support.shared.jquery_style import s
from pages.search_issue_github import IssuePage


@allure.severity(Severity.MINOR)
def test_search_issue_name(browser_config):
    browser.open("/")

    s(".header-search-button").click()
    s('//*[@id="query-builder-test"]').send_keys("yashaka/selene")
    s('//*[@id="query-builder-test"]').submit()

    s(by.link_text("yashaka/selene")).click()

    s("#issues-tab").click()

    s('.Title-module__container--l9xi7').should(be.visible)
    element = browser.element('.Title-module__container--l9xi7')
    expected_text='consider building elements collection based on singular elements'
    element.should((have.text(expected_text)))

@allure.severity(Severity.NORMAL)
def test_search_issue_name_2(browser_config):
    with allure.step("Открываем главную страницу"):
        browser.open("/")

    with allure.step("Ищем репозиторий"):
        s(".header-search-button").click()
        s('//*[@id="query-builder-test"]').send_keys("yashaka/selene")
        s('//*[@id="query-builder-test"]').submit()

    with allure.step("Переходим по ссылке репозитория"):
        s(by.link_text("yashaka/selene")).click()

    with allure.step("Открываем таб Issues"):
        s("#issues-tab").click()

    with allure.step(f"Проверяем наличие определенного Issue"):
        s('.Title-module__container--l9xi7').should(be.visible)
        element = browser.element('.Title-module__container--l9xi7')
        expected_text='consider building elements collection based on singular elements'
        element.should((have.text(expected_text)))




@allure.feature("Repo")
@allure.epic("Repo")
@allure.story("Issue user page")
@allure.label("owner", "RS")
@allure.tag("smoke", "regression", "web", "repo")
@allure.severity(Severity.CRITICAL)
@allure.link("https://github.com", name="issue text")
@allure.step("Поиск ишью по тексту")
def test_search_issue_text_3(browser_config):
    issue = IssuePage()
    issue.open_page('/')
    issue.search_for_repository('yashaka/selene')
    issue.go_to_repository('yashaka/selene')
    issue.open_issue_tab()
    issue.should_see_issue_with_text('consider building elements collection based on singular elements')