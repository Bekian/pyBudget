import sys
import inspect


def help(cmd: str = ""):
    """
    This help function gives instruction on how to use the application.

    Usage:
        pyBudget [cmd] [options]

    Commands:
        help [cmd] [option]

    Args:
        cmd: optionally display specific command usage.
        If no cmd argument is provided, this message is displayed.
    """
    if cmd:
        match cmd:
            case "repl" | "r":
                print('repl sample help output')
            case _:
                print("Command option not found, try again.")
    else:
        print(inspect.getdoc(help))


def main():
    args = sys.argv
    # debug
    # TODO: MAKE THIS A RUN OPTION
    print("\n~~~  DEBUG PRINT START ~~~")
    print('args: ', args)
    print('args len: ', args.__len__())
    print("~~~  DEBUG PRINT END ~~~\n")
    # check which args option was used
    if args.__len__() == 1:
        help()
    elif args.__len__() > 1:
        match args[1]:
            case "h" | "help":
                help()


if __name__ == "__main__":
    main()
