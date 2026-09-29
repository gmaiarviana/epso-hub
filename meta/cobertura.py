"""Gera fontes/cobertura.md: o estado de encaixe de cada seção de cada fonte.

Uso, da raiz do repositório:  python meta/cobertura.py

Estados de uma seção (ver meta/roadmap.md e meta/processo-transcricoes.md):
  encaixada  — citada em arquivo fora de fontes/ que não é next-steps (acervo, meta/, elaborar);
  dispensada — declarada no campo `dispensadas` dos metadados da fonte (documento bruto
               inteiro: campo `dispensada`);
  pendente   — nenhum dos anteriores; com o tier quando algum next-steps.md a cita.

Uma citação vale para a fonte mencionada no mesmo bloco (parágrafo ou item de lista, com os
subitens): `arquivo.md#secao`, ou o nome do arquivo e, adiante no bloco, `#secao`. Um item de
fila que menciona a fonte e diz "arquivo inteiro" põe na fila toda seção ainda sem destino.
Documentos brutos (`fontes/documentos/`) são contados por arquivo, não por seção; o que tem
camada limpa (mesmo nome, sem `.raw`) conta pela limpa, por seção.
"""

import os
import re
import unicodedata

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SAIDA = os.path.join("fontes", "cobertura.md")


def norm(texto):
    texto = unicodedata.normalize("NFKD", texto).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]+", "-", texto).strip("-")


def ler(caminho):
    with open(os.path.join(RAIZ, caminho), encoding="utf-8") as f:
        return f.read()


def metadados(texto):
    """Devolve (titulo, dispensadas) do bloco YAML do topo; parser mínimo, sem dependências."""
    m = re.match(r"---\n(.*?)\n---", texto, re.S)
    titulo, dispensadas, dentro = "", {}, False
    if not m:
        return titulo, dispensadas
    for linha in m.group(1).splitlines():
        if linha.startswith("titulo:"):
            titulo = linha.split(":", 1)[1].strip()
        if linha.startswith("dispensada:"):
            dispensadas["*"] = linha.split(":", 1)[1].strip()
        if linha.startswith("dispensadas:"):
            dentro = True
            continue
        if dentro:
            sub = re.match(r"\s+([^:]+):\s*(.*)", linha)
            if not sub:
                dentro = False
                continue
            dispensadas[norm(sub.group(1))] = sub.group(2).strip()
    return titulo, dispensadas


def fontes():
    """Lista de fontes: caminho, slug (nome sem data), tipo, título, seções, dispensadas."""
    lista = []
    for pasta in ("fontes/transcricoes", "fontes/conversas", "fontes/documentos"):
        nomes = sorted(os.listdir(os.path.join(RAIZ, pasta)))
        for nome in nomes:
            if not nome.endswith(".md") or nome == "README.md":
                continue
            bruto = nome.endswith(".raw.md")
            base = nome[: -len(".raw.md")] if bruto else nome[: -len(".md")]
            # documento bruto com camada limpa conta pela limpa, por seção
            if bruto and f"{base}.md" in nomes:
                continue
            caminho = f"{pasta}/{nome}"
            texto = ler(caminho)
            titulo, dispensadas = metadados(texto)
            if not titulo:
                h1 = re.search(r"^# (.+)$", texto, re.M)
                titulo = h1.group(1).strip() if h1 else ""
            fonte = {"caminho": caminho, "base": base, "slug": base[11:], "titulo": titulo,
                     "dispensadas": dispensadas, "documento": bruto}
            if fonte["documento"]:
                fonte["secoes"] = []
            else:
                fonte["secoes"] = [(norm(h), h.strip()) for h in
                                   re.findall(r"^## (.+)$", texto, re.M)]
            lista.append(fonte)
    # transcrição só com bruto (sem camada limpa) conta por arquivo
    limpas = {f["base"] for f in lista}
    for nome in sorted(os.listdir(os.path.join(RAIZ, "fontes/transcricoes/raw"))):
        base = nome[: -len(".raw.md")] if nome.endswith(".raw.md") else None
        if base and base not in limpas:
            titulo, dispensadas = metadados(ler(f"fontes/transcricoes/raw/{nome}"))
            lista.append({"caminho": f"fontes/transcricoes/raw/{nome}", "base": base,
                          "slug": base[11:], "titulo": titulo, "dispensadas": dispensadas,
                          "documento": True, "secoes": []})
    return lista


