import json
import os
from datetime import datetime

ARQUIVO_TAREFAS = "tasks.json"

def carregar_tarefas():
    if not os.path.exists(ARQUIVO_TAREFAS):
        return []
    
    with open(ARQUIVO_TAREFAS,"r",encoding="utf-8") as arquivo:
        return json.load(arquivo)
    

def salvar_tarefas(tarefas):
    with open(ARQUIVO_TAREFAS,"w", encoding="utf-8") as arquivo:
        json.dump(tarefas, arquivo, indent=4, ensure_ascii=False)


def adicionar_tarefa(tarefas):
    titulo = input("Digite a tarefa: ").strip()
    if not titulo:
        print("!!! A tarefa não pode estar vazia !!!")
        return
    
    prioridade = input("Prioridade (baixa/media/alta): ").lower().strip()
    if prioridade not in ["baixa","media", "alta"]:
        prioridade = "media"

    tarefa = {
        "titulo": titulo,
        "concluida": False,
        "prioridade": prioridade,
        "criada_em": datetime.now().strftime("%Y-%m-%d %H:%M")
    }

    tarefas.append(tarefa)
    salvar_tarefas(tarefas)
    print("Tarefa adicionada com sucesso !")


def listar_tarefas(tarefas):
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
        return
    
    print("\n--- SUAS TAREFAS ---")
    for i, tarefa in enumerate(tarefas):
        status = "Concluída" if tarefa.get("concluida") else "Pendente"
        prioridade = tarefa.get("prioridae" , "media")
        criada_em = tarefa.get("criada_em", "não registrada")

        print(f"{i + 1}.{tarefa['titulo']} "
              f"[{status}] | "
              f"Prioridade: {prioridade} | "
              f"Criada em: {criada_em}")
        


def concluir_tarefa(tarefas):
    listar_tarefas(tarefas)

    try:
        indice = int(input("Digite o número da tarefa concluída: ")) - 1
    except ValueError:
        print("⚠️ Digite um número válido.")
        return

    if 0 <= indice < len(tarefas):
        tarefas[indice]["concluida"] = True
        salvar_tarefas(tarefas)
        print("🎉 Tarefa marcada como concluída!")
    else:
        print("⚠️ Número inválido.")


def remover_tarefa(tarefas):
    listar_tarefas(tarefas)

    try:
        indice = int(input("Digite o número da tarefa para remover: ")) - 1
    except ValueError:
        print("⚠️ Digite um número válido.")
        return

    if 0 <= indice < len(tarefas):
        tarefas.pop(indice)
        salvar_tarefas(tarefas)
        print("🗑️ Tarefa removida!")
    else:
        print("⚠️ Número inválido.")


def menu():
    tarefas = carregar_tarefas()

    while True:
        print("\n--- GERENCIADOR DE TAREFAS ---")
        print("1 - Adicionar tarefa")
        print("2 - Listar tarefas")
        print("3 - Concluir tarefa")
        print("4 - Remover tarefa")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            adicionar_tarefa(tarefas)
        elif opcao == "2":
            listar_tarefas(tarefas)
        elif opcao == "3":
            concluir_tarefa(tarefas)
        elif opcao == "4":
            remover_tarefa(tarefas)
        elif opcao == "0":
            print("👋 Saindo...")
            break
        else:
            print("⚠️ Opção inválida.")


if __name__ == "__main__":
    menu()
