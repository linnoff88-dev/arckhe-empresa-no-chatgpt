# 2. Ficha do perfil (preencha antes de abrir o ChatGPT)

Com a ficha pronta, o cadastro leva poucos minutos e os dados ficam **iguais** em todo lugar
(Google, site, redes e ChatGPT). Dado diferente em cada lugar confunde a IA.

| Campo | O que o ChatGPT pede | Seu dado | Igual no Google e no site? |
|---|---|---|---|
| Nome | o nome como o cliente procura | | ☐ |
| Como atende | **local físico** (loja, consultório, escritório) ou **loja online** (site, marketplace) | | |
| Endereço | só para local físico | | ☐ |
| Site | obrigatório para loja online | | ☐ |
| Prova de que é sua | telefone comercial, e-mail da empresa, registro no DNS do site ou Shopify | | |
| Categoria | escolhida numa lista (pesquise por palavra: "IA", "contador", "dentista"…) | | |
| Descrição | **até 300 caracteres**: o que faz, para quem, como atende | | |
| Telefone | opcional e **público** | | ☐ |
| E-mail | opcional e **público** | | ☐ |
| Entrega | não faz / paga / grátis | | |
| Devolução | não aceita / com taxa / grátis + prazo em dias | | |
| Identidade | documento + selfie (Persona), feito pelo dono | | |
| Equipe | e-mails de quem vai cuidar junto (cada um com a própria conta) | | |

## Modelo de descrição (≤ 300 caracteres)

> `<NOME>` (`<site>`): `<o que faz>` para `<quem>`, `<como atende: online / em <cidade>>`.
> `<diferencial concreto>`. `<quem criou ou desde quando>`.

O nosso (295 caracteres):

> ARCKHÉ AI (ARCKHÉ AI): cursos, guias e projetos práticos de inteligência artificial, gratuitos e
> abertos, direto na internet, em português, inglês e espanhol. Ensina a usar IA no trabalho e no
> negócio (agentes, automação, vídeo com IA) com passo a passo e kit pronto. Criado por Nei Maldaner.

Para conferir tamanho e divergências: `python3 kit/conferir_perfil.py kit/exemplo-ficha.json`.
