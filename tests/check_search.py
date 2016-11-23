# coding=utf-8


def run(manager):
    assert manager['forms'].search('python')
    assert not manager['forms'].search('asdsadsadsadsadsadsadsad')

