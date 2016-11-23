# coding=utf-8
import functions
import tests


def gotosite(manager):
    manager['navigation'].to_index_page()


def run_tests(manager, test_list):
    for test in test_list:
        gotosite(manager)
        # if test.need_authorization:
        # authorization(manager)
        test.run(manager)


def start(driver):
    url = 'https://www.reddit.com/'
    manager = {
        'navigation': functions.Navigation(driver, url),
        'forms': functions.Forms(driver),
    }
    # run tests
    test_list = [tests.check_search,
                 tests.check_login,
                 tests.check_post]
    run_tests(manager, test_list)


