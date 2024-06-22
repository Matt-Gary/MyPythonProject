import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
from datetime import datetime

class SugestoesComunidadeApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Sistema de Sugestões da Comunidade")
        self.master.geometry("800x600")

        self.conn = sqlite3.connect('sugestoes_comunidade.db')
        self.criar_tabela()

        self.criar_widgets()

    def criar_tabela(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS sugestoes (
                id INTEGER PRIMARY KEY,
                categoria TEXT,
                descricao TEXT,
                status TEXT,
                data_criacao TEXT
            )
        ''')
        self.conn.commit()

    def criar_widgets(self):
        # Frame para entrada de dados
        frame_entrada = ttk.Frame(self.master, padding="10")
        frame_entrada.pack(fill=tk.X)

        ttk.Label(frame_entrada, text="Categoria:").grid(row=0, column=0, sticky=tk.W)
        self.categoria_var = tk.StringVar()
        categorias = ["Educação", "Saúde", "Segurança", "Infraestrutura", "Outros"]
        self.categoria_combobox = ttk.Combobox(frame_entrada, textvariable=self.categoria_var, values=categorias)
        self.categoria_combobox.grid(row=0, column=1, sticky=(tk.W, tk.E))

        ttk.Label(frame_entrada, text="Descrição:").grid(row=1, column=0, sticky=tk.W)
        self.descricao_entry = ttk.Entry(frame_entrada, width=50)
        self.descricao_entry.grid(row=1, column=1, sticky=(tk.W, tk.E))

        ttk.Button(frame_entrada, text="Adicionar Sugestão", command=self.adicionar_sugestao).grid(row=2, column=1, sticky=tk.E)

        # Frame para lista de sugestões
        frame_lista = ttk.Frame(self.master, padding="10")
        frame_lista.pack(fill=tk.BOTH, expand=True)

        self.tree = ttk.Treeview(frame_lista, columns=('ID', 'Categoria', 'Descrição', 'Status', 'Data'), show='headings')
        self.tree.heading('ID', text='ID')
        self.tree.heading('Categoria', text='Categoria')
        self.tree.heading('Descrição', text='Descrição')
        self.tree.heading('Status', text='Status')
        self.tree.heading('Data', text='Data')
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar = ttk.Scrollbar(frame_lista, orient=tk.VERTICAL, command=self.tree.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.tree.configure(yscrollcommand=scrollbar.set)

        # Frame para ações
        frame_acoes = ttk.Frame(self.master, padding="10")
        frame_acoes.pack(fill=tk.X)

        ttk.Button(frame_acoes, text="Atualizar Sugestão", command=self.atualizar_sugestao).pack(side=tk.LEFT)
        ttk.Button(frame_acoes, text="Atualizar Status", command=self.atualizar_status).pack(side=tk.LEFT)
        ttk.Button(frame_acoes, text="Excluir Sugestão", command=self.excluir_sugestao).pack(side=tk.LEFT)
        ttk.Button(frame_acoes, text="Atualizar Lista", command=self.atualizar_lista).pack(side=tk.LEFT)

        self.atualizar_lista()

    def adicionar_sugestao(self):
        categoria = self.categoria_var.get()
        descricao = self.descricao_entry.get()
        if not categoria or not descricao:
            messagebox.showerror("Erro", "Por favor, preencha todos os campos.")
            return
        
        status = "Analisando"  # Status padrão para novas sugestões
        data_criacao = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO sugestoes (categoria, descricao, status, data_criacao) VALUES (?, ?, ?, ?)",
                       (categoria, descricao, status, data_criacao))
        self.conn.commit()

        self.descricao_entry.delete(0, tk.END)
        self.atualizar_lista()
        messagebox.showinfo("Sucesso", "Sugestão adicionada com sucesso!")

    def atualizar_lista(self):
        for i in self.tree.get_children():
            self.tree.delete(i)
        
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM sugestoes ORDER BY data_criacao DESC")
        for row in cursor.fetchall():
            self.tree.insert('', tk.END, values=row)

    def atualizar_sugestao(self):
        selecionado = self.tree.selection()
        if not selecionado:
            messagebox.showerror("Erro", "Por favor, selecione uma sugestão para atualizar.")
            return

        item = self.tree.item(selecionado)
        id_sugestao = item['values'][0]
        categoria_atual = item['values'][1]
        descricao_atual = item['values'][2]
        status_atual = item['values'][3]

        # Criar uma nova janela para edição
        edit_window = tk.Toplevel(self.master)
        edit_window.title("Atualizar Sugestão")

        ttk.Label(edit_window, text="Categoria:").grid(row=0, column=0, sticky=tk.W)
        categoria_var = tk.StringVar(value=categoria_atual)
        categorias = ["Educação", "Saúde", "Segurança", "Infraestrutura", "Outros"]
        categoria_combobox = ttk.Combobox(edit_window, textvariable=categoria_var, values=categorias)
        categoria_combobox.grid(row=0, column=1, sticky=(tk.W, tk.E))

        ttk.Label(edit_window, text="Descrição:").grid(row=1, column=0, sticky=tk.W)
        descricao_entry = ttk.Entry(edit_window, width=50)
        descricao_entry.insert(0, descricao_atual)
        descricao_entry.grid(row=1, column=1, sticky=(tk.W, tk.E))

        def salvar_atualizacao():
            nova_categoria = categoria_var.get()
            nova_descricao = descricao_entry.get()

            cursor = self.conn.cursor()
            cursor.execute("UPDATE sugestoes SET categoria = ?, descricao = ? WHERE id = ?",
                           (nova_categoria, nova_descricao, id_sugestao))
            self.conn.commit()

            self.atualizar_lista()
            messagebox.showinfo("Sucesso", "Sugestão atualizada com sucesso!")
            edit_window.destroy()

        ttk.Button(edit_window, text="Salvar", command=salvar_atualizacao).grid(row=2, column=1, sticky=tk.E)

    def atualizar_status(self):
        selecionado = self.tree.selection()
        if not selecionado:
            messagebox.showerror("Erro", "Por favor, selecione uma sugestão para atualizar o status.")
            return

        item = self.tree.item(selecionado)
        id_sugestao = item['values'][0]

        # Criar uma nova janela para seleção do status
        status_window = tk.Toplevel(self.master)
        status_window.title("Atualizar Status")

        status_var = tk.StringVar()
        ttk.Radiobutton(status_window, text="Concluído", variable=status_var, value="Concluído").pack()
        ttk.Radiobutton(status_window, text="Analisando", variable=status_var, value="Analisando").pack()
        ttk.Radiobutton(status_window, text="Excluído", variable=status_var, value="Excluído").pack()

        def salvar_status():
            novo_status = status_var.get()
            if novo_status:
                cursor = self.conn.cursor()
                cursor.execute("UPDATE sugestoes SET status = ? WHERE id = ?", (novo_status, id_sugestao))
                self.conn.commit()

                self.atualizar_lista()
                messagebox.showinfo("Sucesso", f"Status atualizado para {novo_status}!")
                status_window.destroy()
            else:
                messagebox.showerror("Erro", "Por favor, selecione um status.")

        ttk.Button(status_window, text="Salvar", command=salvar_status).pack()

    def excluir_sugestao(self):
        selecionado = self.tree.selection()
        if not selecionado:
            messagebox.showerror("Erro", "Por favor, selecione uma sugestão para excluir.")
            return

        if messagebox.askyesno("Confirmar Exclusão", "Tem certeza que deseja excluir esta sugestão?"):
            item = self.tree.item(selecionado)
            id_sugestao = item['values'][0]

            cursor = self.conn.cursor()
            cursor.execute("DELETE FROM sugestoes WHERE id = ?", (id_sugestao,))
            self.conn.commit()

            self.atualizar_lista()
            messagebox.showinfo("Sucesso", "Sugestão excluída com sucesso!")

if __name__ == "__main__":
    root = tk.Tk()
    app = SugestoesComunidadeApp(root)
    root.mainloop()