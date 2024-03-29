import React from "react";
import {getGameId, ajax} from "../utils"
import Loader from "./loader"

//component that handles the players that joined the game:
export default class Players extends React.Component {
    constructor(props){
        super(props);
        this.state = {joinClicked:false};
    }

    join(){
        if (this.state.joinClicked){
            return;
        }
        this.setState(() => ({
            joinClicked:true
        }), () => { 
            ajax(`/games/${getGameId()}/players`,{method: 'POST'});
        });
    }

    render() {
        return <div className="players">
            <h3>Players</h3><ul className="players">
            {this.props.showJoinBtn &&
            <button className={`join-btn ${(this.state.joinClicked) ? "loading" : ""}`} onClick={this.join.bind(this)}>
            {(this.state.joinClicked) ? <Loader />: "Join!" }
            </button>
            }
            {this.props.players.map(k => (
                <li key={k.player} className="player" >
                <img className="player-avatar" src={"../images/"+k.avatar+".png"}></img>
                <span className="player-name">{k.player} {(k.player === this.props.userName) ? "(you)":""}</span>
                <span className={`player-status ${k.status}`}>{k.status}</span>
                </li>
            ))}
            </ul>
            </div>
    }
}