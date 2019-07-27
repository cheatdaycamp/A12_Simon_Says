import React from "react";

export default class GamePrompt extends React.Component {
    constructor() {
        super();
    }
    render() {
        return(
            <div className="gm-prompt">
                <div>{this.props.name}</div>
                <div>{this.props.status}</div>
            </div>
        )
    }
}