import pytest

# scope选择作用域
@pytest.fixture(scope='function')
def login():
    print('#'*30 + '首先进行登录')
    yield
    print('#'*30 +'运行结束')


# autouse 给所有的测试用例都增加一个前置函数
@pytest.fixture(autouse=True)
def begin():
    print('%'*30 + 'begin的开始 autouse')
    yield
    print('%'*30 +'begin的结束 ')

# fixture 传递参数
@pytest.fixture(params=['para1','para2'])
def fixture_sendpara(request):
    print('@'*30+request.param)
    yield
    print('@'*30+'fixture_sendpara')

# fixture 参数化与fixture结合
@pytest.fixture()
def fixture_para(request):
    print('!'*30+request.param)
    yield
    print('!'*30+'fixture_para')