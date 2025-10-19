
def fifo(paginas, limite_quadros):
    quadros = [] 
    ultima_pagina = paginas[-1] 
    
    for pagina in paginas:
        if pagina not in quadros:
          
            if len(quadros) < limite_quadros:
                quadros.append(pagina)
            else:
                quadros.pop(0) 
                quadros.append(pagina) 
    

    indice_ultima_pagina = quadros.index(ultima_pagina) if ultima_pagina in quadros else None
    

    indice_legivel = indice_ultima_pagina + 1 if indice_ultima_pagina is not None else "N/A"
    
    print("Quadros finais:", quadros)
    print(f"FIFO A última página ({ultima_pagina}) está no quadro:", indice_legivel, "\n")


sequencias = [
    [4, 3, 25, 8, 19, 6, 25, 8, 16, 35, 45, 22, 8, 3, 16, 25, 7],
    [4, 5, 7, 9, 46, 45, 14, 4, 64, 7, 65, 2, 1, 6, 8, 45, 14, 11],
    [4, 6, 7, 8, 1, 6, 10, 15, 16, 4, 2, 1, 4, 6, 12, 15, 16, 11]
]

limite_quadros = 8 


for i, paginas in enumerate(sequencias, 1):
    print(f"===== Sequência {i} =====")
    fifo(paginas, limite_quadros)