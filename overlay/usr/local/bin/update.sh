#define _XOPEN_SOURCE 500
#include <stdio.h>
#include <string.h>
#include <dirent.h>
#include <ftw.h>
#include <stdbool.h>
#include <libgen.h>

// Caminho alvo para comparação
const char *TARGET_DIR = "/System/.installer/code/";

// Função para verificar se o arquivo existe (independente da extensão)
bool existe_correspondente(const char *nome_base) {
    DIR *dir;
    struct dirent *ent;
    bool encontrado = false;

    if ((dir = opendir(TARGET_DIR)) != NULL) {
        while ((ent = readdir(dir)) != NULL) {
            // Remove a extensão do arquivo encontrado no diretório de destino para comparar
            char nome_destino[256];
            strncpy(nome_destino, ent->d_name, sizeof(nome_destino));
            
            char *p_dot = strrchr(nome_destino, '.');
            if (p_dot) *p_dot = '\0';

            if (strcmp(nome_destino, nome_base) == 0) {
                encontrado = true;
                break;
            }
        }
        closedir(dir);
    }
    return encontrado;
}

// Função callback chamada para cada arquivo encontrado pela nftw
int processar_ficheiro(const char *fpath, const struct stat *sb, int typeflag, struct FTW *ftwbuf) {
    // Verificar se é um arquivo regular e termina em .link
    if (typeflag == FTW_F) {
        const char *ext = strrchr(fpath, '.');
        
        if (ext && strcmp(ext, ".link") == 0) {
            // Extrair apenas o nome do arquivo sem o caminho
            char *path_copy = strdup(fpath);
            char *filename = basename(path_copy);
            
            // Remover a extensão .link para a comparação
            char nome_base[256];
            strncpy(nome_base, filename, sizeof(nome_base));
            char *p_dot = strrchr(nome_base, '.');
            if (p_dot) *p_dot = '\0';

            if (existe_correspondente(nome_base)) {
                // --------------------------------------------------
                // ESPAÇO PARA O SEU CÓDIGO (RETORNOU TRUE)
                printf("[TRUE] Correspondencia encontrada para: %s\n", fpath);
                
                // --------------------------------------------------
            } else {
                // --------------------------------------------------
                // ESPAÇO PARA O SEU CÓDIGO (RETORNOU FALSE)
                printf("[FALSE] Sem correspondencia para: %s\n", fpath);

                // --------------------------------------------------
            }
            
            free(path_copy);
        }
    }
    return 0; // Continuar a busca
}

int main() {
    printf("Iniciando busca a partir da raiz (/)...\n");

    // nftw percorre a árvore. 20 é o número máximo de descritores de ficheiro abertos.
    if (nftw("/", processar_ficheiro, 20, FTW_PHYS) == -1) {
        perror("Erro ao percorrer o diretório");
        return 1;
    }

    return 0;
}