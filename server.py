from http.server import BaseHTTPRequestHandler, HTTPServer
import json

# Lista em memória para salvar os dados (substitui o banco de dados) 
mensagens = []

class WebhookHandler(BaseHTTPRequestHandler):
    
    def do_POST(self):
        if self.path == '/webhook':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            
            try:
                data = json.loads(post_data.decode('utf-8'))
                
                # Verifica a estrutura básica do JSON
                if 'id' in data and 'mensagem' in data:
                    mensagens.append(data)
                    
                    self.send_response(201)
                    self.send_header('Content-type', 'application/json')
                    self.end_headers()
                    response = {'status': 'sucesso', 'registrada': data}
                    self.wfile.write(json.dumps(response).encode('utf-8'))
                else:
                    self.send_response(400)
                    self.send_header('Content-type', 'application/json')
                    self.end_headers()
                    response = {'erro': 'O JSON deve conter id e mensagem'}
                    self.wfile.write(json.dumps(response).encode('utf-8'))
                    
            except json.JSONDecodeError:
                self.send_response(400)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                response = {'erro': 'JSON inválido'}
                self.wfile.write(json.dumps(response).encode('utf-8'))
        else:
            self.send_response(404)
            self.end_headers()

    def do_GET(self):
         if self.path == '/mensagens':
             self.send_response(200)
             self.send_header('Content-type', 'application/json')
             self.end_headers()
             # Retorna a lista completa armazenada em memória
             self.wfile.write(json.dumps(mensagens).encode('utf-8'))
         else:
             self.send_response(404)
             self.end_headers()


def run(server_class=HTTPServer, handler_class=WebhookHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Servidor rodando na porta {port}...')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print('Servidor parado.')

if __name__ == '__main__':
    run()
