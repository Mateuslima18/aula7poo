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

    def pegar_livro(self, livro, data, biblioteca):
        
        for emprestimo in self.livros_emprestados:
            if emprestimo.livro == livro and emprestimo.data_devolucao is None:
                print(f"O livro '{livro.titulo}' já está emprestado por {self.nome}.")
                return
        emprestimo = Emprestimo(livro, self, data)
        self.livros_emprestados.append(emprestimo)
        livro.emprestimos.append(emprestimo)
        biblioteca.registrar_emprestimo(emprestimo)
        print(f"Livro '{livro.titulo}' emprestado a {self.nome} em {data}.")

    def devolver_livro(self, livro, data_devolucao, biblioteca):
        for emprestimo in self.livros_emprestados:
            if emprestimo.livro == livro and emprestimo.data_devolucao is None:
                emprestimo.devolver(data_devolucao)
                biblioteca.registrar_devolucao(emprestimo)
                print(f"Livro '{livro.titulo}' devolvido por {self.nome} em {data_devolucao}.")
                return
        print(f"Empréstimo do livro '{livro.titulo}' por {self.nome} não encontrado ou já devolvido.")

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
        return (f"Emprestimo: {self.livro} para {self.membro} em {self.data_emprestimo} - {status}")


class Biblioteca:
    def __init__(self, nome):
        self.nome = nome
        self.categorias = []
        self.membros = []
        self.emprestimos_ativos = []  

    def criar_categoria(self, nome):
        if any(categoria.nome == nome for categoria in self.categorias):
            print(f"A categoria '{nome}' já existe.")
            return None
        cat = Categoria(nome)
        self.categorias.append(cat)
        return cat

    def remover_categoria(self, nome):
        self.categorias = [cat for cat in self.categorias if cat.nome != nome]

    def cadastrar_membro(self, nome, membro_id):
        if any(m.membro_id == membro_id for m in self.membros):
            print(f"Já existe um membro com ID {membro_id}.")
            return None
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

    def registrar_emprestimo(self, emprestimo):
        self.emprestimos_ativos.append(emprestimo)

    def registrar_devolucao(self, emprestimo):
        if emprestimo in self.emprestimos_ativos:
            self.emprestimos_ativos.remove(emprestimo)

    def listar_emprestimos_ativos(self):
        for emprestimo in self.emprestimos_ativos:
            print(emprestimo)

    def __del__(self):
        print(f"A Biblioteca {self.nome} foi excluída.")




biblioteca = Biblioteca("Biblioteca Municipal")


ficcao = biblioteca.criar_categoria("Ficção")
tecnicos = biblioteca.criar_categoria("Técnicos")


livro1 = Livro("1984", "George Orwell")
livro2 = Livro("Python para Todos", "John Doe")
if ficcao:
    ficcao.adicionar_livro(livro1)
if tecnicos:
    tecnicos.adicionar_livro(livro2)


membro1 = biblioteca.cadastrar_membro("Ana", 1)
membro2 = biblioteca.cadastrar_membro("Bruno", 2)


if membro1:
    membro1.pegar_livro(livro1, "2025-05-01", biblioteca)
if membro2:
    membro2.pegar_livro(livro2, "2025-05-02", biblioteca)


if membro1:
    membro1.devolver_livro(livro1, "2025-05-10", biblioteca)


print("\nEmpréstimos ativos:")
biblioteca.listar_emprestimos_ativos()


print("\nCategorias:")
biblioteca.listar_categorias()

print("\nMembros:")
biblioteca.listar_membros()