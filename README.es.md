# Empresa en ChatGPT

[![Empresa en ChatGPT](guia/assets/banner-es.jpg)](https://inematds.github.io/empresa-no-chatgpt/guia/es/)

**🇧🇷 [Português](README.md) · 🇺🇸 [English](README.en.md) · 🇪🇸 [Español](README.es.md)**

## Qué es

**Empresa en ChatGPT** es un kit gratuito para reclamar el perfil de tu empresa en la **Central de Negocios de ChatGPT** (el «Business Hub», lanzado por OpenAI en noviembre de 2026), similar al perfil de empresa de Google. Es para quienes tienen una tienda, consultorio, oficina o venden por internet. Incluye una prueba de lo que ChatGPT dice hoy sobre tu empresa, una ficha para completar, consejos sobre lo que nos salió mal y una solicitud lista para que un agente de IA haga el registro en tu navegador. Para hacerlo manualmente, solo necesitas una cuenta de ChatGPT, incluso la gratuita, y no tiene costo. El proceso con un agente es opcional y usa Claude Code (Anthropic), que requiere un plan de pago de Claude y una computadora con Chrome.

**Puedes recuperar el control de tu empresa en ChatGPT.** Hoy, ChatGPT responde sobre tu empresa con lo que encuentra por ahí. Cuando buscamos «INEMA», mostró el instituto de medio ambiente de Bahía, con 6 direcciones. Ninguna era la nuestra.

## 📖 Guía de uso

Guía completa (página de presentación + paso a paso, con capturas reales): **https://inematds.github.io/empresa-no-chatgpt/guia/es/**

## Los 3 pasos

1. **Encuentra tu empresa:** `chatgpt.com/business-hub` → busca el nombre corto y el completo → elige la que corresponda a tu dirección o selecciona **Crear**.
2. **Demuestra que es tuya:** ubicación física = código enviado al teléfono comercial; tienda online = un registro TXT en el DNS del sitio (también hay opciones de correo de la empresa y Shopify).
3. **Di quién eres:** categoría, descripción de hasta 300 caracteres, entregas, devoluciones → identidad (documento + selfie) → invita a tu equipo.

## Pídele al agente que lo haga (la solicitud)

Opcional y con costo adicional: pega la solicitud en [Claude Code](https://claude.com/claude-code) con la extensión [Claude in Chrome](https://claude.com/claude-in-chrome) (usa tu navegador, donde ya iniciaste sesión; requiere un plan de pago de Claude). Sin agente, sigue los 3 pasos anteriores manualmente y gratis. La solicitud completa y lo que hizo el agente en nuestro caso están en [`automatico/PEDIDO-AGENTE.md`](automatico/PEDIDO-AGENTE.md) (en portugués).

```text
Quiero registrar mi empresa en ChatGPT (Central de Negocios, chatgpt.com/business-hub).
Lee el kit en https://github.com/inematds/empresa-no-chatgpt (los consejos y la ficha del perfil).
Datos: nombre <NOMBRE>, <ubicación física o tienda online>, sitio web <SITIO>, dirección <DIRECCIÓN>, qué hacemos <2 o 3 frases>.
Usa mi navegador, con la sesión iniciada en la cuenta de la EMPRESA. Primero, haz la prueba del kit. Descripción de máximo 300 caracteres.
Detente y pregúntame antes de aceptar términos, modificar el DNS, publicar el teléfono o el correo electrónico y enviar.
Yo me encargo del código del teléfono, el documento y la selfie. Al final, capturas de pantalla y lo que falta.
```

## El kit

| Archivo | Para qué sirve |
|---|---|
| [`kit/1-teste-o-que-o-chatgpt-diz.md`](kit/1-teste-o-que-o-chatgpt-diz.md) (en portugués) | 8 preguntas para ver qué dice ChatGPT sobre ti + ficha de antes y después |
| [`kit/2-ficha-do-perfil.md`](kit/2-ficha-do-perfil.md) (en portugués) | Todos los campos que pide el registro + modelo de descripción de ≤ 300 caracteres |
| [`kit/3-dicas.md`](kit/3-dicas.md) (en portugués) | 19 consejos de nuestro registro real: qué salió mal y cómo evitarlo |
| [`automatico/PEDIDO-AGENTE.md`](automatico/PEDIDO-AGENTE.md) (en portugués) | Cómo hizo el agente el registro por su cuenta y la solicitud para copiar y pegar |
| [`kit/conferir_perfil.py`](kit/conferir_perfil.py) | Revisa la ficha: descripción de ≤ 300 caracteres y que el nombre, el sitio y el teléfono coincidan en todas partes |
| [`automatico/txt_cloudflare.py`](automatico/txt_cloudflare.py) | Crea el registro TXT en Cloudflare y espera a que aparezca en el DNS público |
| [`automatico/conferir_txt.sh`](automatico/conferir_txt.sh) | Comprueba si el TXT ya aparece (cualquier proveedor de DNS) |

## La prueba (22/11/2026)

- **Antes:** «INEMATDS» → ninguna empresa; «INEMA» → instituto de medio ambiente de Bahía, 6 direcciones.
- **Después:** INEMATDS LTDA creada por el agente en unos 10 minutos, tienda online, **inema.club verificado** por DNS, categoría «Empresa de IA». Estado: borrador hasta que el propietario verifique su identidad.
- Fuente de la función: [OpenAI, «Empresas en ChatGPT»](https://openai.com/pt-BR/index/introducing-businesses-chatgpt/) (beta; las reglas pueden cambiar).

---

## Instalación técnica

Requisitos previos: Python 3.10+, `dig` (paquete `dnsutils`/`bind-utils`) para comprobar el DNS. Para crear el TXT con el script: dominio en Cloudflare y un token con permiso *Zone → DNS → Edit*. Sin dependencias externas.

```bash
git clone https://github.com/inematds/empresa-no-chatgpt && cd empresa-no-chatgpt

# comprobar la ficha antes del registro
python3 kit/conferir_perfil.py kit/exemplo-ficha.json          # copia y edita el ejemplo

# crear el TXT de verificación en Cloudflare (el token solo en el entorno, nunca en el código)
export CLOUDFLARE_API_TOKEN=...
python3 automatico/txt_cloudflare.py --dominio seusite.com.br \
  --valor "openai-business-profile=ungi_..." --dry-run          # muestra lo que hará
python3 automatico/txt_cloudflare.py --dominio seusite.com.br \
  --valor "openai-business-profile=ungi_..."                    # crea y espera a que aparezca

# comprobar el TXT con cualquier proveedor
bash automatico/conferir_txt.sh seusite.com.br

# pruebas (10 casos: límite de 300, diferencias en sitio/teléfono, tipo local sin dirección, nombre del TXT, dry-run)
python3 -m unittest discover -s tests
```

`txt_cloudflare.py` termina con código 0 cuando aparece el TXT en el DNS público, 1 si hay un error y 2 si se creó, pero aún no se propagó.

## El proceso, de principio a fin

| # | Paso | Comando / dónde | Quién |
|---|---|---|---|
| 1 | Prueba del «antes» | Las 8 preguntas de `kit/1-teste-o-que-o-chatgpt-diz.md` (en portugués) en ChatGPT | 🧠 propietario (o el agente) |
| 2 | Ficha del perfil | `python3 kit/conferir_perfil.py minha-ficha.json` | 🧠 propietario |
| 3 | Abrir la Central y buscar | `chatgpt.com/business-hub` en el navegador con la sesión iniciada en la cuenta de la empresa | 🤖 agente (Claude in Chrome) |
| 4 | Crear o elegir la empresa | «Crear '<nombre>'» → Empezar → ubicación física / tienda online | 🤖 agente |
| 5 | Demostrar que es tuya | DNS: `python3 automatico/txt_cloudflare.py …` → «Verificar dominio» · teléfono: código | ⚙️ script (con el visto bueno del propietario) / 🧠 propietario |
| 6 | Categoría, descripción, entregas, devoluciones → Enviar | Formulario | 🤖 agente (muestra antes de enviar) |
| 7 | Identidad (Persona: documento + selfie) | Botón «Verificar» en la vista general | 🧠 propietario |
| 8 | Invitar al equipo | «Invitar» en la Central | 🧠 propietario |
| 9 | Prueba del «después» (7 días) | Las mismas 8 preguntas | 🧠 propietario |

## Uso responsable

Reclama solo una empresa que sea tuya o que representes. No publiques un teléfono o correo electrónico que no pueda recibir consultas de clientes. El kit no garantiza una posición en las respuestas de ChatGPT.

Proyectos y cursos gratuitos: https://inema.club · Licencia MIT.