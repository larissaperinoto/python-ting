def exists_word(word, instance):

    response = []

    for item, process in enumerate(instance.queue):
        ocorrencias = []

        for linha, l in enumerate(process['linhas_do_arquivo']):

            if word.lower() in l.lower():
                ocorrencias.append({"linha": linha + 1})

        if len(ocorrencias) > 0:
            response.append({
                "palavra": word,
                "arquivo": instance.queue[item]['nome_do_arquivo'],
                "ocorrencias": ocorrencias
            })

    return response


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