def arquivos_que_citam():
    """(caminho, papel, texto) de cada .md fora de fontes/; papel é 'acervo' ou o tier da fila."""
    saida = []
    for pasta, subpastas, nomes in os.walk(RAIZ):
        rel = os.path.relpath(pasta, RAIZ).replace("\\", "/")
        subpastas[:] = [s for s in subpastas if not s.startswith(".")]
        if rel == "fontes" or rel.startswith("fontes/"):
            continue
        for nome in nomes:
            if not nome.endswith(".md"):
                continue
            caminho = nome if rel == "." else f"{rel}/{nome}"
            if nome == "next-steps.md":
                saida.append((caminho, "fila", ler(caminho)))
            else:
                saida.append((caminho, "acervo", ler(caminho)))
    return saida


def blocos(texto):
    """Quebra em blocos: parágrafo ou item de lista (cada subitem é um bloco). Devolve
    (título de seção ## sob o qual está, contexto, bloco); o contexto é o texto dos itens que
    envolvem um subitem, onde costuma estar o nome da fonte."""
    saida, secao, pilha = [], "", []  # pilha: [recuo, texto] do item atual e dos que o envolvem
    aberto = False

    for linha in texto.splitlines() + [""]:
        item = re.match(r"(\s*)(- |\d+\. )", linha)
        if not linha.strip() or linha.startswith("#") or item:
            if aberto:
                saida.append((secao, "\n".join(t for _, t in pilha[:-1]), pilha[-1][1]))
            aberto = False
            if linha.startswith("## "):
                secao = linha[3:].strip()
            if item:
                recuo = len(item.group(1))
                pilha = [p for p in pilha if p[0] < recuo] + [[recuo, linha]]
                aberto = True
            elif not linha.startswith("#") and not linha.strip():
                continue  # linha em branco dentro de uma lista mantém o contexto
            else:
                pilha = []
            continue
        if not aberto:
            pilha = [[-1, linha]]
            aberto = True
        else:
            pilha[-1][1] += "\n" + linha
    return saida


def menciona(f, texto, slugs):
    """O texto cita a fonte pelo nome do arquivo com data ou, se o nome curto (sem data) for
    único, por ele — nome inteiro, não pedaço de âncora ou de outro nome."""
    nomes = [f["base"]] + ([f["slug"]] if len(slugs.get(f["slug"], [])) == 1 else [])
    return any(re.search(rf"(?<![#\w])(?<!\w-){re.escape(n)}(?![\w-])", texto) for n in nomes)


def cruzar(lista, citantes):
    """Para cada fonte, preenche onde cada seção (ou o arquivo) é citada."""
    slugs = {}
    for f in lista:
        slugs.setdefault(f["slug"], []).append(f)
    for f in lista:
        f["acervo"] = {s: set() for s, _ in f["secoes"]}
        f["fila"] = {s: set() for s, _ in f["secoes"]}
        f["acervo_arquivo"], f["fila_arquivo"] = set(), set()
    por_caminho = {f["caminho"]: f for f in lista}
    # acervo antes da fila: "arquivo inteiro" só alcança o que ainda não está no acervo
    for caminho, papel, texto in sorted(citantes, key=lambda c: c[1] == "fila"):
        # legenda de fontes no topo do arquivo: - **[rótulo]** `fontes/…`
        legenda = {rotulo: por_caminho[c] for rotulo, c in
                   re.findall(r"\*\*\[([^\]]+)\]\*\*\s*`([^`]+)`", texto) if c in por_caminho}
        for secao, contexto, bloco in blocos(texto):
            local = caminho if papel == "acervo" else (
                f"{caminho} › {secao}" if secao else caminho)
            chave = "acervo" if papel == "acervo" else "fila"
            # citação por rótulo: [rótulo]`#secao`, `#outra` — vale até o próximo rótulo
            atual = None
            for rotulo, ancora in re.findall(r"\[([^\]]+)\]|#([^\s`)\],;:#*]+)", bloco):
                if rotulo:
                    atual = legenda.get(rotulo)
                elif atual:
                    s = norm(ancora).rstrip("-")
                    if s in atual[chave]:
                        atual[chave][s].add(local)
            ancoras = {norm(a) for a in re.findall(r"#([^\s`)\],;:#*]+)", bloco)}
            ancoras = {a.rstrip("-") for a in ancoras}
            for f in lista:
                if not menciona(f, contexto + "\n" + bloco, slugs):
                    continue
                f[f"{chave}_arquivo"].add(local)
                for s, _ in f["secoes"]:
                    if s in ancoras:
                        f[chave][s].add(local)
                if papel == "fila" and "arquivo inteiro" in bloco and menciona(f, bloco, slugs):
                    for s, _ in f["secoes"]:
                        if not f["acervo"][s] and not f["fila"][s]:
                            f["fila"][s].add(local + " (arquivo inteiro)")
        if papel == "acervo":
            # arquivo do acervo que declara a fonte uma vez e cita `#secao` adiante
            ancoras = {norm(a).rstrip("-") for a in re.findall(r"#([^\s`)\],;:#*]+)", texto)}
            for f in lista:
                if menciona(f, texto, {}):
                    for s, _ in f["secoes"]:
                        if s in ancoras:
                            f["acervo"][s].add(caminho)


