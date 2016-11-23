# coding=utf-8


def run(manager):
    assert not manager['forms'].authorization('User123', 'Paswwd123')
    assert manager['forms'].authorization('Maxibond', 'reddit666')
