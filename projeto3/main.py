"""
Projeto 4: Sistema de Gerenciamento de Consultas Médicas
Descricao: Criar um sistema de gerenciamento de consultas medicas que permita o
cadastro de Medicos, medicos e agendamento de consultas. 
O sistema deve realizar operacoes CRUD sobre esses registros.

Funcionalidades:
• Cadastro de Medicos (nome, CPF, contato, hist́orico medico, etc.)
• Cadastro de medicos (nome, CRM, especialidade, etc.)
• Agendamento de consultas (paciente, medico, data, hora, etc.)
• Consulta de Medicos, medicos e agendamentos
• Atualizacao de informacoes de Medicos, ḿedicos e agendamentos
• Remocao de registros de Medicos, medicos e agendamentos
"""

import Medicos
import Pacientes
import Consultas

print('='*80)
print('{:^80}'.format('BANCO HOSPITAL RTM'))
print('='*80)

while True:
    resp = input("Digite o modulo a ser acessado: 1-PACIENTES, 2-MÉDICOS, 3-CONSULTAS, 4-SAIR: ")
    
    if resp == "1":
        # Módulo Medicos
        print('='*80)
        print('{:^80}'.format('BANCO HOSPITAL RTM - PACIENTES'))
        print('='*80)
        
        while True:
            while True:
                codigo_paciente = input('Código do Paciente: (0- Mostra Todos) ')
                
                if codigo_paciente.isnumeric():
                    codigo_paciente = int(codigo_paciente)
                    break

            if codigo_paciente == 0:
                Pacientes.mostraTodosPacientes()
            else:
                if Pacientes.consultarPaciente(codigo_paciente) != 0:
                    Pacientes.mostraPaciente(codigo_paciente)
                    op = input("Escolha: [A]-Alterar [E]-Excluir [C]-Cancelar Operações ==> ").upper()
                    while op!='A' and op!='E' and op!='C':
                        op = input("ERRO !!! Escolha CORRETAMENTE : [A]-Alterar [E]-Excluir [C]-Cancelar Operações ==> ").upper()
                    if op == 'A':
                        novoNome = input("Informe novo nome do paciente: ")
                        novoCpf = input("Informe o novo CPF: ")
                        novoTelefone = input("Informe o novo telefone: ")
                        Pacientes.alterarPaciente(codigo_paciente,novoNome,novoCpf,novoTelefone)
                    elif op == 'E':
                        confirma = input('ATENÇÃO !!!! TEM CERTEZA, CONFIRMA EXCLUSÃO? S-SIM OU N-NÃO: ').upper()
                        while confirma != 'S' and confirma != 'N':
                            confirma = input('RESPOSTA INEXISTENTE !!!! TEM CERTEZA, CONFIRMA EXCLUSÃO? S-SIM OU N-NÃO: ').upper()
                        if confirma == "S":
                            Pacientes.deletarPaciente(codigo_paciente)
                            print("Excluído com sucesso!")
                        elif confirma == "N":
                            print("Exclusão cancelada")
                else:
                    nomePaciente = input("Nome : ")
                    cpf = input("CPF : ")
                    telefone = input("Telefone : ")
                    Pacientes.inserirPaciente(codigo_paciente,nomePaciente,cpf,telefone)
            print('\n\n')
            print('='*80)
            continuar = input('Deseja continuar usando o módulo PACIENTES? 1-Sim OU qualquer tecla para sair: ')
            
            if continuar != '1':
                break

    elif resp == "2":
        # Módulo MEDICOS
        print('='*80)
        print('{:^80}'.format('BANCO HOSPITAL RTM - MÉDICOS'))
        print('='*80)
        
        while True:
            while True:
                codigo_medico = input('Código do Médico: (0- Mostra Todos) ')
                
                if codigo_medico.isnumeric():
                    codigo_medico = int(codigo_medico)
                    break

            if codigo_medico == 0:
                Medicos.mostraTodosMedicos()
            else:
                if Medicos.consultarMedico(codigo_medico) != 0:
                    Medicos.mostraMedico(codigo_medico)
                    op = input("Escolha: [A]-Alterar [E]-Excluir [C]-Cancelar Operações ==> ").upper()
                    while op!='A' and op!='E' and op!='C':
                        op = input("ERRO !!! Escolha CORRETAMENTE : [A]-Alterar [E]-Excluir [C]-Cancelar Operações ==> ").upper()
                    if op == 'A':
                        novoNome = input("Informe novo nome do médico: ")
                        novoCRM = input("Informe o novo CRM: ")
                        novaEspecialidade = input("Informe a nova especialidade: ")
                        Medicos.alterarMedico(codigo_medico,novoNome,novoCRM,novaEspecialidade)
                    elif op == 'E':
                        confirma = input('ATENÇÃO !!!! TEM CERTEZA, CONFIRMA EXCLUSÃO? S-SIM OU N-NÃO: ').upper()
                        while confirma != 'S' and confirma != 'N':
                            confirma = input('RESPOSTA INEXISTENTE !!!! TEM CERTEZA, CONFIRMA EXCLUSÃO? S-SIM OU N-NÃO: ').upper()
                        if confirma == "S":
                            Medicos.deletarMedico(codigo_medico)
                            print("Excluído com sucesso!")
                        elif confirma == "N":
                            print("Exclusão cancelada!")
                else:
                    nomeMedico = input("Nome : ")
                    crm = input("CRM : ")
                    especialidade = input("Especialidade : ")
                    Medicos.inserirMedico(codigo_medico,nomeMedico,crm,especialidade)
            print('\n\n')
            print('='*80)
            continuar = input('Deseja continuar usando o módulo MÉDICOS? 1-Sim OU qualquer tecla para sair: ')
            
            if continuar != '1':
                break
    
    elif resp == "3":
        #Modulo CONSULTAS - Agendamento de consultas ->
        """
        para uma consulta -> id_consulta, nome do paciente, nome do medico, data e horario da consulta
        """
        print('='*80)
        print('{:^80}'.format('BANCO HOSPITAL RTM - CONSULTAS'))
        print('='*80)
        
        while True:
            while True:
                codigo_consulta = input('Código da Consulta: (0- Mostra Todas) ')
                
                if codigo_consulta.isnumeric():
                    codigo_consulta = int(codigo_consulta)
                    break

            if codigo_consulta == 0:
                Consultas.mostraTodasConsultas()
            else:
                if Consultas.consultarConsulta(codigo_consulta) != 0:
                    Consultas.mostraConsulta(codigo_consulta)
                    op = input("Escolha: [A]-Alterar [E]-Excluir [C]-Cancelar Operações ==> ").upper()
                    while op!='A' and op!='E' and op!='C':
                        op = input("ERRO !!! Escolha CORRETAMENTE : [A]-Alterar [E]-Excluir [C]-Cancelar Operações ==> ").upper()
                    if op == 'A':
                        print("NOVOS DADOS: ")
                        nomePaciente = input("Nome do paciente: ")
                        nomeMedico = input("Nome do médico: ")
                        data = input("Data da consulta [dd/MM/yy]: ")
                        horario = input("Horário da consulta [HH:mm]: ")
                        Consultas.alterarConsulta(codigo_consulta,nomeMedico,nomePaciente,data,horario)
                    elif op == 'E':
                        confirma = input('ATENÇÃO !!!! TEM CERTEZA, CONFIRMA EXCLUSÃO? S-SIM OU N-NÃO: ').upper()
                        while confirma != 'S' and confirma != 'N':
                            confirma = input('RESPOSTA INEXISTENTE !!!! TEM CERTEZA, CONFIRMA EXCLUSÃO? S-SIM OU N-NÃO: ').upper()
                        if confirma == "S":
                            Consultas.deletarConsulta(codigo_consulta)
                            print("Excluído com sucesso!")
                        elif confirma == "N":
                            print("Exclusao cancelada")
                else:
                    nomePaciente = input("Nome do paciente: ")
                    nomeMedico = input("Nome do médico: ")
                    data = input("Data da consulta [dd/MM/yy]: ")
                    horario = input("Horário da consulta [HH:mm]: ")
                    Consultas.inserirConsulta(codigo_consulta,nomePaciente,nomeMedico,data,horario)
            print('\n\n')
            print('='*80)
            continuar = input('Deseja continuar usando o módulo CONSULTAS? 1-Sim OU qualquer tecla para sair: ')
            
            if continuar != '1':
                break

    
    elif resp == "4":
        break
        
    else:
        print("Opção inválida. Tente novamente.")
        continue

