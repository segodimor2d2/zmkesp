import os

def consolidar_codigos(pasta_origem, arquivo_saida='txt_allfiles.txt'):
    """
    Consolida todos os arquivos de código de uma pasta em um único arquivo de texto.
    
    Args:
        pasta_origem (str): Caminho da pasta contendo os arquivos de código
        arquivo_saida (str): Nome do arquivo de saída consolidado
    """
    
    # Extensões de arquivos de código comuns (pode ser personalizado)
    extensoes = ['.py', '.js', '.java', '.c', '.cpp', '.h', '.html', '.css', 
                 '.php', '.rb', '.go', '.rs', '.swift', '.kt', '.ts', '.sh', 
                 '.sql', '.md', '.txt', '.json', '.xml']
    
    try:
        with open(arquivo_saida, 'w', encoding='utf-8') as saida:
            # Escreve cabeçalho
            saida.write(f"=== CONSOLIDAÇÃO DE CÓDIGOS DA PASTA: {pasta_origem} ===\n\n")
            
            # Percorre todos os arquivos na pasta
            for raiz, _, arquivos in os.walk(pasta_origem):
                for arquivo in arquivos:
                    caminho_completo = os.path.join(raiz, arquivo)
                    
                    # Verifica se é um arquivo de código pela extensão
                    if any(arquivo.lower().endswith(ext) for ext in extensoes):
                        try:
                            with open(caminho_completo, 'r', encoding='utf-8') as entrada:
                                # Escreve separador com nome do arquivo
                                saida.write(f"\n\n=== ARQUIVO: {caminho_completo} ===\n\n")
                                # Escreve o conteúdo do arquivo
                                saida.write(entrada.read())
                                print(f"Processado: {caminho_completo}")
                        except UnicodeDecodeError:
                            # Tenta ler com outro encoding se utf-8 falhar
                            try:
                                with open(caminho_completo, 'r', encoding='latin-1') as entrada:
                                    saida.write(f"\n\n=== ARQUIVO: {caminho_completo} (latin-1) ===\n\n")
                                    saida.write(entrada.read())
                                    print(f"Processado (latin-1): {caminho_completo}")
                            except Exception as e:
                                print(f"Erro ao ler {caminho_completo}: {e}")
                        except Exception as e:
                            print(f"Erro ao processar {caminho_completo}: {e}")
            
            print(f"\nConsolidação concluída! Arquivo gerado: {arquivo_saida}")
    
    except Exception as e:
        print(f"Erro ao criar arquivo de saída: {e}")

if __name__ == "__main__":
    # Solicita ao usuário a pasta de origem
    pasta = input("Digite o caminho da pasta com os arquivos de código: ").strip()
    
    # Verifica se a pasta existe
    if os.path.isdir(pasta):
        consolidar_codigos(pasta)
    else:
        print(f"A pasta '{pasta}' não foi encontrada.")
