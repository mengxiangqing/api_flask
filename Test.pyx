
def logic(param):
    print('this is a logicv function')
    print('param is [s%] % param')
    return param.upper()
'''
注意1：这里在 python 源码中使用一种约定：以JNI_API_为前缀开头的函数表示为Python代码模块要导出对外调用的接口函数，这样做的目的是为了让我们的 Python 一键转 Jar 包系统能自动化识别提取哪些接口作为导出函数。

注意2：这一类接口函数的输入是一个 python 的 str 类型字符串，输出亦然，如此可便于移植以往通过JSON形式作为参数的 RESTful 接口。使用JSON的好处是可以对参数进行封装，支持多种复杂的参数形式，而不用重载出不同的接口函数对外调用。

注意3：还有一点需要说明的是，在接口函数前缀JNI_API_的后面，函数命名不能以 python 惯有的下划线命名法，而要使用驼峰命名法，注意这不是建议，而是要求，原因后续会提到。
'''
def JNI_API_TestFuncion(param):
    print('enter JNI_API_test_function')
    result = logic(param)
    print('leave JNI_API_test_function')
    return result
