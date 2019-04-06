from lib import ImperativeOperations

if __name__ == '__main__':
    for plugin in ImperativeOperations.plugins:
        plugin().execute()
