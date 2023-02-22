import pymysql.cursors
from Funcao import Funcao
from Funcionario import Funcionario



class Database():

    def __init__(self,host='localhost',port=3307, database='prova03', user='root', password='13@84mA.'):
        self.host=host
        self.port=port
        self.database=database
        self.user=user
        self.password=password


    def connect(self):
        self.connection = pymysql.connect(host=self.host,port=self.port, database=self.database, user=self.user, password=self.password,
                                charset='utf8mb4', 
                                cursorclass=pymysql.cursors.DictCursor)
        self.createDatabase()
        
    def parse_sql(self,filename):
        data = open(filename, 'r').readlines()
        stmts = []
        DELIMITER = ';'
        stmt = ''

        for lineno, line in enumerate(data):
            if not line.strip():
                continue

            if line.startswith('--'):
                continue

            if 'DELIMITER' in line:
                DELIMITER = line.split()[1]
                continue

            if (DELIMITER not in line):
                stmt += line.replace(DELIMITER, ';')
                continue

            if stmt:
                stmt += line
                stmts.append(stmt.strip())
                stmt = ''
            else:
                stmts.append(line.strip())
        return stmts

    def createDatabase(self):
        stmts = self.parse_sql('database.sql')
        for stmt in stmts:
            self.connection.cursor().execute(stmt)
            self.connection.commit()

    def add_funcionario(self,funcionario:Funcionario):
        with self.connection.cursor() as cursor:
            sql = "INSERT INTO funcionario (nome, cpf, funcao, salario, telefone) VALUES (%s,%s,%s,%s,%s)"
            cursor.execute(sql, (funcionario.nome, funcionario.cpf, funcionario.funcao.cod, funcionario.salario, funcionario.telefone))
        self.connection.commit()
        

    def add_funcao(self,funcao:Funcao):
        with self.connection.cursor() as cursor:
            sql = "INSERT INTO funcao (nome, cod) VALUES (%s,%s)"
            cursor.execute(sql, (funcao.nome, funcao.cod))
        self.connection.commit()
        

    def update_funcao(self,funcao:Funcao):
        with self.connection.cursor() as cursor:
            sql = "UPDATE funcao SET nome=%s WHERE cod=(%s)"
            cursor.execute(sql, (funcao.nome, funcao.cod))
        self.connection.commit()

    def update_funcionario(self,funcionario:Funcionario):
        with self.connection.cursor() as cursor:
            sql = "UPDATE funcionario SET nome=%s, cpf=%s, funcao=%s, salario=%s, telefone=%s WHERE cpf=(%s)"
            cursor.execute(sql,(funcionario.nome, funcionario.cpf, funcionario.funcao.cod, funcionario.salario, funcionario.telefone, funcionario.cpf,))
        self.connection.commit()
        


    def delete_funcionario(self,cpf):
        with self.connection.cursor() as cursor:
            sql = "DELETE FROM funcionario WHERE cpf=(%s)"
            cursor.execute(sql, (cpf))
        self.connection.commit()
        

    def delete_funcao(self,cpf):
        with self.connection.cursor() as cursor:
            sql = "DELETE FROM funcao WHERE cod=(%s)"
            cursor.execute(sql, (cpf))
        self.connection.commit()


    def search_funcionario(self,cpf):
        with self.connection.cursor() as cursor:
            sql = "SELECT * FROM funcionario WHERE cpf=(%s)"
            cursor.execute(sql,(cpf))
            res = cursor.fetchone()
            return res

    def search_funcao(self,cod):
        with self.connection.cursor() as cursor:
            sql = "SELECT * FROM funcao WHERE cod=(%s)"
            cursor.execute(sql,(cod))
            res = cursor.fetchone()
            return res

    def total_funcao(self):
        with self.connection.cursor() as cursor:
            sql = "SELECT COUNT(*) as total FROM funcao"
            cursor.execute(sql)
            (total) = cursor.fetchone()
            return int(total["total"])

    def total_funcionario(self):
        with self.connection.cursor() as cursor:
            sql = "SELECT COUNT(*) as total FROM funcionario"
            cursor.execute(sql)
            (total) = cursor.fetchone()
            return int(total["total"])