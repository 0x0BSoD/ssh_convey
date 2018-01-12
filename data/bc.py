class bc:
    HEADER = '\033[30m'
    OKGREEN = '\033[31m'
    WARNING = '\033[32m'
    FAIL = '\033[33m'
    ENDC = '\033[37m'


def header(text):            # HEADER
        rez = bc.HEADER + text + bc.ENDC
        print(rez)
        return True


def ok(text):           # OK
        rez = bc.OKGREEN + text + bc.ENDC
        print(rez)
        return True


def fail(text):            # ERROR
        rez = bc.FAIL + text + bc.ENDC
        print(rez)
        return True


def warning(text):            # WARNING
        rez = bc.WARNING + text + bc.ENDC
        print(rez)
        return True


def colorReset():
    rez = bc.ENDC
    print(rez)
    return True


if __name__ == '__main__':
    header('Test')
    ok('Test')
    warning('Test')
    fail('Test')
    print('Test')
