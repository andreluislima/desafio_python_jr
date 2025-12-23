# 🩺 Desafio Técnico — Desenvolvedor(a) Python Júnior

## 📌 Contexto

Você está participando de um processo seletivo para uma **healthtech** que desenvolve soluções com **inteligência artificial para apoiar profissionais de saúde**.

Um dos primeiros passos desses sistemas é **organizar e estruturar informações clínicas básicas** a partir de dados recebidos por uma API, antes de qualquer uso avançado de IA.

Este desafio simula esse cenário de forma **simplificada e segura**, utilizando apenas **dados fictícios**.

---

## 🎯 Objetivo do desafio

Avaliar sua capacidade de:

- Trabalhar com **Python**
- Ler e interpretar requisitos
- Modelar e validar dados
- Criar uma **API simples**
- Escrever código **claro, organizado e compreensível**
- Demonstrar cuidado ao lidar com dados da área da saúde

> ⚠️ Não esperamos uma solução perfeita.  
> Valorizamos **clareza, organização e boas decisões técnicas**.

---

## 🧩 Descrição do desafio

Você deverá criar uma **API em Python** que receba dados de uma consulta médica fictícia, processe essas informações e retorne um **resumo estruturado**.

---

## 📥 Dados de entrada (exemplo)

```json
{
  "patient": {
    "name": "Maria Silva",
    "birth_date": "1985-03-12",
    "gender": "F"
  },
  "appointment": {
    "date": "2025-03-20",
    "complaint": "Dor de cabeça há 3 dias",
    "notes": "Paciente relata dor moderada, sem febre."
  },
  "medications": [
    {
      "name": "Dipirona",
      "dosage": "500mg",
      "frequency": "8/8h"
    }
  ]
}
```

---

## 🌐 API esperada

Implemente um endpoint HTTP:

```
POST /consultations
```

Você pode usar **FastAPI** ou **Flask**.

---

## ✅ Requisitos obrigatórios

### 1️⃣ Validação dos dados

Implemente validações básicas:

- Nome do paciente é obrigatório
- Data de nascimento deve ser válida
- Data da consulta **não pode ser no futuro**
- A lista de medicamentos pode estar vazia

Você pode usar:
- `pydantic` (recomendado), ou
- validação manual simples

---

### 2️⃣ Processamento das informações

A aplicação deve:

- Calcular a **idade do paciente**
- Normalizar o gênero para:
  - `"female"`, `"male"` ou `"other"`
- Gerar um **resumo textual determinístico**, baseado apenas em regras

#### Exemplo de resumo esperado (rule-based):

```text
Paciente Maria Silva, 39 anos, sexo feminino. Queixa principal: Dor de cabeça há 3 dias.
```

> ⚠️ Este resumo **não deve usar IA**.  
> Ele deve ser construído programaticamente a partir dos dados recebidos.

---

### 3️⃣ Resposta da API (exemplo)

```json
{
  "patient_summary": {
    "name": "Maria Silva",
    "age": 39,
    "gender": "female"
  },
  "appointment_summary": {
    "date": "2025-03-20",
    "complaint": "Dor de cabeça há 3 dias",
    "notes": "Paciente relata dor moderada, sem febre."
  },
  "medications": [
    "Dipirona 500mg (8/8h)"
  ],
  "text_summary": "Paciente Maria Silva, 39 anos, sexo feminino. Queixa principal: Dor de cabeça há 3 dias."
}
```

---

## ⭐ Funcionalidade opcional (PLUS): uso de LLM local

> ⚠️ **Esta parte é totalmente opcional.**  
> A aplicação **deve funcionar perfeitamente sem IA**.

Se você se sentir confortável, pode implementar um **segundo modo de resumo textual** utilizando um **modelo de linguagem local (LLM)**.

### Regras para o uso de LLM:

- O uso de IA **não substitui** o resumo determinístico
- O LLM deve ser usado apenas como **modo alternativo**
- O modelo deve rodar **localmente**
- O resumo gerado por IA:
  - Não deve inventar informações
  - Não deve inferir diagnósticos
  - Deve se limitar aos dados fornecidos

---

## 🧪 Diferenciais (não obrigatórios)

- Testes automatizados (`pytest`)
- Documentação no `README.md`
- Organização do projeto em pastas
- Tratamento de erros com mensagens claras
- Uso de Docker

---

## 🚫 O que NÃO é esperado

- Machine Learning
- NLP avançado
- Banco de dados
- Autenticação
- Deploy em cloud

---

## 📦 Entrega

- Repositório GitHub com o código
- Um `README.md` explicando:
  - Como rodar o projeto
  - Decisões técnicas importantes
  - Observações que achar relevantes

---

## 📝 Observações finais

- Use apenas **dados fictícios**
- Priorize **código simples e legível**
- Se algo não ficar claro, documente suas decisões
- Não existe uma única solução correta

Boa sorte! 🚀  
Estamos curiosos para conhecer seu raciocínio e sua forma de programar.
