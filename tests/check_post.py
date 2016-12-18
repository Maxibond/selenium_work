# coding=utf-8

need_authorization = True


def run(manager):
    assert manager['navigation'].to_first_text_post()
