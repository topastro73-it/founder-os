# 🖥️ Configurazione Macchine

## Come identificare la macchina

Usare `scutil --get LocalHostName` (stabile su qualsiasi rete), NON `hostname` (cambia in base alla rete).

> Questa tabella viene popolata automaticamente al primo avvio (`/setup` o `/routine start`):
> il sistema rileva il `LocalHostName` e, se non è registrato, chiede una volta sola di aggiungerlo.

| Nome macchina | LocalHostName | Model ID | RAM | Note |
|--------------|---------------|----------|-----|------|
| {{MACHINE_NAME}} | {{LOCAL_HOST_NAME}} | {{MODEL_ID}} | {{RAM}} | {{MACHINE_NOTE}} |
