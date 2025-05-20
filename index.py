class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.emprestimos = [] 

    def __str__(self):
        return f'"{self.titulo}" por {self.autor}'

class Categoria:
    def __init__(self, nome):
        self.nome = nome
        self.livros = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)

    def __str__(self):
        return f"Categoria: {self.nome} com {len(self.livros)} livros"

class Membro:
    def __init__(self, nome, membro_id):
        self.nome = nome
        self.membro_id = membro_id
        self.livros_emprestados = [] 

    def pegar_livro(self, livro, data):
        emprestimo = Emprestimo(livro, self, data)
        self.livros_emprestados.append(emprestimo)
        livro.emprestimos.append(emprestimo)

    def devolver_livro(self, livro, data_devolucao):
        
        for emprestimo in self.livros_emprestados:
            if emprestimo.livro == livro and emprestimo.data_devolucao is None:
                emprestimo.devolver(data_devolucao)
                break

    def __str__(self):
        return f"{self.nome} (ID: {self.membro_id})"

class Emprestimo:
    def __init__(self, livro, membro, data):
        self.livro = livro
        self.membro = membro
        self.data_emprestimo = data
        self.data_devolucao = None

    def devolver(self, data_devolucao):
        self.data_devolucao = data_devolucao

    def __str__(self):
        status = f"Devolvido em {self.data_devolucao}" if self.data_devolucao else "Em andamento"
        return f"Emprestimo: {self.livro} para {self.membro} em {self.data_emprestimo} - {status}"

class Biblioteca:
    def __init__(self, nome):
        self.nome = nome
        self.categorias = []
        self.membros = []

   
    def criar_categoria(self, nome):
        cat = Categoria(nome)
        self.categorias.append(cat)
        return cat

    def remover_categoria(self, nome):
        self.categorias = [cat for cat in self.categorias if cat.nome != nome]

   
    def cadastrar_membro(self, nome, membro_id):
        membro = Membro(nome, membro_id)
        self.membros.append(membro)
        return membro

    def remover_membro(self, membro_id):
        self.membros = [m for m in self.membros if m.membro_id != membro_id]

    def listar_membros(self):
        for m in self.membros:
            print(m)

    def listar_categorias(self):
        for categoria in self.categorias:
            print(categoria)

    def __del__(self):
        print(f"A Biblioteca {self.nome} foi excluída, suas categorias também.")


biblioteca = Biblioteca("Biblioteca Municipal")

ficcao = biblioteca.criar_categoria("Ficção")
tecnicos = biblioteca.criar_categoria("Técnicos")


livro1 = Livro("1984", "George Orwell")
livro2 = Livro("Python para Todos", "John Doe")
ficcao.adicionar_livro(livro1)
tecnicos.adicionar_livro(livro2)


membro1 = biblioteca.cadastrar_membro("Ana", 1)
membro2 = biblioteca.cadastrar_membro("Bruno", 2)


membro1.pegar_livro(livro1, "2025-05-01")
membro2.pegar_livro(livro2, "2025-05-02")


membro1.devolver_livro(livro1, "2025-05-10")


for m in biblioteca.membros:
    for emprestimo in m.livros_emprestados:
        print(emprestimo)


print("\nCategorias:")
biblioteca.listar_categorias()
print("\nMembros:")
biblioteca.listar_membros()


del biblioteca