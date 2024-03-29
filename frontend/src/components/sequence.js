import React from "react";
import SequenceLight from "./sequenceLight"

//Lights up the color sequence received
export default class Sequence extends React.Component {
    render() {
        return <div className="sequence">
            {this.props.sequence.map((s, index) => (
                <SequenceLight key={index} color={s} show={(this.props.step > index)}/>
            ))}
        </div>
    }
}