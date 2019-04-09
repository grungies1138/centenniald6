from evennia.utils import evtable


def node_formatter(nodetext, optionstext, caller=None):
    separator1 = "|010_|n" * 78 + "\n\n"
    separator2 = "\n" + "|010_|n" * 78 + "\n\n|330You may type '|540q|n' |330or|n '|540quit|n' " \
                                         "|330at any time to quit this application.|n\n" + "|010_|n" * 78 + "\n\n"
    return separator1 + nodetext + separator2 + optionstext


def options_formatter(optionlist, caller=None):
    options = []
    for key, option in optionlist:
        options.append("|w%s|n: %s" % (key, option))

    if len(options) > 6:
        if len(options) % 2 > 0:
            colA = options[:len(options) / 2 + 1]
            colB = options[len(options) / 2 + 1:]
        else:
            colA = options[:len(options) / 2]
            colB = options[len(options) / 2:]
        table = evtable.EvTable(table=[colA, colB], border=None)

        table.reformat_column(0, width=40)
        table.reformat_column(1, width=40)

        return str(table) + "\n"

    else:
        return "\n".join(options)