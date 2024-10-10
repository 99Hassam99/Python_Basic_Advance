"""
two issues with this code.
code repetition
creating expensive DB connection in every test case

two ways to fix issues
1.setup and teardown methods (classic xunit style)
2.fixtures(recommended)
"""

from mydb import myDB
import pytest
# conn = None # method 1
# cur = None

@pytest.fixture(scope="module") # setting: will be print one time
def cur():
    print("setting:") # pytest -v --capture=no
    db = myDB()
    conn = db.connect("server")
    curs = conn.cursor()
    # return curs
    # for teardown change return to yeild
    yield curs
    curs.close()
    conn.close()
    print("close")
# def setup_module(module):
#     global conn
#     global cur
#     db = myDB()
#     conn = db.connect("server")
#     cur = conn.cursor()
#
# def teardown_module(module):
#     cur.close()
#     conn.close()

def test_John_id(cur):
    # db = myDB()
    # conn = db.connect("server")
    # cur = conn.cursor()
    id = cur.execute("select id from employee_db where name=John")
    assert id == 123

def test_Tom_id(cur):
    # db = myDB()
    # conn = db.connect("server")
    # cur = conn.cursor()
    id = cur.execute("select id from employee_db where name=Tom")
    assert id == 789