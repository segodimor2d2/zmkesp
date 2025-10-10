import os
import sys

def consolidar_codigos(pasta_origem, arquivo_saida='out_print_allfiles.md'):
    """
    Consolida todos os arquivos de código de uma pasta em um único arquivo Markdown.
    
    Args:
        pasta_origem (str): Caminho da pasta contendo os arquivos de código
        arquivo_saida (str): Nome do arquivo de saída consolidado
    """
    
    # Mapeamento de extensões para linguagens Markdown
    extensoes_linguagem = {
        '.py': 'python', '.js': 'javascript', '.java': 'java', '.c': 'c', '.cpp': 'cpp',
        '.h': 'c', '.html': 'html', '.css': 'css', '.php': 'php', '.rb': 'ruby',
        '.go': 'go', '.rs': 'rust', '.swift': 'swift', '.kt': 'kotlin', '.ts': 'typescript',
        '.sh': 'bash', '.sql': 'sql', '.md': 'markdown', '.txt': 'text', '.json': 'json', '.xml': 'xml'
    }
    
    try:
        with open(arquivo_saida, 'w', encoding='utf-8') as saida:
            # Escreve cabeçalho do documento
            saida.write(f"# Projeto da pasta: {pasta_origem}\n\n")
            
            # Percorre todos os arquivos na pasta
            for raiz, _, arquivos in os.walk(pasta_origem):
                for arquivo in arquivos:
                    caminho_completo = os.path.join(raiz, arquivo)
                    _, extensao = os.path.splitext(arquivo)
                    
                    # Verifica se é um arquivo de código pela extensão
                    if extensao.lower() in extensoes_linguagem:
                        linguagem = extensoes_linguagem[extensao.lower()]
                        try:
                            with open(caminho_completo, 'r', encoding='utf-8') as entrada:
                                # Escreve cabeçalho do arquivo
                                saida.write(f"## arquivo: {caminho_completo}\n\n")
                                # Abre bloco de código com a linguagem específica
                                saida.write(f"```{linguagem}\n")
                                # Escreve o conteúdo do arquivo
                                saida.write(entrada.read())
                                # Fecha bloco de código
                                saida.write("\n```\n\n\n")
                                print(f"Processado: {caminho_completo}")
                        except UnicodeDecodeError:
                            # Tenta ler com outro encoding se utf-8 falhar
                            try:
                                with open(caminho_completo, 'r', encoding='latin-1') as entrada:
                                    saida.write(f"## arquivo: {caminho_completo} (latin-1)\n\n")
                                    saida.write(f"```{linguagem}\n")
                                    saida.write(entrada.read())
                                    saida.write("\n```\n\n\n")
                                    print(f"Processado (latin-1): {caminho_completo}")
                            except Exception as e:
                                saida.write(f"*Erro ao ler arquivo: {e}*\n\n")
                                print(f"Erro ao ler {caminho_completo}: {e}")
                        except Exception as e:
                            saida.write(f"*Erro ao processar arquivo: {e}*\n\n")
                            print(f"Erro ao processar {caminho_completo}: {e}")
            
            print(f"\nConsolidação concluída! Arquivo gerado: {arquivo_saida}")
    
    except Exception as e:
        print(f"Erro ao criar arquivo de saída: {e}")

if __name__ == "__main__":
    pasta = sys.argv[1:][0]

    # Verifica se a pasta existe
    if os.path.isdir(pasta):
        consolidar_codigos(pasta)
    else:
        print(f"A pasta '{pasta}' não foi encontrada.")
