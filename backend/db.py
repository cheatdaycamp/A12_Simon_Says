from backend import dbutils

def getAllGames():
    return dbutils.queryAll("SELECT * FROM game")

def getGame(game_id):
    return dbutils.queryOne("SELECT * FROM game where id = {}".format(game_id))

def newGame(name, creator, sequence):
    return dbutils.updateOrInsert("INSERT INTO game (name, sequence, creator) VALUES ('{}', '{}', '{}')".format(name, sequence, creator))

def updateGameStatus(game_id, status):
    return dbutils.updateOrInsert("UPDATE game SET status = '{}' WHERE id = '{}' ".format(status, game_id))

def updateGameStatusAndStep(game_id, status, new_step):
    return dbutils.updateOrInsert("UPDATE game SET status = 'won', step='{}' WHERE id = '{}'".format(new_step, game_id))

def updateGameStep(game_id, new_step):
    return dbutils.updateOrInsert("UPDATE game SET step = '{}' WHERE id = '{}'".format(new_step, game_id))

def getGamePlayers(game_id):
    return dbutils.queryAll("SELECT * FROM playergame where game = {} ORDER BY created".format(game_id))

def newPlayer(player_name, player_av):
    return dbutils.updateOrInsert("INSERT INTO player (id,avatar) VALUES ('{}','{}')".format(player_name,player_av))

def joinGame(game_id, player_id):
    avatar=dbutils.queryOne("SELECT avatar FROM player WHERE id=('{}')".format(player_id))
    avatar=avatar['avatar']
    print(avatar)
    return dbutils.updateOrInsert("INSERT INTO playergame (game, player, avatar) VALUES ('{}', '{}', '{}')".format(game_id, player_id, avatar))

def updatePlayerStatus(game_id, player_id, status):
    return dbutils.updateOrInsert("UPDATE playergame SET status = '{}' WHERE game = '{}' AND player='{}'".format(status, game_id, player_id))

def getReadyPlayers(game_id):
    return dbutils.queryAll("SELECT * FROM playergame WHERE game = '{}' AND status = 'ready'".format(game_id))

def setFirstTurn(game_id):
    return dbutils.updateOrInsert("UPDATE playergame SET status = 'turn' WHERE game = '{}' ORDER BY created ASC LIMIT 1".format(game_id))


def getNextPlayer(game_id, last_player):
    player = dbutils.queryOne("""SELECT * FROM playergame WHERE
                             game = '{game_id}' AND 
                             player <> '{last_player}' AND status <> 'failed' AND created > (SELECT created FROM playergame WHERE player ='{last_player}' AND game = {game_id})
                             ORDER BY created ASC LIMIT 1
                             """.format(game_id = game_id, last_player=last_player))
    if not player:
        player = dbutils.queryOne("SELECT * FROM playergame WHERE game = '{game_id}' AND status <> 'failed' ORDER BY created ASC LIMIT 1".format(game_id = game_id))
    if player:
        return player["player"]
    return None

def updateWonPlayers(game_id):
    return dbutils.updateOrInsert("UPDATE playergame SET status = 'won'  WHERE game = '{}' AND status <> 'failed'".format(game_id))

def delete_game(id):
    dbutils.delete_game(id)

def high_scores_retrieve():
    return dbutils.high_scores_retrieve()