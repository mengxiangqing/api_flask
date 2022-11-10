from unittest import result


def logic(param):
    print('this is a logicv function')
    print('param is [s%] % param')
    return param.upper()
def JNI_API_TestFuncion(param):
    print('enter JNI_API_test_function')
    result = logic(param)
    print('leave JNI_API_test_function')
    return result
