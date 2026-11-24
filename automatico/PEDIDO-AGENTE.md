# Como a gente fez o cadastro de forma automática

Quem fez o cadastro da linnoff88-dev LTDA foi um agente: o **Claude Code** com a extensão **Claude in Chrome**
(o agente usa o seu navegador já logado) e, para o DNS, o script `txt_cloudflare.py` deste kit.
O dono só deu três "sim": cadastrar, usar a API do Cloudflare para o registro TXT e (depois) a selfie.

## O que o agente fez sozinho (22/11/2026, ~10 minutos)

1. Abriu `chatgpt.com/business-hub` no Chrome logado na conta da empresa.
2. Pesquisou "linnoff88-dev" e "ARCKHÉ" e mostrou o problema (só aparecia o instituto da Bahia).
3. Clicou em **Criar 'linnoff88-dev LTDA'** → **Começar** → **Loja online** → site `https://ARCKHÉ AI`.
4. Leu a tela do registro TXT (host `openai-business-profile` + valor) e **parou para pedir o OK** do dono.
5. Com o OK, criou o TXT no Cloudflare (`txt_cloudflare.py`), conferiu no DNS público e clicou em **Verificar domínio**.
6. Escolheu a categoria, escreveu a descrição (e encurtou para 300 caracteres quando viu o corte), marcou entrega e devolução e enviou.
7. Abriu a visão geral, salvou os prints e avisou: falta a identidade (Persona), que só o dono faz.

## Onde o agente PARA (de propósito)

- Antes de mexer no DNS (é configuração do seu domínio).
- No código do telefone, na selfie e no documento: isso é do dono.
- Telefone e e-mail públicos: só com o dado que o dono passar.

## Pedido para colar no Claude Code (com Claude in Chrome)

```text
Quero cadastrar a minha empresa no ChatGPT (Central de Negócios, chatgpt.com/business-hub).
Leia o kit em https://github.com/linnoff88-dev/empresa-no-chatgpt (kit/2-ficha-do-perfil.md e kit/3-dicas.md).

Dados da empresa:
- nome: <NOME>
- como atende: <local físico | loja online>
- site: <URL>            endereço (se físico): <ENDEREÇO>
- categoria que eu quero: <PALAVRA>
- o que fazemos (vou revisar a descrição): <2 ou 3 frases>

Regras:
1. Use o meu Chrome (já logado na conta da EMPRESA no ChatGPT). Não troque de conta.
2. Primeiro rode o teste do kit (kit/1-teste-o-que-o-chatgpt-diz.md) e me mostre o "antes".
3. Pesquise o nome curto e o completo. Se achar a minha empresa, escolha a do meu endereço; senão, "Criar".
4. Escreva a descrição com no máximo 300 caracteres e me mostre antes de enviar.
5. PARE e me pergunte antes de: aceitar termos, mexer no DNS, colocar telefone ou e-mail público, e enviar.
6. Código por telefone, documento e selfie são comigo: me avise e espere.
7. No fim, salve prints de cada tela e me diga o status (rascunho ou verificado) e o que falta.
```

## Script do DNS (Cloudflare)

`txt_cloudflare.py` cria o registro TXT pela API do Cloudflare e espera ele aparecer no DNS público.
Token no ambiente (`CLOUDFLARE_API_TOKEN`, permissão *Zone → DNS → Edit*), nunca no código:

```bash
export CLOUDFLARE_API_TOKEN=...        # ou carregue do seu .env
python3 automatico/txt_cloudflare.py --dominio seusite.com.br \
  --host openai-business-profile --valor "openai-business-profile=ungi_..." --dry-run   # mostra o que vai fazer
python3 automatico/txt_cloudflare.py --dominio seusite.com.br \
  --host openai-business-profile --valor "openai-business-profile=ungi_..."             # cria e confere
```

Seu DNS não é Cloudflare? Copie host e valor da tela do ChatGPT no painel do seu provedor
(Registro.br, Hostinger, GoDaddy…), tipo **TXT**, e confira com `bash automatico/conferir_txt.sh seusite.com.br`.
