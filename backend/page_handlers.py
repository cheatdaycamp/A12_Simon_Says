from bottle import (Bottle, request, jinja2_view, redirect)
from backend import utils
from backend import controller

pageHandler = Bottle()

@pageHandler.get('/start')
@jinja2_view('./backend/pages/start.html')
def start():
    currentPlayer = request.get_cookie("player")
    if currentPlayer:
        redirect("/games")
        return
    return {"version" : utils.getVersion()}

@pageHandler.get('/games')
@jinja2_view('./backend/pages/games.html')
def games():
    currentPlayer = request.get_cookie("player")
    if not currentPlayer:
        redirect("/start")
        return
    return {"version" : utils.getVersion(), "games": controller.listGames(), "player": currentPlayer}

@pageHandler.delete('/games/<id>')
def delete_game(id):
    controller.delete_game(id)
    return redirect('/games')

@pageHandler.get('/games/<game_id>')
@jinja2_view('./backend/pages/game.html')
def play(game_id):
    currentPlayer = request.get_cookie("player")
    if not currentPlayer or not controller.gameExists(game_id):
        redirect("/start")
        return
    return {"version" : utils.getVersion()}

@pageHandler.get('/')
@jinja2_view('./backend/pages/index.html')
def landing():
    return {"version" : utils.getVersion()}

@pageHandler.get('/highscores')
@jinja2_view('./backend/pages/highscores.html')
def highscores():
    scores = controller.high_scores_retrieve()
    return {"version": utils.getVersion(), "scores": scores}