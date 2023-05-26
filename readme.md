# PoC: Twitch Bot & Overlay

## TwitchIO

Créer un fichier `.env` :

```
TMI_TOKEN= # https://twitchapps.com/tmi/
CLIENT_ID= # Identifiant Twitch de l'app à créer sur https://dev.twitch.tv
BOT_NICK= # Pseudo du Bot, doit correspondre au compte connecté pour TMI_TOKEN
BOT_PREFIX= # Préfixe des commandes ("!" par exemple)
CHANNEL= # Nom de la chaîne
```

## Lancer le script Python

``py main.py``

## Overlay

* URL : `http://localhost:8000`

## Websocket

* URL : `ws://localhost:8001`

## VueJS

Pour travailler sur l'overlay (http://localhost:5173) :

```
cd overlay
npm run dev
```

Il faut build l'application Vue pour que les modifications soient visibles dans l'overlay :

```
cd overlay
npm run build
```