def curto(local):
    """`next-steps.md › 2. Foco (arquivo inteiro)` vira `Foco`; next-steps de bloco fica pelo
    caminho."""
    arquivo, _, secao = local.partition(" › ")
    if arquivo == "next-steps.md" and secao:
        return re.sub(r"^\d+\. | \(arquivo inteiro\)$", "", secao)
    return arquivo.replace(" (arquivo inteiro)", "")


def estado_secao(f, s):
    """Devolve (estado, grupo): o grupo é o rótulo sob o qual a seção aparece nas pendências;
    vazio quando está concluída."""
    fila = ", ".join(sorted({curto(l) for l in f["fila"][s]}))
    if f["acervo"][s]:
        return "encaixada", (f"{fila}, com parte já encaixada" if f["fila"][s] else "")
    if f["fila"][s]:
        return "fila", fila
    if s in f["dispensadas"]:
        return "dispensada", ""
    return "pendente", "sem nota na fila"


def resumo(f):
    if f["documento"]:
        partes = (["citado"] if f["acervo_arquivo"] else []) + (
            ["na fila"] if f["fila_arquivo"] else [])
        if not partes and "*" in f["dispensadas"]:
            return "dispensado", "—"
        return "; ".join(partes) or "pendente", "—"
    estados = [estado_secao(f, s)[0] for s, _ in f["secoes"]]
    total = len(estados)
    encaixadas = sum(1 for s, _ in f["secoes"]
                     if f["acervo"][s] and not f["fila"][s]) + estados.count("dispensada")
    if encaixadas == total:
        rotulo = "completo"
    elif estados.count("encaixada") == 0:
        rotulo = "não iniciado"
    else:
        rotulo = "parcial"
    return rotulo, f"{encaixadas}/{total}"


def gerar():
    lista = fontes()
    cruzar(lista, arquivos_que_citam())
    linhas = [
        "# Cobertura das fontes",
        "",
        "Gerado por [meta/cobertura.py](../meta/cobertura.py) — não editar à mão. Estado de encaixe "
        "de cada fonte e, nas pendências, as seções que faltam encaixar, com o tier da fila quando "
        "houver. Regras em "
        "[meta/roadmap.md](../meta/roadmap.md) e "
        "[meta/processo-transcricoes.md](../meta/processo-transcricoes.md).",
        "",
        "Uma seção encaixada pode ainda ter ideia sem destino: o script vê a seção, não a ideia.",
        "",
        "## Resumo",
        "",
        "| Fonte | Estado | Concluídas |",
        "|---|---|---|",
    ]
    pendentes = 0
    for f in lista:
        rotulo, fracao = resumo(f)
        linhas.append(f"| [{f['base']}](../{f['caminho']}) | {rotulo} | {fracao} |")
    linhas += ["", "## Pendências", "",
               "Só o que não está concluído. Onde uma seção encaixada mora: buscar a âncora no "
               "repositório."]
    for f in lista:
        if f["documento"]:
            if not (f["acervo_arquivo"] or f["fila_arquivo"] or "*" in f["dispensadas"]):
                pendentes += 1
                linhas += ["", f"### {f['base']}", "", "- pendente, sem nota na fila"]
            continue
        grupos = {}
        for s, _ in f["secoes"]:
            estado, grupo = estado_secao(f, s)
            pendentes += estado in ("fila", "pendente") or bool(grupo)
            if grupo:
                grupos.setdefault(grupo, []).append(f"`#{s}`")
        if grupos:
            linhas += ["", f"### {f['base']}", ""]
            linhas += [f"- {g}: " + ", ".join(ss) for g, ss in sorted(grupos.items())]
    with open(os.path.join(RAIZ, SAIDA), "w", encoding="utf-8", newline="\n") as saida:
        saida.write("\n".join(linhas) + "\n")
    print(f"{SAIDA} gerado. Seções pendentes: {pendentes}.")
    return pendentes


if __name__ == "__main__":
    gerar()
