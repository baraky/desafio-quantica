# Desafio Técnico - Quantica
## Instruções de execução:
```
docker-compose up
```

## Instruções de uso:

Acessar http://localhost:15672/

**login**: guest
**senha**: guest

Publicar mensagem na queue ***fps_converter***, exemplo de payload:

```
{ "url": "https://edisciplinas.usp.br/pluginfile.php/5196097/mod_resource/content/1/Teste.mp4", "fps": 30 }
```
## Instruções adicionais:

Para configurar a quantidade de consumers (capacidade de processar mais de 1 vídeo por vez), basta mudar a variável **NUM_INSTANCES** no *docker-compose.yml*. Por padrão é iniciado três.
