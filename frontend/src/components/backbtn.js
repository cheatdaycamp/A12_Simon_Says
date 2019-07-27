import React from "react";

// Back button component:
export default class BackBtn extends React.Component {
    constructor() {
        super();
    }
    gamesPage() {
        fetch('/games', {method: "GET", redirect: 'follow'})
            .then(function(response) {
                window.location = response.url
            })
    }
    render() {
        return (
            <button onClick={this.gamesPage.bind(this)} className="send-to-games-btn">Back</button>
        )
    }
}
