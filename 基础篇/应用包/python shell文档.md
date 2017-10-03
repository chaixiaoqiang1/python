通过Python Shell文档＃

我们可以使用该help()命令了解更多关于函数，类或模块的信息。使用help()函数只是传递函数，类或模块的名称。例如，要了解input()函数调用help()函数如下：

>>>
>>> help(input)
Help on built-in function input in module builtins:

input(...)
    input([prompt]) -> string

    Read a string from standard input.  The trailing newline is stripped.
    If the user hits EOF (Unix: Ctl-D, Windows: Ctl-Z+Return), raise EOFError.
    On Unix, GNU readline is used if enabled.  The prompt string, if given,
    is printed without a trailing newline before reading.

>>>
>>>
该行input([prompt]) -> string被称为函数签名。函数签名定义它的参数和返回值。如果一个参数是可选的，那么它将被包含在方括号内，即[]。

该行input([prompt]) -> string意味着该input()函数接受一个可选参数，prompt并返回一个类型为string的值。

请注意，该help()函数不使用Internet连接来获取文档，而是使用存储在硬盘驱动器中的文档的脱机副本。Python文档也可以在线获取，访问https://docs.python.org/3/。