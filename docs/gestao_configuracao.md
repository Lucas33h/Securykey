# Estratégia de Gestão de Configuração - Fase 3

**Projeto:** SecuryKey
**Data:** 25/11/2025

Este documento formaliza as práticas de Gestão de Configuração de Software (SCM) adotadas pela equipe para garantir a integridade, rastreabilidade e qualidade do código.

## 1. Estratégia de Branches (Git Flow Adaptado)

A equipe utiliza uma estratégia de ramificação baseada em **Git Flow** para organizar o desenvolvimento paralelo:

* **`main` (Produção):** Contém a versão estável do produto. O código nesta branch é protegido e só recebe atualizações via *Pull Request* aprovado.
* **`develop` (Integração):** Branch principal de desenvolvimento. Todas as novas funcionalidades são integradas aqui para testes conjuntos antes de irem para a main.
* **`feature/*` (Funcionalidades):** Branches temporárias criadas a partir da `develop`.
    * *Nomenclatura:* `feature/nome-da-tarefa` (Ex: `feature/login-auth`, `feature/docs-fase3`).
    * *Ciclo de vida:* Criada no início da tarefa -> Pull Request -> Merge na develop -> Branch deletada.

## 2. Política de Code Review (Revisão de Código)

Para assegurar a qualidade do código (QA) e disseminação de conhecimento:

1.  **Pull Requests (PR):** Nenhuma alteração entra na `main` ou `develop` sem um PR aberto.
2.  **Aprovação:** É necessário pelo menos **1 revisão (review)** de outro membro da equipe.
3.  **Critérios:** O revisor deve verificar clareza do código, padrões de projeto e se não há quebra de funcionalidades existentes.

## 3. Integração Contínua (CI Pipeline)

O projeto utiliza **GitHub Actions** para automação.
* **Gatilho:** O pipeline é acionado a cada *push* ou *pull request* para as branches principais.
* **Verificação:** O sistema executa testes unitários automatizados.
* **Bloqueio:** O merge é desencorajado caso o pipeline retorne erro (Status: Vermelho), garantindo que a build permaneça estável.
