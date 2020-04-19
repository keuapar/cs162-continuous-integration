
import unittest
import requests
import sqlalchemy
import psycopg2
from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.orm import sessionmaker, mapper

# adapted from https://gist.github.com/keuapar/8dd05ff6f191c234db4108204daf7bcf

class TestCase(unittest.TestCase):

    def test_q0(self):
        self.assertEqual(True, True)

    def test_q1(self):
        r = requests.post('http://127.0.0.1:5000/add', data={'expression': '8+7+6+5+4+3+2+1'})
        self.assertEqual(r.status_code, 200)

    def test_q2(self):
        DATABASE_URI = 'postgres+psycopg2://cs162_user:cs162_password@127.0.0.1:5432/cs162'

        class Exps(object):
            pass

        from sqlalchemy import create_engine, MetaData, Table
        engine = create_engine(DATABASE_URI)

        from sqlalchemy.orm import sessionmaker, mapper

        Session = sessionmaker(bind=engine)

        metadata = MetaData(engine)
        expressions = Table('expression', metadata, autoload=True)
        mapper(Exps, expressions)

        s = Session()
        exps = s.query(Exps).all()

        self.assertEqual(exps[0].value, 36.0)

    def test_q3(self):
        r = requests.post('http://127.0.0.1:5000/add', data={'expression': '15!'})
        self.assertEqual(r.status_code, 500)

    def test_q4(self):
        exps = s.query(Exps).all()
        self.assertEqual(exps[-1], 36.0)

if __name__ == '__main__':
    unittest.main()

