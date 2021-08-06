import argparse

# python3 usable_scripts/Arguments.py --help
parsser = argparse.ArgumentParser()
parsser.add_argument('-a', '--action', help='Action to perform.')
args = parsser.parse_args()
action = args.action


class ArgumentTest():
    """Testing argument."""

    @staticmethod
    def run():
        print('running...')

    @staticmethod
    def rest():
        print('resting...')

if __name__ == '__main__':
    arg = ArgumentTest()

    # python3 usable_scripts/Arguments.py --action 'run'
    if action == 'run':
        arg.run()

    # python3 usable_scripts/Arguments.py --action 'rest'
    if action == 'rest':
        arg.rest()
