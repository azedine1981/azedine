#L'instruction match confronte la valeur d'une expression à plusieurs filtres successifs donnés par les instructions case. L’instruction match peut faire penser au switch que l'on trouve dans les langages C, Java, JavaScript et autres, mais elle ressemble plus au filtrage par motif des langages Rust et Haskell. Seul le premier filtre qui correspond est exécuté et elle permet aussi d'extraire dans des variables des composantes de la valeur, comme les éléments d'une séquence ou les attributs d'un objet.
def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"
