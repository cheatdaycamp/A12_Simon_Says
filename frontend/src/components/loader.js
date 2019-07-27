import React from "react";

//loader animation when joinning a game
export default class Loader extends React.Component {
    render() {
        return
        <div className="lds-ellipsis">
            <div></div>
            <div></div>
            <div></div>
            <div></div>
        </div>
    }
}