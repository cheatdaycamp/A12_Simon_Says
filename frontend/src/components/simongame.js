import React from "react";
import {getGameId, ajax} from "../utils"
import Simon from "./simon"
import Players from "./players"
import Sequence from "./sequence"
import BackBtn from "./backbtn"
<<<<<<< HEAD
=======
import GamePrompt from "./gameprompt"

>>>>>>> 8e328eec2f71898d6c1dc1785ea329343f257270

export default class SimonGame extends React.Component {
    constructor(){
        super();
        this.state = {game:{status:"loading", sequence:[]}, user:{name:"", status:""}, players:[], prompt: "prompt-hide"}
        this.playTurn = this.playTurn.bind(this);
    }

    componentDidMount() {
        this.gameLoop();
    }

    gameLoop(){
        ajax(`/games/${getGameId()}/status`, {},  (newStatus) => {
            this.setState(() => (newStatus), () => {
                //Poll the status only if the game is not over
                if (newStatus.game.status != "failed" && newStatus.game.status != "won"){
                    setTimeout(() => {this.gameLoop()}, 2000);
                } else {
                    this.setState({prompt: "prompt"})
                }
             });
        });
    }

    isViewMode(){
        return this.state.user.status == "viewer" && this.state.game.status === "on";
    }

    playTurn(){
        this.setState({
            user: {name: this.state.user.name, status: "not turn"}
        })
    }

    render() {
        return <div className="main">
                <div className={this.state.prompt}>
                    <GamePrompt name={this.state.user.name} status={this.state.user.status}/>
                </div>
                <div className="center">
                    <Simon  sequence={this.state.game.sequence} disabled={this.state.user.status != "turn"} playTurn={this.playTurn} showPlayBtn={this.state.user.status == "new"}/>
                    <Sequence sequence={this.state.game.sequence} step={this.state.game.step} />
                </div>
                <div className="side">
                    <div className="game-name">{this.state.game.name}</div>
                    {(this.isViewMode()) && <div className="view-mode" >View mode</div>}
                    <div className={`game-status ${this.state.game.status}`}>{this.state.game.status}</div>
                    <Players players={this.state.players} userName={this.state.user.name} showJoinBtn={ this.state.user.status == "viewer" && this.state.game.status === "open"} />
                    <BackBtn/>
                </div>
            </div>
    }
}