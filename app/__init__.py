def tabulate(value):
    return value + ' ' * (TAB_WIDTH - len(value))


TAB_WIDTH = 12
STATEMENT_HEADER = '\n' + tabulate('Date') + tabulate('Amount') + tabulate('Balance') + '\n'
