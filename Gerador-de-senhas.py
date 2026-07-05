# Importar Secrets para gerar as senhas
import secrets

# Criar um banco de caracteres para as senhas
banco = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789@#$&?!£¢€¥%"

# Variável para guardar a senha gerada
senha = ""

# Repetir 8 vezes
for i in range(8):

    # Escolher um caractere aleatório do banco
    senha += secrets.choice(banco)

# Mostrar a senha no terminal
print(senha)