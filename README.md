HW ASSASSIN
==========

This repo is a couple of hours of messing around with James Lennon's HW
Assassin app endpoints to see what kind of information can be gleaned.


GAME STATE REQUEST
------

```
POST http://hwassassin.hwtechcouncil.com/game/get_state
```

```
key=encrypted base64 key
```

The key is based on the value returned by add_player.

REGISTER AS PLAYER
-------

`POST http://hwassassin.hwtechcouncil.com/players/add_player`

```
  image=base64 image data
  name=full name
  year=2015
  school_id=115-010
```

Response:

```
{"key":"base64 encoded encrypted data"}
```

Appears to be an encrypted (probably with secret) key. Probably not
forgeable without source code of the app.

SIGNIFICANT VULNERABILITIES
-------

There is a problem, `school_id` is displayed for all of the top 25
players. This should be considered a secret. [Data
dump](https://gist.github.com/paralin/812e93282fd45869592b) acquired
using this vulnerability.
