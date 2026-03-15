# Opção A (Desafio)
Crie uma rota /webhook que receba um JSON com { "id": 123, "mensagem": "Olá" }  e salve em uma lista/array/arquivo.  Depois crie uma rota /mensagens que liste todas.  Não precisa banco de dados — apenas estrutura.  Entregue o código no GitHub e explique em 5 linhas como testou.

Como Testei:
1.Instalei o framework rodando pip install flask no terminal e iniciei o servidor com o comando python app.py.
2.O servidor subiu e ficou escutando requisições localmente no endereço port 3000.
3.Abri um segundo terminal e disparei o evento via cURL: curl -X POST http://localhost:3000/webhook -H "Content-Type: application/json" -d "{\"id\": 123, \"mensagem\": \"Olá\"}".
4.O servidor me retornou o Status HTTP 201 com a confirmação de que os dados foram registrados.
5.Em seguida fiz um requisição de lista: curl http://localhost:3000/mensagens e recebi na tela o Array de volta contendo exatamente o objeto JSON que enviei.
